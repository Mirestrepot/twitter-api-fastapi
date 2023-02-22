from fastapi import HTTPException,status


from db.database import db_client,db_users
from db.schemas.user import user_schema, users_schema

from models.user import LoginUser, UserModel, UserRegistrer


def search_user(username: str):
    if username in db_client.users:
        return UserRegistrer(**db_users[username])
    
    # try:
    #     user =  db_client.users.find_one({username: str})
    #     return UserModel(**user_schema(user))
    # except:
    #     raise HTTPException(status_code=404, detail="User not found") 
    
def find_one_user(field: str,key):
    try:
        user =  db_client.users.find_one({field: key})
        return UserModel(**user_schema(user))
    except:
        raise HTTPException(status_code=404, detail="User not found") 

def find_all_users():
    try:
        return users_schema(db_client.users.find())
    except:
        raise HTTPException(status_code=404, detail="Users not found")
    
def delete_one_user(field: str,key):
    try:
        user_response =  db_client.users.find_one({field: key})
        if user_response is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail='User not found')
        if user_response != field:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='You are not allowed to perform this action')
        #Delete user
        user_response =  db_client.users.delete_one_user({field: key})
    except:
        raise HTTPException(status_code=404, detail="Invalid ID")  
    
       
        
    
    
def create_user(id):
    try:
        new_user = user_schema(db_client.users.find_one({"_id": id}))
        

    except:
        raise HTTPException(status_code=404, detail="Cannot create user")
    
