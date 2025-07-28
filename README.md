# World of Alorin – Narrated Dungeon Master API

A full-stack AI-powered interactive storytelling engine for solo Dungeons & Dragons 5e campaigns. This project provides immersive, memory-rich narration through a virtual Dungeon Master ("Lorekeeper") that remembers decisions, NPCs, quests, and campaign states across sessions.

## Features

- **Narrative AI Engine**: Uses Gemini Pro and OpenAI models for dynamic, immersive storytelling.
- **Persistent World State**: Automatically tracks characters, quests, locations, and factions.
- **Save File Merging & Summarization**: Combines session data into narrative memories.
- **Web Interface**: Frontend chat UI with editable character sheets and session recaps.
- **Token Tracking**: Integrated usage statistics per thread to manage model interactions.
- **Secure API**: FastAPI backend with CORS, API key validation, and rate limiting.

---

## Project Structure
.
├── _index.html # Web UI frontend
├── _script.js # Frontend JS controller (session logic, rendering, TTS)
├── _main.py # FastAPI backend server (core API logic, summary + chat)
├── storage.py # Filesystem persistence for chat history and tokens
├── token_tracker.py # Thread-based token accounting
├── save_file_models.py # Pydantic models for characters, NPCs, quests, etc.
├── merge_save_files.py # Merges historical save data across sessions
├── thread_registry.py # Maps session names to persistent thread IDs

## 🧑‍💻 Technologies Used

- **Frontend**: Vanilla JS, HTML, CSS
- **Backend**: Python, FastAPI, SlowAPI (rate limiting), Pydantic
- **AI**: Google Generative AI (`gemini-pro`), OpenAI API
- **Persistence**: JSON save files per session
- **Hosting Consideration**: CORS-enabled for deployment under `alorinworld.com`

---

## 🛡️ Security Notes

- Do **not** expose your OpenAI or Gemini API keys in the frontend.
- API requests require a valid `x-api-key` header to interact with chat endpoints.

---

## 🔧 Running Locally

### Prerequisites

- Python 3.10+
- Node.js (optional, for frontend enhancements)

### Installation

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt


## 🔧 Environment Setup

Create a .env file with:

OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_gemini_key
OPENAI_ASSISTANT_ID=your_assistant_id


### Run the Backend
uvicorn _main:app --reload
