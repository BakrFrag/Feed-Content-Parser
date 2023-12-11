from datetime import datetime 
from fastapi import Depends, HTTPException , APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.db.dependancies import get_db
from app.schemas.feed import FeedContentModel , URLFeedModel
from app.services.queries import get_rss_by_url , get_rss_url_by_id , add_rss_object , update_rss_object , insert_bulk_feed_content , delete_bulk_feed_content
from app.services.feed_parser import ParseRssFeed
from app.services.utils import validate_parsed_url , reparse_url
from typing import List 
import sys
router = APIRouter(
    prefix="/rss",
    tags=["rss-url"],
    dependencies=[Depends(get_db)],

)

# 
@router.post("/parse/",response_model=List[FeedContentModel])
def parse_url_feed(url_feed: URLFeedModel ,db:Session= Depends(get_db)):
    try:
        parsed_url = url_feed.url
        if not validate_parsed_url(parsed_url):
            
            raise HTTPException(status_code = 400 , detail= "invalid url")
        
        url_feed_object = get_rss_by_url(db , parsed_url)
        if not url_feed_object:
            
            rss_parser = ParseRssFeed(parsed_url)
            data = rss_parser.parse_rss_feed()
            url_feed_object = add_rss_object(db , url_feed)
            insert_bulk_feed_content(db , data , url_feed_object.id)
            return JSONResponse(content=data, status_code=200)
        
        elif url_feed_object and reparse_url(url_feed_object):
            print("re pase take place")
            rss_parser = ParseRssFeed(parsed_url)
            data = rss_parser.parse_rss_feed()
            print("url feed object:",url_feed_object.id)
            url_feed_object = update_rss_object(db , url_feed_object)
            print(f"url feed object updated with number:{url_feed_object.number_of_parsed}")
            delete_bulk_feed_content(db , url_feed_object.id)
            print("bulk delete feed object")
            insert_bulk_feed_content(db , data , url_feed_object.id)
            print("bulk insert feed objects")
            return JSONResponse(content=data, status_code=200)

    except Exception as E:
        #print(sys.exc_info())
        raise HTTPException(status_code= 500 , detail = f"internal server error\n {sys.exc_info()}")    
    



    
    


