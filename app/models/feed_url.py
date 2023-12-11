from sqlalchemy import Column, String, DateTime, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base , relationship
from app.db.database import Base




class FeedURL(Base):
    __tablename__ = 'feed_url'

    id = Column(Integer, primary_key=True)
    url = Column(String,unique = True,nullable=False)
    number_of_parsed = Column(Integer , nullable= False)
    parsed_datetime = Column(DateTime, default=func.now(), nullable=False)
    items = relationship('FeedContent', back_populates='url')
   