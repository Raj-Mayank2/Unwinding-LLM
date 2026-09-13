from pydantic import BaseModel
from typing import List


class NewsArticle(BaseModel):
    title: str
    summary: str
    link: str


class NewsResponse(BaseModel):
    category: str
    articles: List[NewsArticle]