from db.database import db_client
from db.schemas.user import user_schema, users_schema

from models.user import UserModel

def search_user(field: str, key):

    try:
        user = db_client.users.find_one({field: key})
        return UserModel(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}
