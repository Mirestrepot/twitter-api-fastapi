def user_schema(user) -> dict:
    return {
        "password": user["password"],
        "id": str(user["_id"]),
        "email": user["email"],
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "birth_date": user["birth_date"],
        
    }
    
def users_schema(user) -> list:
    return [user_schema(user) for user in user]