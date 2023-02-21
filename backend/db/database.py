import ssl
import certifi

#MongoDB driver
from fastapi import HTTPException
from pymongo import MongoClient
from db.schemas.user import user_schema, users_schema
from models.user import UserModel


client = MongoClient(
    "mongodb+srv://mirestrepot:JCaCLq8ENMyCRIZJ@twitterapi.tixzlnu.mongodb.net/?retryWrites=true&w=majority",
     tlsCAFile=certifi.where())


db_client = client["twitterAPI"]
db_users = db_client["users"]

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
    
    
    
    
def create_user(id):
    try:
        new_user = user_schema(db_client.users.find_one({"_id": id}))
        pass

    except:
        raise HTTPException(status_code=404, detail="Cannot create user")