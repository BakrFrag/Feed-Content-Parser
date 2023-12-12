from app.db.database import SessionLocal 


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