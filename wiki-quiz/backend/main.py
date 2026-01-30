from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models
from .scraper import scrape_wikipedia
#from .llm import generate_quiz_and_topics
from .crud import save_article
from .crud import get_article_by_id
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate-quiz")
def generate_quiz(url: str, db: Session = Depends(get_db)):
    from .import llm

    # Check cache first
    article = db.query(models.Article).filter(models.Article.url == url).first()

    if False and article:
        quiz = [
            {
                "question": q.question,
                "options": q.options.split("|"),
                "answer": q.answer,
                "difficulty": q.difficulty,
                "explanation": q.explanation
            }
            for q in article.quizzes
        ]

        topics = [t.topic for t in article.topics]

        return {
            "id": article.id,
            "title": article.title,
            "summary": article.summary,
            "quiz": quiz,
            "related_topics": topics
        }

    # Else generate fresh
    scraped = scrape_wikipedia(url)
    quiz, topics = llm.generate_quiz_and_topics(scraped["text"])
    article = save_article(db, url, scraped, quiz, topics)

    return {
        "id": article.id,
        "title": article.title,
        "summary": article.summary,
        "quiz": quiz,
        "related_topics": topics
    }

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    articles = db.query(models.Article).all()

    return [
        {
            "id": article.id,
            "title": article.title,
            "url": article.url
        }
        for article in articles
    ]

@app.get("/quiz/{article_id}")
def get_quiz_details(article_id: int, db: Session = Depends(get_db)):
    article = get_article_by_id(db, article_id)

    if not article:
        return {"error": "Article not found"}

    quiz = [
        {
            "question": q.question,
            "options": q.options.split("|"),
            "answer": q.answer,
            "difficulty": q.difficulty,
            "explanation": q.explanation
        }
        for q in article.quizzes
    ]

    related_topics = [t.topic for t in article.topics]

    return {
        "id": article.id,
        "title": article.title,
        "summary": article.summary,
        "quiz": quiz,
        "related_topics": related_topics
    }

@app.get("/")
def root():
    return {"message": "Wiki Quiz API running"}
