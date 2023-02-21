


#MongoDB driver
from fastapi import HTTPException
from pymongo import MongoClient
from db.schemas.user import user_schema
from models.user import UserModel

MONGO_URI = 'mongodb://localhost'



client = MongoClient(MONGO_URI)


db_client = client["twitterAPI"]
db_users = db_client["users"]

def find_one_user(field: str,key):
    
    try:
        user =  db_client.users.find_one({field: key})
        return UserModel(**user_schema(user))
    except:
        raise HTTPException(status_code=404, detail="User not found") 
