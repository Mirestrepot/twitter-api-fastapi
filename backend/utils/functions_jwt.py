import datetime
from os import getenv
from jwt import decode, encode
from jwt import exceptions
from fastapi.responses import JSONResponse
from fastapi import HTTPException,status


def expire_date(days:int): 
    date = datetime.now()
    new_date = date + datetime.timedelta(days)
    return new_date
def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2) }, key=getenv("SECRET_KEY"), algorithm="HS256")
    return token

def validate_token(token, output=False):
    try:
        if output:
            decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=status.HTTP_401_UNAUTHORIZED)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"messege": "Token Expired"}, status_code=status.HTTP_401_UNAUTHORIZED)