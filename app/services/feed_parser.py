import feedparser
import urllib 
import xml.sax
from fastapi import HTTPException


class ParseRssFeed(object):
    """
    parse rss feed within rss feed url 
    """

    __parser = feedparser()
    def __init__(self,url):
        """
        init necessry variables for feed parse 
        """
        self.url = url
        self.parse_exception = None

    def handle_parse_exception(self):
        """
        handle various exceptions while get rss feed content
        """
        if isinstance(self.parse_exception, urllib.error.URLError):
            raise HTTPException("can't parse url , check internet connection")
        elif isinstance(self.parse_exception , xml.sax._exceptions.SAXParseException):
            raise HTTPException("parsed url is not rss feed")
    
    def parse_rss_feed(self, url:str):
        """
        parse rss feed & extract items
        """
        data = self.__parser.parse(self.url)
        if data.get("bozo"):
            self.parse_exception = data.get("bozo_exception")
            return self.handle_parse_exception()
        return self.extract_items(data)
    
    def extract_items(self,data):
        """
        capture items in rss
        """
        return data.entries
    

