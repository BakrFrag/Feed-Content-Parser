from fastapi import Depends, HTTPException , APIRouter
from sqlalchemy.orm import Session
from app.dependancies.dtatanase import get_db
from app.schemas.user import UserRegister , UserSchema
from app.services.user import check_hashed_password , get_hashed_password
from app.authentication.jwt_token import JWTToken
from app.db.queries.user import get_user_by_username , add_user
router = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(get_db)],
    
)

@router.post("/add/",response_model=UserSchema)
def register_new_user(user_data:UserRegister , db: Session = Depends(get_db)) -> UserSchema:
    """
    add new user
    """
    print("user data:",user_data)
    user_exits = get_user_by_username(db , user_data.username.lower())
    if user_exits:
        raise HTTPException(status_code=400, detail="Username already registered")
    elif user_data.password != user_data.confirm_password:
        raise HTTPException(status_code=400 , detail="parsed password & confirmed password don't match ")

    hashed_password = get_hashed_password(user_data.password).decode("utf-8")
    user_data = UserSchema(
            username =user_data.username.lower() , 
            password = hashed_password
    )
    return add_user(db,user_data)


@router.post("/login/")
def login_user(login_data:UserSchema,db:Session = Depends(get_db)):
   
   
    user_by_username = get_user_by_username(db , login_data.username.lower())
    password = login_data.password
    
    if (not user_by_username):
        raise HTTPException(status_code=400 , detail = "username not exists")

    password_check = check_hashed_password(password , user_by_username.password)
    if not password_check:
        raise HTTPException(status_code=400 , detail = "wrong username or password")
    jwt = JWTToken()
    token_response = jwt.token_response(user_by_username.id)
    return token_response