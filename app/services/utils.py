import re 
from datetime import datetime

URL_REGEX = re.compile(r"https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$")

def validate_parsed_url(url:str) -> bool:
    """
    validate parsed string is valid url
    """
    validation_url: bool  = bool(re.match(URL_REGEX , url))
    return validation_url

def reparse_url(url_feed_object) -> bool:
    """
    check if last time rss url parsed is > 10 minutes them reparse 
    otherwise not 
    """
    repase = False 
    now = datetime.utcnow()
    diff_in_minutes = (now - url_feed_object.parsed_datetime).total_seconds()/60
    if diff_in_minutes > 10:
        repase = True 
    return repase