from sqlalchemy import Column, String, DateTime, Integer, func
from sqlalchemy.orm import declarative_base , relationship
from . import Base

class FeedURL(Base):
    __tablename__ = 'feed_url'

    id = Column(Integer, primary_key=True)
    url = Column(String,unique = True,nullable=False)
    number_of_parsed = Column(Integer , nullable= False)
    last_parsed_datetime = Column(DateTime, default=func.now(), nullable=False)
    items = relationship('FeedContent', back_populates='url')
   