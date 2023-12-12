from typing import Dict 
import jwt 
import time 

SECRET_KEY = "!sd+(p=gwjrjsbe-(a#nl!gox0t#fq94@f6u#no+81$3qmx&gm"
SCHEMA = "Bearer"


 
class JWTToken(object):
    secret_key = SECRET_KEY
    algorithm = "HS256"
    def __init__(self):
        self.payload = {
            "user_id":None , 
            "expires": time.time() + 36000
        }

    def token_response(self,user_id:int) -> Dict[str,str]:
        """
        response access token
        """
        token = self.get_token(user_id)
        return { 
            "access":token
        }

    def get_token(self, user_id:int) -> str:
        """
        get jwt token 
        """
        self.payload["user_id"]=user_id
        token = jwt.encode(self.payload, self.secret_key, algorithm=self.algorithm)
        return token


    def verify_token(self , token:str) -> dict: 
        """
        verify token if it is still valid or not
        """
        try:
            
            decoded_token = jwt.decode(
                token, 
                self.secret_key, 
                algorithms=[self.algorithm])
            return decoded_token if decoded_token.get("expires") > time.time() else None

        except Exception as E:
            
            return None
              
