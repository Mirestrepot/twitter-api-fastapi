#Python
from datetime import datetime
from typing import Optional

#Pydantic
from pydantic import BaseModel, Field

from models.user import UserModel, UserRegistrer

#Models



class Tweet(BaseModel):
    id: str = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: UserRegistrer = Field(...)
    


class TweetUserID(BaseModel):
    user_id: str = Field(...,
    title='User who created the tweet',

    )