import bcrypt
def get_hashed_password(password: str) -> bytes:
    """
    convert password from clear text to hashed version 
    """
    salt = bcrypt.gensalt()
    encoded_password = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password


def check_hashed_password(password:str , hashed_password:str) -> bool:
    """
    check if parsed password match hashed password 
    """
    encoded_password = password.encode("utf-8")
    encoded_hashed_password = hashed_password.encode("utf-8")
    return bcrypt.checkpw(encoded_password , encoded_hashed_password)