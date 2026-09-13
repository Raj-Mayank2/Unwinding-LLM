# 📰 AI News Summarizer

A beginner-friendly AI news summarization agent built with **FastAPI, Agno, Groq, and RSS feeds**.

The project fetches recent news, uses an open-weight LLM to generate concise summaries, and displays the results through a simple web UI.

> Part of **Unwinding-LLM** — a growing collection of practical LLM and AI applications built step-by-step from beginner to advanced.

## ✨ Features

- 📰 Fetch recent news through RSS feeds
- 🤖 AI-powered news summarization
- 🧠 Agno-based AI agent
- ⚡ FastAPI REST API
- 🌐 Simple HTML/CSS/JavaScript UI
- 🔗 Links to original articles
- 🆓 Free-tier inference
- 🐍 Lightweight Python backend
- 🔐 API keys stored using environment variables

## 🏗️ Architecture

```text
                    User
                     │
                     ▼
              ┌─────────────┐
              │   Web UI    │
              │ HTML/CSS/JS │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │   FastAPI   │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │ Agno Agent  │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │  News Tool  │
              └──────┬──────┘
                     │
                     ▼
                 RSS Feeds
                     │
                     ▼
                  Articles
                     │
                     ▼
              ┌─────────────┐
              │  Groq LLM   │
              │ GPT-OSS-20B │
              └──────┬──────┘
                     │
                     ▼
                AI Summary
                     │
                     ▼
                    UI
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| FastAPI | REST API |
| Agno | AI agent framework |
| Groq | LLM inference |
| GPT-OSS-20B | Open-weight language model |
| Feedparser | RSS feed parsing |
| HTML/CSS/JavaScript | Frontend |

## 📁 Project Structure

```text
news_summarizer/
│
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── main.py
│   ├── schemas.py
│   └── tools.py
│
├── static/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Unwinding-LLM.git
cd Unwinding-LLM/starter_ai_agents/news_summarizer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Groq

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file.

### 5. Start the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 🌐 Web UI

Open:

```text
http://127.0.0.1:8000/ui
```

Select a category and number of stories, then click **Get News**.

## 📚 API

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

### Get News

```http
POST /news
```

Request:

```json
{
  "category": "technology",
  "limit": 3
}
```

Response:

```json
{
  "category": "technology",
  "articles": [
    {
      "title": "Example technology story",
      "summary": "A concise AI-generated summary of the story.",
      "link": "https://example.com/article"
    }
  ]
}
```

### Interactive API Documentation

```text
http://127.0.0.1:8000/docs
```

## 📰 Supported Categories

The current version supports:

```text
technology
science
world
```

News is retrieved from configured RSS feeds.

## 🔄 How It Works

1. User selects a news category.
2. The frontend sends a request to FastAPI.
3. The news tool retrieves recent RSS articles.
4. The Agno agent processes the articles.
5. Groq runs the open-weight LLM.
6. The model generates concise summaries.
7. FastAPI returns the results as JSON.
8. The frontend displays the summaries as news cards.

## 🎯 Learning Goals

This project is intentionally lightweight and focuses on the fundamentals of building an AI agent:

- FastAPI API development
- LLM integration
- Agno agent basics
- Tool calling
- RSS-based data retrieval
- Prompting
- AI summarization
- AI + backend integration
- Simple frontend integration

## 🔮 Future Improvements

- [ ] Custom news topic search
- [ ] More news sources
- [ ] Better article extraction
- [ ] News deduplication
- [ ] Source filtering
- [ ] Improved structured responses
- [ ] RAG-based news history
- [ ] MCP integration
- [ ] Scheduled news digests
- [ ] Deployment

## ⚠️ Current Limitations

This is a **starter AI agent**, not a production-grade news aggregation system.

- RSS feeds determine which articles are available.
- Some publishers may provide limited article descriptions.
- Some websites may block article extraction.
- News coverage depends on configured RSS sources.
- The project relies on free-tier model/API limits.

## 📌 Project Status

**Status:** 🟢 Working — Starter Version

Built as part of:

**Unwinding-LLM → Starter AI Agents**

---

⭐ More practical LLM, AI agent, RAG, MCP, and GenAI projects will be added to **Unwinding-LLM**.
