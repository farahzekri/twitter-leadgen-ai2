# app/models.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base
from pydantic import BaseModel

# --- SQLAlchemy Models ---
class TweetDB(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True, index=True)
    tweet_id = Column(String, unique=True, index=True)
    author = Column(String)
    content = Column(String)
    engagement_score = Column(Float)
    relevance_score = Column(Float, default=0)  # ajout pour Agent 1
    matched_keywords = Column(String, nullable=True)  # ajout pour mots-clés matchés

class LeadDB(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    twitter_handle = Column(String)
    message_sent = Column(String, nullable=True)   # tweet ou message généré
    response = Column(String, nullable=True)

# --- Pydantic Models ---
class Tweet(BaseModel):
    tweet_id: str
    author: str
    content: str
    engagement_score: float
    relevance_score: float
    matched_keywords: str = None

    class Config:
        orm_mode = True

class Lead(BaseModel):
    name: str = None
    twitter_handle: str = None
    message_sent: str = None
    response: str  | None = None

    class Config:
        orm_mode = True

# Nouveau modèle pour générer les idées de tweets
class GeneratedTweet(BaseModel):
    content: str

    class Config:
        orm_mode = True
