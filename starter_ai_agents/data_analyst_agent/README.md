# 📊 Data Analysis Agent

A beginner-friendly AI data analysis agent that allows users to upload a CSV file and get useful insights about the dataset using an LLM.

The application combines **Pandas** for reliable data processing with **Agno + Groq** for natural-language analysis and explanations.

> Part of **Unwinding-LLM → Starter AI Agents**

---

## ✨ Features

- 📂 Upload CSV datasets
- 👀 Preview the uploaded data
- 📏 View dataset dimensions
- 🔢 View numerical statistics
- ❌ Detect missing values
- 🤖 Generate AI-powered dataset analysis
- 💡 Get key insights and recommendations
- 🌐 Simple Streamlit interface

---

## 🏗️ How It Works

```text
              CSV File
                  │
                  ▼
          ┌──────────────┐
          │   Streamlit  │
          │      UI      │
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │    Pandas    │
          │ Data Analysis│
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │  Agno Agent  │
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │  Groq LLM    │
          │ GPT-OSS-20B  │
          └──────┬───────┘
                 │
                 ▼
        ┌──────────────────┐
        │ AI Analysis      │
        │                  │
        │ • Overview       │
        │ • Insights       │
        │ • Data Quality   │
        │ • Recommendations│
        └──────────────────┘