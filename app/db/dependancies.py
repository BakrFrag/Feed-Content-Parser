from .database import SessionLocal , engine 
from app.models import feed_content , feed_url


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