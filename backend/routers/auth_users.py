#Python
from utils.functions_jwt import write_token
from utils.fuction import search_user
#DB
from db.database import db_client,db_users
from db.schemas.user import user_schema
#Models
from models.user import UserRegistrer,UserModel,LoginUser

# FastAPI
from fastapi import APIRouter, Body, Request,HTTPException,status, Depends
from fastapi.security import (
    OAuth2,OAuth2PasswordBearer,
    OAuth2PasswordRequestForm)
from fastapi.responses import JSONResponse





router = APIRouter()


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
#OAuth2PasswordRequestForm
async def Login(form: LoginUser = Body(...) ):
    username = form.username
    password = form.password
    # username = user.username
    # password =  user.password
    def find_by_username(username: str):
        try:
            user = user_schema(db_client.users.find_one({"username": username}))
            return UserRegistrer(**user)
        except:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="not authenticated", headers={"WWW-Authenticate": "Bearer"})
        # user_model = UserRegistrer(**user_schema(user))

        
    
    current_user = find_by_username(username)
    if form.username == current_user.username:
        return write_token(current_user)
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=status.HTTP_404_NOT_FOUND)
    # if password == current_user.password:
    #     return ("success", current_user)
    
    
    
    # username = form.username
    # user_db = db_client.users.find_one({username: str})  #search_user(form.username)
    # if not user_db:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="first raise") 
    # user = search_user(form.username)
    # if not form.password == user.password:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="password is incorrect") 
    # return {"access_token": user.username , "token_type": "bearer"}

@router.get("/users/me")
async def me(user:UserModel = Depends(current_user)):
    return user

