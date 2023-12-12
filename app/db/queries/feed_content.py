from sqlalchemy.orm import Session
from app.models.feed_content import FeedContent


def insert_bulk_feed_content(db:Session, data:list ):
    """
    query optimization for insert multipli feed content with single query 
    instead of one query for each item
    """
    feed_content_data = [FeedContent(**obj) for obj in data] 
    db.add_all(feed_content_data)
    
    db.commit()



def delete_bulk_feed_content(db:Session,url_id:int):
    """
    query optimization for delete bulk rows 
    delete all content for specfic url 
    in case of re-parse url after 10 minutes and them update with new parse data
    """
   
    db.query(FeedContent).filter(FeedContent.url_id == url_id).delete()
    db.commit()

def get_bulk_feed_content(db:Session,url_id):
    """
    return bulk feed content that's attached for specfic url by id
    """
   
    return db.query(FeedContent).filter(url_id == url_id).all()





