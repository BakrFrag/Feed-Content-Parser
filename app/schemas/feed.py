from pydantic import BaseModel 
from datetime import datetime
from typing import Optional
class URLFeedModel(BaseModel):
    """
    for submit url to rss feed 
    """
    url: str

class URLFeedWrtieModel(URLFeedModel):
    """
    for update / create url feed
    """
    number_of_parsed:int = 1

class FullURLFeedModel(URLFeedWrtieModel):
    """
    schema model input for feed URL
    """
    id: int 
    parsed_datetime: datetime 

class FeedContentModel(BaseModel):
    """
    schema model for feed content data
    """
    id: int 
    title: Optional[str] 
    description: Optional[str]
    link: Optional[str]
    publish_date: Optional[str]
    
   
