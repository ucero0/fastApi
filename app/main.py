from fastapi import FastAPI, Depends
from app.db.session import get_db, engine
from app.db.base import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)
@app.get("/")
async def read_root():
    return {"Hello": "World"}