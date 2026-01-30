from pydantic import BaseModel
from typing import List

class QuizSchema(BaseModel):
    question: str
    options: List[str]
    answer: str
    difficulty: str
    explanation: str

class ArticleResponse(BaseModel):
    id: int
    url: str
    title: str
    summary: str
    quiz: List[QuizSchema]
    related_topics: List[str]
