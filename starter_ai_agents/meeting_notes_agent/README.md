# 📝 Meeting Notes Agent

A beginner-friendly AI agent that converts meeting transcripts into clear, structured meeting notes.

> Part of **Unwinding-LLM → Starter AI Agents**

## ✨ Features

- 📝 Meeting transcript analysis
- 📌 Concise meeting summary
- 💬 Key discussion points
- ✅ Key decisions
- 📋 Action items
- 👤 Responsible people
- 📅 Deadlines when mentioned
- 🌐 Simple Streamlit interface

## 🏗️ How It Works

```text
Meeting Transcript
        ↓
   Streamlit UI
        ↓
    Agno Agent
        ↓
     Groq LLM
        ↓
   Structured Notes
```

The user pastes a meeting transcript into the application. The Agno agent sends it to the Groq-hosted LLM, which analyzes the conversation and generates structured meeting notes.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web interface |
| Agno | AI agent framework |
| Groq | LLM inference |
| GPT-OSS-20B | Language model |
| python-dotenv | Environment variables |

## 📁 Project Structure

```text
meeting_notes_agent/
│
├── meeting_notes_agent.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your Groq API key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file to GitHub.

### 3. Run the application

```bash
streamlit run meeting_notes_agent.py
```

The application will open in your browser.

## 📌 Output

The agent generates four main sections:

- **Meeting Summary** — Short overview of the meeting
- **Key Discussion Points** — Important topics discussed
- **Key Decisions** — Decisions made during the meeting
- **Action Items** — Tasks, responsible people, and deadlines

## 🎯 Learning Goals

This project demonstrates:

- LLM prompting
- AI agents with Agno
- Groq model integration
- Text analysis
- Streamlit applications
- Environment variable management

## 🔮 Future Improvements

- Upload `.txt` or `.md` transcripts
- Audio-to-text meeting transcription
- Speaker identification
- Export notes as PDF
- Automatic meeting title and date extraction
- Calendar integration

## 📌 Project Status

**Status:** 🟢 Working — Starter Version

Built as part of **Unwinding-LLM**, a collection of practical LLM and AI applications built step-by-step from beginner to advanced.
