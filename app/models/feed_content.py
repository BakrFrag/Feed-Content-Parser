from sqlalchemy import Column, String, DateTime, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base



Base = declarative_base()

class FeedURL(Base):
    __tablename__ = 'feed_url'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(512),nullable=False)
    link = Column(String(255), nullable=False)
    publish_date = Column(String(255), nullable=False)

    def __init__(self, title , description , link , publish_date):
        self.title = title 
        self.link = link 
        self.description = description 
        self.publish_date = publish_date