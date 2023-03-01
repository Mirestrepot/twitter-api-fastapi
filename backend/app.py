

from fastapi import FastAPI

from routers.login import router as login_router
from routers.user import router as user_router
from routers.tweet import router as tweet_router
from routers.auth_users import router as auth_user_router
from fastapi.responses import RedirectResponse

app = FastAPI()

# @app.get('/')
# async def root():
#     return RedirectResponse(url ="/docs")

app.include_router(login_router, prefix='/login')
app.include_router(user_router, prefix='/user')
app.include_router(tweet_router, prefix='/tweet')
app.include_router(auth_user_router, prefix='/login')

