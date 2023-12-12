from fastapi import FastAPI
from app.routers.rss_feed import router as rss_feed_router

app = FastAPI()
app.include_router(rss_feed_router)