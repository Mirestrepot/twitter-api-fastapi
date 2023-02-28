#Python
import json
from typing import List

from bson import ObjectId
from db.schemas.user import user_schema

from utils.fuction import delete_one_user, find_all_users, find_one_user, search_user

#FastApi

from fastapi import HTTPException, Path, Response, status
from fastapi import APIRouter
router = APIRouter()

#Models
from models.user import UserModel



#Db

from db.database import db_client,db_users

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
    Args:
        id (str): _description_

    Returns:
        id(str): User
    """
    try:
        return find_one_user("_id", ObjectId(id))
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid ID passed") 
    
### Delete a User
@router.delete(
    path="/users/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a User",
    tags=["Users"]
)
async def delete_user(id: str):

    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found") 
        
        


