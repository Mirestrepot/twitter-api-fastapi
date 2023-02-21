#Python
from datetime import date

from typing import Optional

#Pydantic
from pydantic import BaseModel, EmailStr, Field





#Models
class UserBaseModel(BaseModel):
    username: str = Field(...,
                          title="Username",
                          example="username123")
    id: str = Field(...)
    email: EmailStr = Field(...)
class PasswordModel(BaseModel):
        password: str = Field(
        ...,
        min_length=8,
        max_length=60)

class UserModel(UserBaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[str] = Field(default=None,
                                       title='Birth date',
                                       example='2021-01-01',)
    
class UserRegistrer(UserModel,PasswordModel):  
    pass

class LoginUser(PasswordModel):
    email: EmailStr = Field(...,)


