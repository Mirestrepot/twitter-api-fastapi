#Python
import json
from typing import List

from bson import ObjectId

from utils.fuction import search_user

#FastApi

from fastapi import HTTPException, status
from fastapi import APIRouter
router = APIRouter()

#Models
from models.user import UserModel



#Db

from db.database import db_client, find_all_users, find_one_user

##Users


### Show all the Users
@router.get(
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
    return find_all_users()

    
### Show a User
@router.get(
    path="/users/{id}",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
async def show_a_user(id: str):
    """_summary_
    63f3fce703f32c899751d86a
    Args:
        id (str): _description_

    Returns:
        id(str): User
    """
    try:
        return find_one_user("_id", ObjectId(id))
    except:
        raise HTTPException(status_code=404, detail="User not found") 
    
### Delete a User
@router.delete(
    path="/users/{user_id}/delete",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
async def delete_a_user():
    pass


