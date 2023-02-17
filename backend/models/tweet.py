#Python
from datetime import datetime
from typing import Optional
from uuid import UUID
#Pydantic
from pydantic import BaseModel, Field

from models.user import UserModel

#Models



class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: UserModel = Field(...)
    


class TweetUserID(BaseModel):
    user_id: int = Field(...,
    ge=1,
    title='User who created the tweet',
    example=1,)