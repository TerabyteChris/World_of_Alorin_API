import os
import json
import datetime
from google.generativeai import GenerativeModel, configure
import streamlit as st
import uuid
from storage import load_history, save_message, get_all_thread_ids, load_full_save, get_user_session_path, load_summary_cache
from token_tracker import add_token_usage, get_token_usage
from gemini_utils import get_total_tokens, summarize_chat_history_with_gemini
from campaign_utils import (
    list_campaigns, create_campaign,
    list_sessions, create_session,
    readable_session_names, extract_session_id
)
from prompt_loader import load_prompt

MAX_TOKENS_BEFORE_SUMMARY = 200000
MAX_TOKENS_PER_THREAD = 800000

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
cumulative_tokens = get_total_tokens(st.session_state.session_id)
# === Sidebar ===
with st.sidebar:
    # --- Auth Info ---
    st.markdown(f"👤 **{st.user.name}**")
    st.markdown(f"📧 {st.user.email}")

    # --- Campaigns ---
    campaigns = list_campaigns(st.user.email)
    campaign_names = [c["name"] for c in campaigns]
    selected_campaign_name = st.selectbox("🎲 Select Campaign", campaign_names)

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
    for c in campaigns:
        if c["name"] == selected_campaign_name:
            st.session_state.campaign_id = c["id"]
            break

    # --- Sessions ---
    if st.session_state.get("campaign_id"):
        sessions = list_sessions(st.user.email, st.session_state.campaign_id)
        session_options = readable_session_names(sessions)
        selected_session = st.selectbox("📘 Select Session", session_options)

        if st.button("➕ New Session"):
            new_session_id = create_session(st.user.email, st.session_state.campaign_id)
            st.session_state.session_id = new_session_id
            st.rerun()

        # Save selected session_id
        st.session_state.session_id = extract_session_id(selected_session)
        st.session_state.campaign_name = selected_campaign_name

    # --- Token Usage ---
    if st.session_state.get("session_id"):
        cumulative_tokens = get_token_usage(
            st.session_state.session_id,
            campaign_name=st.session_state.campaign_name,
            user_id=st.user.email
        )
        st.markdown(f"**🧠 Tokens Used:** {cumulative_tokens['total']:,}")
        st.progress(min(cumulative_tokens['total'] / 800000, 1.0))

    # --- Logout ---
    st.markdown("---")
    if st.button("🚪 Log Out"):
        st.logout()


with tab1:
    if not st.session_state.get("campaign_id") or not st.session_state.get("session_id"):
        st.info("Please select a campaign and session to begin.")
        st.stop()
    with st.container(height=600):
        # === 1. Render Chat History First ===
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # === 2. Chat Input Box LAST so it stays at bottom ===
    prompt = st.chat_input("Speak your will, adventurer...")

    # === 3. Handle Submission ===
    if prompt:
        formatted_history = [
            {
                "role": "model" if m["role"] == "assistant" else m["role"],
                "parts": [{"text": m["content"]}]
            }
            for m in st.session_state.messages
        ]

        if st.session_state.get("is_new_campaign"):
            prompt_header = load_prompt("new_campaign_prompt")
        elif summary_cache := load_summary_cache(st.session_state.session_id, user_id=st.user.email):
            prompt_header = load_prompt("continuation_prompt")
        else:
            prompt_header = load_prompt("startup_script")

        system_prompt = load_prompt("static_instructions") + "\n\n" + prompt_header

        # === 3. Create the chat object ===
        formatted_history.insert(0, {
            "role": "user",
            "parts": [{"text": system_prompt}]
        })

        chat = model.start_chat(history=formatted_history)


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


            st.session_state.total_tokens += total_token_count

        # Save messages (assistant includes token usage)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        save_message(
            st.session_state.session_id,
            "assistant",
            response_text,
            token_usage=total_token_count,
            user_id=st.user.email
        )

        # First: Trigger summary if threshold hit
        if cumulative_tokens.get("total", 0) >= MAX_TOKENS_BEFORE_SUMMARY and not st.session_state.get("has_summarized"):
            st.session_state.has_summarized = True  # prevent double triggering
            with st.spinner("📖 Summarizing this session..."):
                try:
                    summary_text = summarize_chat_history_with_gemini(model, st.session_state.session_id)

                    save_path = get_user_session_path(st.session_state.session_id, st.user.email)
                    if os.path.exists(save_path):
                        with open(save_path, "r", encoding="utf-8") as f:
                            save_data = json.load(f)
                        save_data.setdefault("summary_chunks", []).append(summary_text)
                        save_data["last_summarized_token_usage"] = cumulative_tokens
                        with open(save_path, "w", encoding="utf-8") as f:
                            json.dump(save_data, f, indent=2)
                except Exception as e:
                    st.warning(f"Summary failed: {e}")

        # Then: Create new thread if max tokens reached
        if cumulative_tokens.get("total", 0) >= MAX_TOKENS_PER_THREAD:
            st.toast("⚠️ Thread too large! Archiving and starting a new one...", icon="🧠")

            old_path = get_user_session_path(st.session_state.session_id, st.user.email)
            if os.path.exists(old_path):
                with open(old_path, "r", encoding="utf-8") as f:
                    old_data = json.load(f)
            else:
                old_data = {}

            new_thread_id = str(uuid.uuid4())
            new_path = get_user_session_path(new_thread_id, st.user.email)

            new_data = {
                "thread_id": new_thread_id,
                "summary_cache": old_data.get("summary_cache", {}),
                "summary_chunks": old_data.get("summary_chunks", []),
                "timestamp": datetime.utcnow().isoformat(),
                "last_summarized_token_usage": 0,
                "token_usage": 0,
                "startup_injected": True
            }

            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            with open(new_path, "w", encoding="utf-8") as f:
                json.dump(new_data, f, indent=2)

            st.session_state.session_id = new_thread_id
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

