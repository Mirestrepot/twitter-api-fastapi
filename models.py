#Python
from datetime import datetime,date
import json
from typing import Optional, List
from uuid import UUID

#Pydantic
from pydantic import BaseModel, EmailStr,Field

#FastApi

from fastapi import Body, FastAPI,status
app = FastAPI()


#Models
class UserBaseModel(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
class PasswordModel(BaseModel):
        password: str = Field(
        ...,
        min_length=8,
        max_length=60)
class UserLoginModel(UserBaseModel,PasswordModel):
    pass
class UserModel(UserBaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)
    
class UserRegistrer(UserModel,PasswordModel):  
    
    pass
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: UserModel = Field(...)
    


#Path parameters

##Users

### Register a User
@app.post(
    path="/signup",
    response_model=UserModel,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
async def signup(
    user: UserRegistrer = Body(...)):
    """Signup register
    description:Register a User
    parameters: Request body parameters= User
    returns: Response Json with the basic information
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        json.dump(results, f)
        user_dic = user.dict()
        user_dic["user_id"] = str(user_dic["user_id"])
        user_dic["birth_date"] = str(user_dic["birth_date"])
        results.append(user_dic)
        f.seek(0)
        f.write(json.dumps(results))
        return user
### Login a User
@app.post(
    path="/login",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
async def Login():
    pass
### Show all the Users
@app.get(
    path="/users",
    response_model=List[UserModel],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
async def show_all_users():
    """Show_all_Users
    Parameters: 
    
    Return: All Users 
        -user_ID: UUID
        -email: EmailStr
        -first_name: Str
        -last_name: Str
        -birth_date: datetime
    """
    with open("users.json", "r", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results
### Show a User
@app.get(
    path="/users/{user_id}",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
async def show_a_user():
    pass
### Delete a User
@app.delete(
    path="/users/{user_id}/delete",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
async def delete_a_user():
    pass


##Teweets

### Show all Tweets
@app.get(
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
@app.post(
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
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
    tags=["Tweet"]
)
async def show_a_tweet():
    pass
### Delete a Tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweet"]
)
async def delete_a_tweet():
    pass
### Update a Tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=["Tweet"]
)
async def update_a_tweet():
    pass
