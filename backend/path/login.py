#Python
import json


#FastApi

from fastapi import Body,status
from fastapi import APIRouter

#Models
from models.user import UserModel, UserRegistrer


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
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        json.dump(results, f)
        user_dic = user.dict()
        user_dic["user_id"] = str(user_dic["user_id"])
        user_dic["birth_date"] = str(user_dic["birth_date"])
        results.append(user_dic)
        f.seek(0)
        f.write(json.dumps(results))
        return user
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