from pydantic import BaseModel 
from datetime import date , datetime

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
    title: str 
    description: str 
    link: str 
    publish_date: date 
    
   
