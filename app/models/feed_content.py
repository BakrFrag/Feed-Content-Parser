from sqlalchemy import Column, String, ForeignKey , Integer, func
from sqlalchemy.orm import declarative_base , relationship
from . import Base
class FeedContent(Base):
    __tablename__ = 'feed_content'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    description = Column(String(512),nullable=True)
    link = Column(String(255), nullable=True)
    publish_date = Column(String(255), nullable=True)
    url_id = Column(Integer, ForeignKey('feed_url.id'))
    url = relationship("FeedURL", back_populates= "items")

    