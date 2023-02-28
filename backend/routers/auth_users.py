from typing import Dict
from typing import Any

# FastAPI
from fastapi import APIRouter, Request
from fastapi import HTTPException
from fastapi.security import (
    OAuth2,OAuth2PasswordBearer,
    OAuth2PasswordRequestForm)
from fastapi import Depends
from fastapi import status
from models.user import UserModel
from utils.fuction import search_user

router = APIRouter()

# Utilities

# Database
from db.database import db_client,db_users
# Models


# Schemas


oauth2 = OAuth2PasswordBearer(tokenUrl="login")


async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="not authenticated", headers={"WWW-Authenticate": "Bearer"}
        )
    return user 

### Login a User
@router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Login"]
)
async def Login(form: OAuth2PasswordRequestForm = Depends()):
    pass
    username = form.username
    asdf = []
    user_db = db_client.users.find_one({username: str})  #search_user(form.username)
    asdf.append(user_db)
    
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=asdf) 
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="password is incorrect") 
    return {"access_token": user.username , "token_type": "bearer"}

@router.get("/users/me")
async def me(user:UserModel = Depends(current_user)):
    return user

