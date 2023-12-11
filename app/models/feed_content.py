from sqlalchemy import Column, String, ForeignKey , Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base , relationship
from app.db.database import Base


class FeedContent(Base):
    __tablename__ = 'feed_content'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(512),nullable=False)
    link = Column(String(255), nullable=False)
    publish_date = Column(String(255), nullable=False)
    url_id = Column(Integer, ForeignKey('feed_url.id'))
    url = relationship("FeedURL", back_populates= "items")

    