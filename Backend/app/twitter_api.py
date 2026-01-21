import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
USE_MOCK = os.getenv("USE_MOCK", "True").lower() == "true"

# Création du client Tweepy
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Exemple de tweets mock
MOCK_TWEETS = [
    {
        "tweet_id": "111",
        "author": "mock_user",
        "content": "Manual infrastructure management is slowing our DevOps team",
        "engagement_score": 120
    },
    {
        "tweet_id": "222",
        "author": "mock_user",
        "content": "Scaling deployments without automation is painful",
        "engagement_score": 85
    },
    {
        "tweet_id": "333",
        "author": "mock_user",
        "content": "We just migrated our marketing website",
        "engagement_score": 30
    }
]

def fetch_tweets_from_user(username: str, count: int = 5):
    if USE_MOCK:
        print("Running in MOCK mode")
        return MOCK_TWEETS

    # Mode réel avec Twitter API
    try:
        user = client.get_user(username=username)
        if not user.data:
            return []

        tweets = client.get_users_tweets(
            user.data.id,
            max_results=count,
            tweet_fields=["public_metrics"]
        )

        results = []
        if tweets.data:
            for t in tweets.data:
                metrics = t.public_metrics
                engagement = metrics.get("like_count", 0) + metrics.get("retweet_count", 0)
                results.append({
                    "tweet_id": str(t.id),
                    "author": username,
                    "content": t.text,
                    "engagement_score": engagement
                })
        return results

    except Exception as e:
        print("Twitter API Error:", e)
        return []
