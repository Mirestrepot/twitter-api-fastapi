

from fastapi import FastAPI

from routers.login import router as login_router
from routers.user import router as user_router
from routers.tweet import router as tweet_router


app = FastAPI()

app.include_router(login_router, prefix='/login')
app.include_router(user_router, prefix='/user')
app.include_router(tweet_router, prefix='/tweet')
