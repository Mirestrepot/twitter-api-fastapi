#Python
from datetime import date
from typing import Optional
from uuid import UUID
#Pydantic
from pydantic import BaseModel, EmailStr, Field





#Models
class UserBaseModel(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
class PasswordModel(BaseModel):
        password: str = Field(
        ...,
        min_length=8,
        max_length=60)
class UserLoginModel(UserBaseModel,PasswordModel):
    pass
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
    birth_date: Optional[date] = Field(default=None)
    
class UserRegistrer(UserModel,PasswordModel):  
    
    pass

class LoginRequest(PasswordModel):
    email: EmailStr = Field(...,)


