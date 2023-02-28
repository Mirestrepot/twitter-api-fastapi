#Python

import json


#FastApi

from fastapi import Body, Depends, HTTPException,status
from fastapi import APIRouter
from db.schemas.user import user_schema
from fastapi.security import (
    HTTPAuthorizationCredentials,HTTPBearer,
    OAuth2,OAuth2PasswordBearer,
    OAuth2PasswordRequestForm)

#Models
from models.user import LoginUser, UserModel, UserRegistrer
from db.database import db_client
from routers.auth_users import current_user
from utils.fuction import create_user, search_user

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
    

    new_user = create_user(user)

    return UserRegistrer(**new_user)


