from datetime import datetime
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.feed_url import FeedURL
from app.schemas.feed_url import  URLFeedModel , FullURLFeedModel 


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
    reservation = db.query(FeedURL).filter_by(url = feed_url).first()
    return reservation 

def add_rss_object(db:Session , feed_data: FullURLFeedModel ) -> URLFeedModel:
    """
    add new feed rss url object to db 
    """
   
    url_object_data = dict(feed_data)
    feed_url_object = FeedURL(**url_object_data , number_of_parsed = 1)
    db.add(feed_url_object)
    db.commit()
    db.refresh(feed_url_object)
    return feed_url_object

def update_rss_object(db:Session , url_feed_object ) -> URLFeedModel:
    """
    update rss url object
    """
    
    
    url_feed_object.number_of_parsed  += 1
    url_feed_object.last_parsed_datetime = datetime.utcnow()
    db.commit()
    db.refresh(url_feed_object)
    return url_feed_object

def get_all_feed_urls(db:Session):
    """
    get all feed parsed urls
    """
    urls = db.query(FeedURL).all()
    return urls