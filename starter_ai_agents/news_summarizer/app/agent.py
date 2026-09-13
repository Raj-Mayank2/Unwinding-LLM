from dotenv import load_dotenv

load_dotenv()

from agno.agent import Agent
from agno.models.groq import Groq

from app.tools import get_news


news_agent = Agent(
    model=Groq(id="openai/gpt-oss-20b"),

    tools=[
        get_news
    ],

    instructions=[
        "You are a news summarization assistant.",
        "Use get_news whenever the user asks for current news.",
        "Summarize the retrieved articles using only the information provided.",
        "Do not invent facts.",
        "Keep summaries concise."
    ],

    markdown=True,
)