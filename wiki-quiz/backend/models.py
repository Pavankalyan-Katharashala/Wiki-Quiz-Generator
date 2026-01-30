from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True)
    title = Column(String)
    summary = Column(Text)
    raw_text = Column(Text)

    quizzes = relationship("Quiz", back_populates="article")
    topics = relationship("RelatedTopic", back_populates="article")


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("articles.id"))
    question = Column(Text)
    options = Column(Text)
    answer = Column(String)
    difficulty = Column(String)
    explanation = Column(Text)

    article = relationship("Article", back_populates="quizzes")


class RelatedTopic(Base):
    __tablename__ = "related_topics"

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"))
    topic = Column(String)

    article = relationship("Article", back_populates="topics")
