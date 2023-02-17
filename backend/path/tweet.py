#Python
import json
from typing import List

#FastApi

from fastapi import Body, status
from fastapi import APIRouter
from models.tweet import Tweet

#Models



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
async def post(tweet: Tweet = Body(...)):
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
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dic = tweet.dict()
        tweet_dic["tweet_id"] = str(tweet_dic["tweet_id"])
        tweet_dic["created_at"] = str(tweet_dic["created_at"])
        tweet_dic["updated_at"] = str(tweet_dic["updated_at"])
        tweet_dic["by"]["user_id"] = str(tweet_dic["by"]["user_id"])
        tweet_dic["by"]["birth_date"] = str(tweet_dic["by"]["birth_date"])
        results.append(tweet_dic)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet
    
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
