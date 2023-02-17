#Python

import json


#FastApi

from fastapi import Body,status
from fastapi import APIRouter
from db.schemas.user import user_schema

#Models
from models.user import UserModel, UserRegistrer
from db.database import db_client

router = APIRouter()


##Login


@router.post(
    path="/signup",
    response_model=UserModel,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Login"]
)
async def signup(
    user: UserRegistrer = Body(...)):
    """Signup register
    description:Register a User
    parameters: Request body parameters= User
    returns: Response Json with the basic information
    """
    
    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return UserRegistrer(**new_user)
    
    
    # with open("users.json", "r+", encoding="utf-8") as f:
    #     results = json.load(f)
    #     json.dump(results, f)
    #     user_dic = user.dict()
    #     user_dic["user_id"] = str(user_dic["user_id"])
    #     user_dic["birth_date"] = str(user_dic["birth_date"])
    #     results.append(user_dic)
    #     f.seek(0)
    #     f.write(json.dumps(results))
    #     return user
### Login a User
@router.post(
    path="/login",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Login"]
)
async def Login():
    pass