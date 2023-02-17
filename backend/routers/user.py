#Python
import json
from typing import List
from uuid import UUID

#FastApi

from fastapi import HTTPException, status
from fastapi import APIRouter


#Models
from models.user import UserModel
from db.database import db_client
from db.schemas.user import user_schema, users_schema
from utils.fuction import search_user

router = APIRouter()


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
    return users_schema(db_client.users.find())
    
    
### Show a User
@router.get(
    path="/users/{user_id}",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
async def show_a_user(user_id: UUID):
    return search_user(user_id)

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



def search_id(user_id):

    database = "users.json"
    data = json.loads(open(database).read())
    try:
        for i in data:
            if i['user_id'] == user_id:
                result = i['user_id']
                return result
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail='User not found')
            