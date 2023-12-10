from pydantic import BaseModel 
from datetime import date , datetime

class URLFeedModel(BaseModel):
    """
    schema model input for feed URL
    """
    id: int 
    url: str
    parsed_datetime: datetime 

class FeedContentModel(BaseModel):
    """
    schema model for feed content data
    """
    id: int 
    title: str 
    description: str 
    link: str 
    publish_date: date 
    
   
