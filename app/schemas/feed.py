from pydantic import BaseModel 
from datetime import date 

class ParseURLFeed(BaseModel):
    """
    schema model input for feed URL
    """
    url: str

class FeedContent(BaseModel):
    """
    schema model for feed content data
    """
    id: int 
    title: str 
    description: str 
    link: str 
    publish_date: date 
    
   
