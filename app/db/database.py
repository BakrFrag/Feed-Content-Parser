from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.models import feed_content , feed_url , user
SQLALCHEMY_DATABASE_URL = "sqlite:///./rss_parser.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




# migeate feed content to db
feed_content.Base.metadata.create_all(bind=engine)
# migrate feed url to db
feed_url.Base.metadata.create_all(bind=engine)
# migrate user to db 
user.Base.metadata.create_all(bind=engine)