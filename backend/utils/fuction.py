from fastapi import HTTPException
from db.database import find_one_user,db_client,db_users
from db.schemas.user import user_schema, users_schema

from models.user import UserModel

def search_user(field: str, key):

    try:
        user =  db_client.users.find_one({field: key})
        return UserModel(**user_schema(user))
    except:
        raise HTTPException(status_code=404, detail="User not found") 
