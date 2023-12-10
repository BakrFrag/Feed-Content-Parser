from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import HTTPException , Depends
from app.schemas import *
from sqlalchemy.orm import Session
from app.models.feed_content import FeedContent
from app.models.feed_url import FeedURL
from app.schemas.feed import FeedContentModel , URLFeedModel

def get_rss_url_by_id(db:Session , feed_url:int) -> URLFeedModel :
    """
    get feed object by id 
    """
    reservation = db.query(FeedURL).filter(id == feed_url).first()
    return reservation 

def get_rss_by_url(db:Session , feed_url:str) -> URLFeedModel:
    """
    get feed object by url 
    """
    reservation = db.query(FeedURL).filter(url == feed_url).first()
    return reservation 




