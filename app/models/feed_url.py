from sqlalchemy import Column, String, DateTime, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base , relationship



Base = declarative_base()

class FeedURL(Base):
    __tablename__ = 'feed_url'

    id = Column(Integer, primary_key=True)
    url = Column(String,unique = True,nullable=False)
    parsed_datetime = Column(DateTime, default=func.now(), nullable=False)
    items = relationship('FeedURL', back_populates='url')
    def __init__(self, url):
        self.url = url