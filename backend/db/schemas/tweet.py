from db.schemas.user import user_schema


def tweet_schema(tweet) -> dict:
    user = tweet["by"]
    return {
        "id": str(tweet["_id"]),
        "created_at": tweet["created_at"],
        "content": tweet["content"],
        "updated_at": tweet["updated_at"],
        "by": user_schema(user)
    }
    
def tweets_schema(tweet) -> list:
    return [tweet_schema(tweet) for tweet in tweet]