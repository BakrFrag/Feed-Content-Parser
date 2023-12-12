from pydantic import BaseModel

class UserSchema(BaseModel):
    """
    user login schema
    """
    username: str
    password: str 

class UserRegister(UserSchema):
    """
    user register schema
    """
    confirm_password: str 