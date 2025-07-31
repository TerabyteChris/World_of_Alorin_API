import os
import json
from datetime import datetime
from google.generativeai import GenerativeModel, configure
import streamlit as st
import uuid
from storage import load_history, save_message, get_all_thread_ids, load_full_save, get_user_session_path, load_summary_cache, sanitize_email
from token_tracker import add_token_usage, get_token_usage
from gemini_utils import get_total_tokens, summarize_in_background, summarize_chat_history_with_gemini
from campaign_utils import (
    list_campaigns, create_campaign,
    list_sessions, create_session,
    readable_session_names, extract_session_id
)
from prompt_loader import load_prompt
from save_helpers import get_save_file_path, save_file_to_text
from merge_save_files import merge_save_files

MAX_TOKENS_BEFORE_SUMMARY = 10000
MAX_TOKENS_PER_THREAD = 30000

def build_session_path(session_id, user_id, campaign_name):
    return os.path.join("saves", sanitize_email(user_id), campaign_name, "sessions", f"{session_id}.json")


# Enforce login
if not st.user.is_logged_in:
    if st.button("Log in with Google"):
        st.login()
        st.rerun()  # <-- Required to reload app state
    st.stop()


# === Streamlit Setup ===
st.set_page_config(page_title="World of Alorin Chat", layout="wide")
st.title("🗺️ World of Alorin – Narrated Chat")
tab1, tab2 = st.tabs(["Chat", "Campaign"])

# === Gemini Client Setup ===
configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = GenerativeModel("gemini-2.5-flash")

# === Session State ===
# Load previous history if not already loaded
all_threads = get_all_thread_ids()

# Set a valid thread_id at start if needed
if "session_id" not in st.session_state or st.session_state.session_id in (None, "None", ""):
    if all_threads and all_threads[0] not in (None, "None", ""):
        st.session_state.session_id = all_threads[0]
    else:
        st.session_state.session_id = str(uuid.uuid4())

if not st.session_state.get("messages_loaded"):
    messages, _ = load_history(st.session_state.session_id, user_id=st.user.email)
    if messages:
        st.session_state.messages = messages
        st.session_state.messages_loaded = True
if "messages" not in st.session_state:
    st.session_state.messages = []
if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0
if "tokens_since_summary" not in st.session_state:
    st.session_state.tokens_since_summary = 0
if "tokens_since_rollover" not in st.session_state:
    st.session_state.tokens_since_rollover = 0
cumulative_tokens = get_total_tokens(st.session_state.session_id, st.user.email)
session_path = get_user_session_path(st.session_state.session_id, st.user.email)
if session_path and os.path.exists(session_path):
    with open(session_path, "r", encoding="utf-8") as f:
        session_data = json.load(f)
        st.session_state.tokens_since_summary = session_data.get("tokens_since_summary", 0)
        st.session_state.tokens_since_rollover = session_data.get("tokens_since_rollover", 0)

# === Sidebar ===
with st.sidebar:
    # --- Auth Info ---
    st.markdown(f"👤 **{st.user.name}**")
    st.markdown(f"📧 {st.user.email}")

    # --- Campaigns ---
    campaigns = list_campaigns(st.user.email)
    campaign_names = [c["name"] for c in campaigns]

    if campaign_names:
        selected_campaign_name = st.selectbox("🎲 Select Campaign", campaign_names)
    else:
        selected_campaign_name = None
        st.warning("No campaigns found. Please create one to continue.")


    if "creating_campaign" not in st.session_state:
        st.session_state.creating_campaign = False

    new_name = st.text_input("➕ New Campaign Name", key="new_campaign_name")

    if st.button("Create Campaign"):
        st.session_state.creating_campaign = True

    if st.session_state.creating_campaign and new_name:
        new_campaign = create_campaign(st.user.email, new_name)
        st.session_state.campaign_id = new_campaign["id"]
        st.session_state.session_id = None
        st.session_state.creating_campaign = False
        st.session_state.is_new_campaign = True
        st.rerun()
    # Store selected campaign ID
    if selected_campaign_name:
        for c in campaigns:
            if c["name"] == selected_campaign_name:
                st.session_state.campaign_id = c["id"]
                st.session_state.campaign_name = selected_campaign_name
                break
    else:
        st.session_state.campaign_id = None
        st.session_state.campaign_name = None


    # --- Sessions ---
    if st.session_state.get("campaign_id"):
        sessions = list_sessions(st.user.email, st.session_state.campaign_id)
        session_options = readable_session_names(sessions)
        selected_session = st.selectbox("📘 Select Session", session_options, key="session_selectbox")

        # Store current ID if not already stored
        if "previous_session_id" not in st.session_state:
            st.session_state.previous_session_id = None

        selected_id = extract_session_id(selected_session)

        # Only update session state if changed
        if selected_id != st.session_state.previous_session_id:
            st.session_state.session_id = selected_id
            st.session_state.messages = []
            st.session_state.messages_loaded = False
            st.session_state.previous_session_id = selected_id
            st.rerun()

        st.session_state.campaign_name = selected_campaign_name


    # --- Token Usage ---
    if st.session_state.get("session_id"):
        cumulative_tokens = get_token_usage(
            st.session_state.session_id,
            campaign_name=st.session_state.campaign_name,
            user_id=st.user.email
        )
        st.markdown(f"**🧠 Tokens Used:** {cumulative_tokens['total']:,}")
        st.progress(min(cumulative_tokens['total'] / MAX_TOKENS_PER_THREAD, 1.0))

    # --- Logout ---
    st.markdown("---")
    if st.button("🚪 Log Out"):
        st.logout()


with tab1:
    if not st.session_state.get("campaign_id") or not st.session_state.get("session_id"):
        st.info("Please select a campaign and session to begin.")
        st.stop()
    with st.container(height=450):
        # === 1. Render Chat History First ===
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # === 2. Chat Input Box LAST so it stays at bottom ===
    prompt = st.chat_input("Speak your will, adventurer...")

    # === 3. Handle Submission ===
    if prompt:
        # === Determine the prompt header type ===
        if st.session_state.get("is_new_campaign"):
            prompt_header = load_prompt("new_campaign_prompt")
        elif summary_cache := load_summary_cache(st.session_state.session_id, user_id=st.user.email):
            prompt_header = load_prompt("continuation_prompt")
        else:
            prompt_header = load_prompt("startup_script")

        # === Construct system prompt ===
        system_prompt = load_prompt("static_instructions") + "\n\n" + prompt_header

        # === Get the chat history ===
        messages, _ = load_history(st.session_state.session_id, st.user.email)
        formatted_history = [
            {
                "role": m["role"],
                "parts": [{"text": m["content"]}]
            }
            for m in messages if m["role"] in {"user", "model"}
        ]

        # === 3. Create the chat object ===
        # Inject system prompt as first user message
        formatted_history.insert(0, {
            "role": "model",
            "parts": [{"text": system_prompt}]
        })

        chat = model.start_chat(
            history=formatted_history
        )


        # Only reset system_prompt once it's used
        if st.session_state.get("system_prompt"):
            st.session_state.system_prompt = None



        # Reset the campaign flag after first prompt submission
        if st.session_state.get("is_new_campaign"):
            st.session_state.is_new_campaign = False
        response_stream = chat.send_message(prompt, stream=True)

        response_text = ""
        for chunk in response_stream:
            if not chunk.candidates:
                continue
            parts = chunk.candidates[0].content.parts
            if not parts:
                continue
            response_text += parts[0].text


        # Save both user and assistant messages *after* response is complete
        st.session_state.messages.append({"role": "user", "content": prompt})
        save_message(st.session_state.session_id, "user", prompt, user_id=st.user.email)

        # Extract usage info before saving
        total_token_count = 0
        if hasattr(response_stream, "usage_metadata") and response_stream.usage_metadata:
            usage = response_stream.usage_metadata
            total_token_count = usage.total_token_count
            st.session_state.total_tokens += total_token_count
            st.session_state.tokens_since_summary += total_token_count
            st.session_state.tokens_since_rollover += total_token_count
            add_token_usage(
                st.session_state.session_id,
                {
                    "prompt_tokens": usage.prompt_token_count,
                    "completion_tokens": usage.candidates_token_count,
                    "total_tokens": total_token_count
                },
                campaign_name=st.session_state.campaign_name,
                user_id=st.user.email
            )
            

        # Save messages (assistant includes token usage)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        save_message(
            st.session_state.session_id,
            "assistant",
            response_text,
            token_usage=total_token_count,
            user_id=st.user.email
        )
        # Recalculate token usage *after* saving assistant message
        cumulative_tokens = get_token_usage(
            st.session_state.session_id,
            campaign_name=st.session_state.campaign_name,
            user_id=st.user.email
        )

        # === 4. Summary and Rollover Logic ===
        trigger_summary = (
            st.session_state.tokens_since_summary >= MAX_TOKENS_BEFORE_SUMMARY
            and st.session_state.tokens_since_rollover < MAX_TOKENS_PER_THREAD
        )

        trigger_rollover = st.session_state.tokens_since_rollover >= MAX_TOKENS_PER_THREAD

        if trigger_summary and not trigger_rollover:
            try:
                with st.spinner("📖 Summarizing session for memory..."):
                    summarize_chat_history_with_gemini(
                        gemini_model=model,
                        user_email=st.user.email,
                        campaign_name=st.session_state.campaign_name,
                        thread_id=st.session_state.session_id
                    )
                    st.session_state.tokens_since_summary = 0
            except Exception as e:
                st.warning(f"Memory summary failed: {e}")
        # Step 2: If rollover, make new thread after summary
        if trigger_rollover:
            st.toast("⚠️ Thread too large! Archiving and starting a new one...", icon="🧠")

            # === 1. Final summary and save
            try:
                summarize_in_background(
                    gemini_model=model,
                    thread_id=st.session_state.session_id,
                    user_email=st.user.email,
                    campaign_name=st.session_state.campaign_name
                )
            except Exception as e:
                st.warning(f"❌ Final summary before rollover failed: {e}")

            # === 2. Create new session name
            campaign_dir = os.path.join("saves", sanitize_email(st.user.email), st.session_state.campaign_name, "sessions")
            os.makedirs(campaign_dir, exist_ok=True)

            existing_sessions = [f for f in os.listdir(campaign_dir) if f.startswith("Session") and f.endswith(".json")]
            session_numbers = []
            for fname in existing_sessions:
                try:
                    parts = fname.split()
                    if parts[0] == "Session":
                        session_numbers.append(int(parts[1]))
                except:
                    continue

            next_session_number = max(session_numbers + [-1]) + 1
            now_str = datetime.now().strftime("%Y-%m-%d %H-%M")
            new_thread_id = f"Session {next_session_number} {now_str}"
            new_path = os.path.join(campaign_dir, f"{new_thread_id}.json")

            # === 3. Merge summary_cache from old and new sessions
            try:
                new_session_id = create_session(st.user.email, st.session_state.campaign_id)
                merge_save_files(
                    old_id=st.session_state.session_id,
                    new_id=new_session_id,
                    user_email=st.user.email,
                    campaign_name=st.session_state.campaign_name
                )
            except Exception as e:
                st.warning(f"⚠️ Merge failed: {e}")

            # === 4. Load save file and convert to priming text
            save_path = get_save_file_path(st.user.email, st.session_state.campaign_name)
            try:
                priming_text = save_file_to_text(save_path)
            except Exception as e:
                priming_text = "(Could not load save file summary.)"
                st.warning(f"⚠️ Failed to parse priming memory: {e}")

            # === 5. Load startup script (narrator intro)
            startup_script_path = os.path.join("prompts", "startup_script.txt")
            if os.path.exists(startup_script_path):
                with open(startup_script_path, "r", encoding="utf-8") as f:
                    startup_script = f.read()
            else:
                startup_script = ""

            system_prompt = f"{startup_script}\n\n{priming_text}".strip()

            # === 6. Create new session JSON file
            new_data = {
                "thread_id": new_thread_id,
                "summary_cache": {},
                "summary_chunks": [],
                "timestamp": datetime.utcnow().isoformat(),
                "last_summarized_token_usage": 0,
                "token_usage": {
                    "prompt_tokens": 0,
                    "completion_tokens": 0,
                    "total_tokens": 0
                },
                "startup_injected": True
            }

            with open(new_path, "w", encoding="utf-8") as f:
                json.dump(new_data, f, indent=2)

            # === 7. Reset app state for new session
            st.session_state.session_id = new_thread_id
            st.session_state.messages = []
            st.session_state.system_prompt = system_prompt
            st.session_state.messages_loaded = False
            st.session_state.is_new_campaign = True
            st.session_state.tokens_since_summary = 0
            st.session_state.tokens_since_rollover = 0

            st.toast(f"✨ New thread started: {new_thread_id[:8]}", icon="🆕")
        st.rerun()

with tab2:
    summary = load_full_save(st.session_state.session_id, user_id=st.user.email)

    if not summary:
        st.info("No campaign data has been generated yet.")
    else:
        st.subheader("🧙 Player Characters")
        for c in summary.get("characters", []):
            st.markdown(f"- **{c.get('name', 'Unnamed')}**: {c.get('occupation', 'Unknown')} ({c.get('race', 'Unknown')})")

        st.subheader("🧑‍🤝‍🧑 Key NPCs")
        for npc in summary.get("key_npcs", []):
            st.markdown(f"- **{npc.get('name', 'Unnamed')}**: {npc.get('role', 'Unknown')} ({npc.get('affiliation', 'None')})")

        st.subheader("📍 Known Locations")
        for loc in summary.get("known_locations", []):
            st.markdown(f"- **{loc.get('name', 'Unnamed')}**: {loc.get('type', 'Place')} in {loc.get('region', 'Unknown')}")

        st.subheader("🏛️ Factions")
        for f in summary.get("factions", []):
            st.markdown(f"- **{f.get('name', 'Unnamed')}** ({f.get('tier', 'N/A')}) - {f.get('alignment', 'Unknown')}")

