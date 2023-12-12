
from fastapi import Depends, HTTPException , APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.db.dependancies import get_db
from app.schemas.feed import FeedContentModel , URLFeedModel ,FullURLFeedModel
from app.services.queries import get_rss_by_url , add_rss_object , update_rss_object , insert_bulk_feed_content , delete_bulk_feed_content , get_bulk_feed_content ,get_all_feed_urls
from app.services.feed_parser import ParseRssFeed
from app.services.utils import validate_parsed_url , reparse_url
from typing import List 
import sys
router = APIRouter(
    prefix="/rss",
    tags=["rss-url"],
    dependencies=[Depends(get_db)],

)


@router.post("/parse/",response_model=List[FeedContentModel])
def parse_url_feed(url_feed: URLFeedModel ,db:Session= Depends(get_db)):
    
        parsed_url = url_feed.url
        if not validate_parsed_url(parsed_url):
            
            raise HTTPException(status_code = 400 , detail= "invalid url")
        
        url_feed_object = get_rss_by_url(db , parsed_url)
        if not url_feed_object:
          
            url_feed_object = add_rss_object(db , url_feed)
            rss_parser = ParseRssFeed(parsed_url)
            data = rss_parser.parse_rss_feed()
            data = rss_parser.parse_data( url_feed_object.id , data)
            insert_bulk_feed_content(db , data )
            return JSONResponse(content=data, status_code=200)
        
        elif url_feed_object and reparse_url(url_feed_object):
           
            rss_parser = ParseRssFeed(parsed_url)
            data = rss_parser.parse_rss_feed()
            data = rss_parser.parse_data(  url_feed_object.id , data)
            url_feed_object = update_rss_object(db , url_feed_object)
            delete_bulk_feed_content(db , url_feed_object.id)
            insert_bulk_feed_content(db , data )
            return JSONResponse(content=data, status_code=200)
        return get_bulk_feed_content(db ,url_feed_object.id)
    
    
@router.get("/parse/",response_model=List[FullURLFeedModel])
def get_all_urls(db:Session= Depends(get_db)):
   
   return get_all_feed_urls(db)