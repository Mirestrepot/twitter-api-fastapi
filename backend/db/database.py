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

