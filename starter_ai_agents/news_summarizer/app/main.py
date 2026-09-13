from fastapi import FastAPI
from pydantic import BaseModel
from app.tools import get_news
from app.agent import news_agent
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(
    title="News Summarizer Agent",
    description="AI agent that fetches and summarizes news",
    version="1.0.0",
)
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

class SummarizeRequest(BaseModel):
    text: str


class NewsRequest(BaseModel):
    category: str = "technology"
    limit: int = 3


@app.get("/")
def root():
    return {
        "message": "News Summarizer Agent is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/summarize")
def summarize(request: SummarizeRequest):

    response = news_agent.run(
        f"""
        Summarize the following news article:

        {request.text}
        """
    )

    return {
        "summary": response.content
    }


@app.post("/news")
def news(request: NewsRequest):

    articles = get_news(
        category=request.category,
        limit=request.limit
    )

    results = []

    for article in articles:

        response = news_agent.run(
            f"""
            Summarize this news article in 2-3 sentences.

            Title:
            {article["title"]}

            Content:
            {article["content"]}

            Do not invent information.
            """
        )

        results.append({
            "title": article["title"],
            "summary": response.content,
            "link": article["link"]
        })

    return {
        "category": request.category,
        "articles": results
    }

@app.get("/ui")
def ui():
    return FileResponse("static/index.html")