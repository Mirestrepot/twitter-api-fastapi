#Python
from datetime import datetime
from typing import Optional

#Pydantic
from pydantic import BaseModel, Field

from models.user import UserBaseModel, UserModel

#Models



class TweetUsername(BaseModel):
    by: str = Field(...,
                        title='User who created the tweet',

    )
class TweetUserId(BaseModel):
    user_id: str = Field(...,
                        title='User who created the tweet', )   

class BaseTweet(TweetUserId):
   content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
 

class Tweet(BaseTweet,TweetUsername,TweetUserId):
    id: str = Field(...)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[str] = Field(default=None,
                                      example = None)

class TweetDomain(Tweet):
    user: UserModel = Field(...,
                        title='User who created the tweet', )    
