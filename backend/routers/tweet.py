#Python
import datetime
import json
from typing import List
from bson import ObjectId

#FastApi
from fastapi import Body, HTTPException, status
from fastapi import APIRouter
from db.schemas.user import user_schema

router = APIRouter()
#Models
from models.user import UserBaseModel, UserModel, UserRegistrer
from models.tweet import BaseTweet, Tweet
#DB
from db.database import db_client
from db.schemas.tweet import tweet_schema,tweets_schema


#utils
from utils.fuction import find_one_user, user_on




##Tweets

### Show all Tweets
@router.get(
    path='/home',
    response_model= List[Tweet],
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

    try:
        return tweets_schema(db_client.tweets.find())
        
    except:
        pass
        # raise HTTPException(status_code=404, detail="Users not found")
    


        
### Post a Tweet
@router.post(
    path="/post",
    response_model= Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweet"]
)
async def post(
    tweet: BaseTweet = Body(...)):
    """Post a tweet
    Parameters:
    -
    Returns a json with the basic tweet information:
    -id: ObjectId
    -content: str
    -created_at: datetime
    -update_at: Optional[datetime]
    -by: ObjectId the user that created the tweet
    """
    dict_tweet = dict(tweet)
    try:
        current_user = user_on(dict_tweet["user_id"])
        dict_tweet["by"] = current_user.username
        dict_tweet["created_at"] = datetime.datetime.now()
        dict_tweet["updated_at"] = None
        dict_tweet["user_id"] = current_user.id
        id = db_client.tweets.insert_one(dict_tweet).inserted_id
        new_tweet = tweet_schema(db_client.tweets.find_one({"_id": id}))
    except:
        pass
        # raise HTTPException(status_code=404, detail="Tweet not found")
    return (Tweet(**new_tweet))
    

    
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
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweet"]
)
async def delete_a_tweet(id: str):
    try:
        db_client.tweets.find_one_and_delete({"_id": ObjectId(id)})
    except: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Id is deleted successfully")

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