#Python
import json
from typing import List

#FastApi

from fastapi import Body, HTTPException, status
from fastapi import APIRouter
from models.tweet import Tweet

#Models

#DB
from db.database import db_client
from db.schemas.tweet import tweet_schema,tweets_schema
from models.user import UserRegistrer


router = APIRouter()



##Teweets

### Show all Tweets
@router.get(
    path='/',
    response_model=List[Tweet],
    status_code=200,
    summary="Show all Tweets",
    tags=["Tweet"]
    )
async def home():
    """Show_all_Tweets
    Parameters: 
    
    Return: All tweets 
        -tweet_id: UUID
        -content: str
        -created_at: datetime
        -update_at: Optional[datetime]
        -by: UserModel
    """
    with open("tweets.json", "r", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results
### Post a Tweet
@router.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweet"]
)
async def post(
    tweet: Tweet = Body(...)):
    """Post a tweet
    Parameters:
    -
    Returns a json with the basic tweet information:
    -tweet_id: UUID
    -content: str
    -created_at: datetime
    -update_at: Optional[datetime]
    -by: UserModel
    """
    def create_tweet(tweet):
        try:
            dict_tweet = dict(tweet)
            user = UserRegistrer(dict_tweet["by"])
            user = db_client.users.find_one({user})
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            else:
                
                id = db_client.tweets.insert_one(dict(tweet)).inserted_id
                new_tweet = tweet_schema(db_client.tweets.find_one({"_id": id}))
            return new_tweet
        except:
            raise HTTPException(status_code=404, detail="Cannot create user")

    return create_tweet(tweet)
    

    
### Show a Tweet
@router.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
    tags=["Tweet"]
)
async def show_a_tweet():
    pass



### Delete a Tweet
@router.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweet"]
)
async def delete_a_tweet():
    pass
### Update a Tweet
@router.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=["Tweet"]
)
async def update_a_tweet():
    pass
