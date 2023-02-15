#Python
from datetime import datetime,date
from typing import Optional, List
from uuid import UUID

#Pydantic
from pydantic import BaseModel, EmailStr,Field

#FastApi

from fastapi import FastAPI,status
app = FastAPI()


#Models
class UserBaseModel(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLoginModel(UserBaseModel):
    password: str = Field(
        ...,
        min_length=8,
        max_length=60)
    
class UserModel(UserBaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=20
        )
    birth_day: Optional[date] = Field(default=None)
  
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
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
async def signup():
    pass
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
    path="/Users",
    response_model=List[UserModel],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
async def show_all_users():
    pass
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
    return {"Home: Twitter Page"}
### Post a Tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweet"]
)
async def Post():
    pass
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
