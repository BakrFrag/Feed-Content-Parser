from pydantic import BaseModel 
from typing import Optional


class FeedContentModel(BaseModel):
    """
    schema model for feed content data
    """
    id: int 
    title: Optional[str] 
    description: Optional[str]
    link: Optional[str]
    publish_date: Optional[str]
    
   
