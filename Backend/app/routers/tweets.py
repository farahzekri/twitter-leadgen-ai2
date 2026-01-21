from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import TweetDB
from ..twitter_api import fetch_tweets_from_user
from ..relevance import compute_relevance

router = APIRouter(prefix="/tweets", tags=["Agent 1"])

RELEVANCE_THRESHOLD = 40

@router.post("/monitor/")
def monitor_account(username: str, db: Session = Depends(get_db)):
    raw_tweets = fetch_tweets_from_user(username)

    qualified = []

    for t in raw_tweets:
        relevance_score, matched = compute_relevance(t["content"])
        if relevance_score >= RELEVANCE_THRESHOLD:
            tweet_db = TweetDB(
                tweet_id=t["tweet_id"],
                author=t["author"],
                content=t["content"],
                engagement_score=t["engagement_score"],
                relevance_score=relevance_score,
                matched_keywords=",".join(matched)
            )
            db.add(tweet_db)
            qualified.append(tweet_db)

    db.commit()

    return {
        "qualified_tweets": len(qualified),
        "tweets": [
            {
                "author": t.author,
                "content": t.content,
                "relevance_score": t.relevance_score,
                "engagement_score": t.engagement_score
            } for t in qualified
        ]
    }
