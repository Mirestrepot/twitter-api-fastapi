def user_schema(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "birth_date": user["birth_date"],
        "username": user["username"],
        "password": user["password"]
    }

    
def users_schema(users) -> list:
    return [user_schema(user) for user in users]

