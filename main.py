from app.db import Base, engine
from app.routes.tasks import router
from fastapi import FastAPI
app=FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router)