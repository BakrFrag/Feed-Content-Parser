from .database import SessionLocal , engine
from app.models.feed_content import FeedContent as feed_content
from app.models.feed_url import FeedURL as feed_url
#migrate User Table to Database
feed_content.Base.metadata.create_all(bind=engine)
feed_url.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    """
    yield db session for various quries
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()