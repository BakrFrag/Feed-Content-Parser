from pydantic import BaseModel

class BaseUser(BaseModel):
    """
    base user schema 
    """
    username: str


class UserLogin(BaseModel):
    """
    user login schema
    """
    
    password: str 

class UserRegister(UserLogin):
    """
    user register schema
    """
    confirm_password: str 