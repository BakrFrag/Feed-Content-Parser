from pydantic import BaseModel 
from datetime import datetime
from typing import Optional

class URLFeedModel(BaseModel):
    """
    for submit url to rss feed 
    """
    url: Optional[str]



class FullURLFeedModel(URLFeedModel):
    """
    schema model input for feed URL
    """
    id: int 
    number_of_parsed:int
    last_parsed_datetime: datetime 