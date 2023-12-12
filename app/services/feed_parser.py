import feedparser
import urllib 
import xml.sax
from fastapi import HTTPException


class ParseRssFeedContent(object):
    """
    parse rss feed content within rss feed url 
    """

    __parser = feedparser
    def __init__(self,url):
        """
        init necessry variables for feed parse 
        """
        self.url = url
        self.parse_exception = None
       
    def _handle_parse_exception(self):
        """
        handle various exceptions while get rss feed content
        """
        
        if isinstance(self.parse_exception, urllib.error.URLError):
            raise HTTPException(status_code = 400 , detail="can't parse url , check internet connection")
        elif isinstance(self.parse_exception , xml.sax._exceptions.SAXParseException):
            raise HTTPException(status_code = 400 , detail= "parsed url is not a valid rss feed")
    
    def parse_rss_conntent_feed(self):
        """
        parse rss feed & extract items
        """
        data = self.__parser.parse(self.url)
        if data.get("bozo"):
            self.parse_exception = data.get("bozo_exception")
            return self._handle_parse_exception()
        return self._extract_items(data)
    
    def _extract_items(self,data):
        """
        capture items in rss
        """
        return self._parse_data_items(data.entries) 
    
    def _parse_data_items(self , data):
        """
        extract desired info from data and set url_id for each one
        """
        parsed_data = [] 
        for item in data:
            item_data = {
                "title":item.get("title") , 
                "description":item.get("description"),
                "link":item.get("link"),
                "publish_date":item.get("published"),
                
            }
            parsed_data.append(item_data)

        return parsed_data
    

