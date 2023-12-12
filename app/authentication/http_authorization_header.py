from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_token import JWTToken

class JWTBearer(HTTPBearer):
    """
    JWT Bearer , ensure Headers include authorization and validate token
    """
    def __init__(self, auto_error: bool = False):
        
        super(JWTBearer, self).__init__(auto_error=auto_error)
        

    async def __call__(self, request: Request):
        
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials and (not self.verify_jwt(credentials.credentials)):
               raise HTTPException(status_code=401, detail="Invalid token or expired token.")
           
        elif not credentials:
               raise HTTPException(status_code=401, detail="Invalid Authentication")
        
        return credentials.credentials

    def verify_jwt(self, jwtoken: str) -> bool:
        """
        verify barsed token
        """
        try:
                
                jwt = JWTToken()
                token_verification  = jwt.verify_token(jwtoken)
                return True if token_verification is not None else False 
                
        except Exception as E:
            
                return False
    