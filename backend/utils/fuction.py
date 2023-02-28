from bson import ObjectId
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
        raise HTTPException(status_code=404, detail="User not found1") 

def find_all_users():
    try:
        return users_schema(db_client.users.find())
    except:
        raise HTTPException(status_code=404, detail="Users not found2")
    
def delete_one_user(field: str,key):
    pass
       
        
    
    
def create_user(user):
    try:
        user_dict = dict(user)
        del user_dict["id"]
        id = db_client.users.insert_one(user_dict).inserted_id
        new_user = user_schema(db_client.users.find_one({"_id": id}))
        return new_user
    except:
        raise HTTPException(status_code=404, detail="Cannot create user")
    



        # if user_response != key:
        #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
        #                     detail='You are not allowed to perform this action')
        

def user_on(id: str) -> UserModel:
    user = find_one_user("_id", ObjectId(id))  
    return user