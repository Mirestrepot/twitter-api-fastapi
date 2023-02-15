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
@app.get(
    path='/',
    status_code=200)
async def home():
    return {"Home: Twitter Page"}
##Users
@app.post(
    path="/signup",
    response_model=UserModel,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup():
    pass

@app.post(
    path="/login",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def Login():
    pass

@app.get(
    path="/Users",
    response_model=List[UserModel],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["users"]
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass
