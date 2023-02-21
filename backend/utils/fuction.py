from fastapi import HTTPException
from db.database import db_client,db_users
from db.schemas.user import user_schema

from models.user import LoginUser, UserModel, UserRegistrer

def search_user(username: str):
    if username in db_client.users:
        return UserRegistrer(**db_users[username])
    
    # try:
    #     user =  db_client.users.find_one({username: str})
    #     return UserModel(**user_schema(user))
    # except:
    #     raise HTTPException(status_code=404, detail="User not found") 
    
