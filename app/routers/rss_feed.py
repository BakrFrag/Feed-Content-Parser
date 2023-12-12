
from fastapi import Depends, HTTPException , APIRouter
from sqlalchemy.orm import Session
from app.dependancies.dtatanase import get_db
from app.schemas.feed_content import FeedContentModel 
from app.schemas.feed_url import URLFeedModel ,FullURLFeedModel
from app.db.queries.feed_content import  insert_bulk_feed_content , delete_bulk_feed_content , get_bulk_feed_content 
from app.db.queries.feed_url import  get_rss_by_url , add_rss_object , update_rss_object , get_all_feed_urls
from app.services.feed_parser import ParseRssFeedContent
from app.services.utils import validate_parsed_url , reparse_url
from app.authentication.http_authorization_header import JWTBearer
from typing import List 

router = APIRouter(
    prefix="/rss",
    tags=["rss-url"],
    dependencies=[Depends(get_db),Depends(JWTBearer())],

)


@router.post("/parse/",response_model=List[FeedContentModel])
def parse_url_feed(url_feed: URLFeedModel ,db:Session= Depends(get_db)):
        """
        accept rss url and parse rss feed content
        validate parsed url , 
        if url not exists , start parse 
        if url exists , and last time parsed > 10 minutes them reparse again 
        otherwise return feed content items from database 
        """
        parsed_url = url_feed.url
        if not validate_parsed_url(parsed_url):
            raise HTTPException(status_code = 400 , detail= "invalid url")
        
        url_feed_object = get_rss_by_url(db , parsed_url)
        if not url_feed_object:
           
            rss_parser = ParseRssFeedContent(parsed_url )
            data = rss_parser.parse_rss_conntent_feed()
            url_feed_object = add_rss_object(db , url_feed)
            insert_bulk_feed_content(db , data , url_feed_object.id )
            return get_bulk_feed_content(db, url_feed_object.id)
        
        elif url_feed_object and reparse_url(url_feed_object):
            rss_parser = ParseRssFeedContent(parsed_url)
            data = rss_parser.parse_rss_conntent_feed()
            url_feed_object = update_rss_object(db , url_feed_object)
            delete_bulk_feed_content(db , url_feed_object.id)
            insert_bulk_feed_content(db , data , url_feed_object.id )
            return get_bulk_feed_content(db, url_feed_object.id)
        
        return get_bulk_feed_content(db ,url_feed_object.id)
    
    
@router.get("/parse/",response_model=List[FullURLFeedModel])
def get_all_urls(db:Session= Depends(get_db)):
   
   return get_all_feed_urls(db)

