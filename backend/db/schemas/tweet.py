from db.schemas.user import user_schema

def tweet_schema(tweet) -> dict:

    return {
        "id": str(tweet["_id"]),
        "content": tweet["content"],
        "updated_at": tweet["updated_at"],
        "created_at": tweet["created_at"],
        "by": tweet["by"],
        "user_id": tweet["user_id"],
    }
    
def tweets_schema(tweets) -> list:
    return [tweet_schema(tweet) for tweet in tweets]