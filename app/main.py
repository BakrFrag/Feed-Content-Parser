from fastapi import FastAPI
from app.routers.rss_feed import router as rss_feed_router
from app.routers.user import router as user_router
app = FastAPI()
app.include_router(rss_feed_router)
app.include_router(user_router)