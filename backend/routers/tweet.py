#Python
import datetime
import json
from typing import List
from bson import ObjectId

#FastApi
from fastapi import Body, HTTPException, status
from fastapi import APIRouter
from models.tweet import Tweet
router = APIRouter()
#Models


#DB
from db.database import db_client
from db.schemas.tweet import tweet_schema,tweets_schema
from models.user import UserRegistrer

#utils





##Tweets

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
    def find_all_users():
        try:
            return tweets_schema(db_client.tweets.find())
            
        except:
            raise HTTPException(status_code=404, detail="Users not found")
        
    return find_all_users()

        
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
            # tweet = db_client.tweets.find_one({dict_tweet})
            # if tweet is None:
            #     raise HTTPException(status_code=404, detail="Tweet not found")
            # else:

            id = db_client.tweets.insert_one(dict_tweet).inserted_id
            dict_tweet["created_at"] = datetime.datetime.now()
            new_tweet = tweet_schema(db_client.tweets.find_one({"_id": id}))
            return new_tweet
        except:
            raise HTTPException(status_code=404, detail="Cannot be posted tweet")

    return Tweet(create_tweet(tweet))
    

    
### Show a Tweet
@router.get(
    path="/tweets/{id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
    tags=["Tweet"]
)
async def show_a_tweet(id: str):
    """Show a Tweet
    Args:
        id (str): ObjectID

    Returns:
        dict: Tweet schema
    """
    def find_one_user(field: str,key):
        try:    
            tweet =  db_client.tweets.find_one({field: key})
            return Tweet(**tweet_schema(tweet))
        except:
            raise HTTPException(status_code=404, detail="User not found") 
    try:
        return find_one_user("_id", ObjectId(id))
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid ID passed") 



### Delete a Tweet
@router.delete(
    path="/tweets/{id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweet"]
)
async def delete_a_tweet(id: str):
    found_response = db_client.tweets.find_one_and_delete({"_id": ObjectId(id)})

    if not found_response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found") 
### Update a Tweet
@router.put(
    path="/tweets/{id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=["Tweet"]
)
async def update_a_tweet(id: str):
    pass