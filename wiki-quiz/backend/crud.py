from sqlalchemy.orm import Session
from .models import Article, Quiz, RelatedTopic

def get_article_by_url(db: Session, url: str):
    return db.query(Article).filter(Article.url == url).first()

def get_article_by_id(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()

def save_article(db: Session, url: str, data, quiz, topics):
    # 🔹 Check if article already exists
    existing = get_article_by_url(db, url)
    if existing:
        return existing

    article = Article(
        url=url,
        title=data["title"],
        summary=data["summary"],
        raw_text=data["text"]
    )
    db.add(article)
    db.commit()
    db.refresh(article)

    for q in quiz:
        db.add(Quiz(
            article_id=article.id,
            question=q["question"],
            options="|".join(q["options"]),
            answer=q["answer"],
            difficulty=q["difficulty"],
            explanation=q["explanation"]
        ))

    for t in topics:
        db.add(RelatedTopic(article_id=article.id, topic=t))

    db.commit()
    return article
