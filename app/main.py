from fastapi import FastAPI
from app.routers.rss import router as rss_router

app = FastAPI()
app.include_router(rss_router)