from sqlalchemy.orm import Session
from app.schemas.user import UserSchema
from app.models.user import User


def get_user_by_username(db:Session , username:str):
    """
    get user by username
    """
    return db.query(User).filter(User.username==username).first()


def get_user_by_id(db:Session , user_id:int):
    """
    get user by id
    """
    return db.query(User).filter(User.id==user_id).first()





def add_user(db:Session , new_user:UserSchema):
    """
    create new user 
    """
    user = User(username = new_user.username , password = new_user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user 
    






