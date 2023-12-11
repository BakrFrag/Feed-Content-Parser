from datetime import datetime
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import HTTPException , Depends
from sqlalchemy.orm import Session
from app.db.database import engine
from app.models.feed_content import FeedContent
from app.models.feed_url import FeedURL
from app.schemas.feed import FeedContentModel , URLFeedModel , URLFeedWrtieModel

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

def add_rss_object(db:Session , feed_data: URLFeedWrtieModel) -> URLFeedModel:
    """
    add new feed rss url object to db 
    """
    print("feed data:",feed_data,type(feed_data))
    print("feed data dirs:",dir(feed_data))
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
    url_feed_object.parsed_datetime = datetime.utcnow()
    db.commit()
    db.refresh(url_feed_object)
    return url_feed_object


def insert_bulk_feed_content(db:Session, data:list , url_id: int):
    """
    query optimization for insert multipli feed content with single query 
    instead of one query for each item
    """
    data_to_insert = []
    for item in data: 
        item_data = {
            "title":item.get("title") , 
            "description":item.get("description"),
            "link":item.get("link"),
            "publish_date":item.get("publishDate"),
            "url_id":url_id
        }
        data_to_insert.append(item_data)

    insert_bulk_feed_content_query = FeedContent.insert().values(data_to_insert)
    with engine.connect() as db_connection:
        db_connection.execute(insert_bulk_feed_content_query)


def delete_bulk_feed_content(db:Session,url_id:int):
    """
    query optimization for delete bulk rows 
    delete all content for specfic url 
    in case of re-parse url after 10 minutes and them update with new parse data
    """
    delete_bulk_feed_content_query = FeedContent.delete().where(FeedContent.c.url_id == url_id)
    with engine.connect() as db_connection:
        db_connection.execute(delete_bulk_feed_content_query)

