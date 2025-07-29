import streamlit as st

st.set_page_config(page_title="World of Alorin – Narrated Dungeon Master", layout="wide")

# Inject custom CSS (adapted from your HTML)
st.markdown("""
    <style>
        html, body {
            background-color: #0b0c10;
            color: #c5c6c7;
            font-family: 'Georgia', serif;
        }
        .stTextArea textarea {
            background-color: #1c1c1c !important;
            color: white !important;
        }
        .chat-bubble {
            padding: 1rem;
            border-radius: 6px;
            margin-bottom: 1rem;
            box-shadow: 0 1px 4px rgba(0,0,0,0.3);
        }
        .user {
            background-color: #e0ecff;
            color: #1a1a1a;
            border-left: 5px solid #4a90e2;
        }
        .assistant {
            background: linear-gradient(to left, #1a1a1a, #2e2e2e);
            color: #f1f1f1;
            font-style: italic;
            border-left: 5px solid #66fcf1;
        }
        .token-bar {
            background-color: #222;
            border: 1px solid #444;
            border-radius: 5px;
            height: 20px;
            max-width: 400px;
            margin-bottom: 0.5rem;
        }
        .token-fill {
            height: 100%;
            background-color: #66fcf1;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 World of Alorin – Narrated Dungeon Master")

# Sidebar Controls
with st.sidebar:
    st.header("Controls")

    model = st.selectbox("Choose a model:", [
        "gemini"
    ], index=0)

    tts = st.selectbox("TTS Engine", [
        "Browser TTS (Free)",
        "Google Cloud TTS",
        "OpenAI TTS"
    ])

    narrate = st.checkbox("Speak responses aloud")

    st.markdown("### Memory Usage")
    usage = 45  # Placeholder
    st.markdown(f"""
        <div class="token-bar">
            <div class="token-fill" style="width: {usage}%;"></div>
        </div>
        <span>{usage}%</span>
    """, unsafe_allow_html=True)

    st.markdown(f"**Token Usage:** 120 prompt + 80 completion = 200 total")
    st.markdown(f"**Session Total:** 235 tokens")


# Tabs
tab = st.radio("Select View", ["💬 Chat", "📘 Campaign Notes"], horizontal=True)

# --- Chat Interface
if tab == "💬 Chat":
    st.subheader("Chat with your Dungeon Master")

    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []

    for role, msg in st.session_state.chat_log:
        css_class = "user" if role == "user" else "assistant"
        st.markdown(f'<div class="chat-bubble {css_class}">{msg}</div>', unsafe_allow_html=True)

    user_input = st.text_area("Speak your will, adventurer...", height=150)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🎮 Start Campaign"):
            st.session_state.chat_log.append(("assistant", "Welcome, adventurer! Your journey begins now."))
    with col2:
        if st.button("🔄 Reset Session"):
            st.session_state.chat_log = []
    with col3:
        if st.button("🎙️ Speak"):
            st.session_state.chat_log.append(("user", user_input))
            st.session_state.chat_log.append(("assistant", f"Echo: {user_input}"))

# --- Campaign Notes Tab
elif tab == "📘 Campaign Notes":
    st.subheader("Current Save File")
    st.markdown("_(This will show structured campaign notes here.)_")

