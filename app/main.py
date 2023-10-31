from fastapi import FastAPI, Depends, status
from db.session import get_db, engine
import models
import schemas.user
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models.user
from core.security import verify_password,get_password_hash
from typing import List

app = FastAPI()
get_db()
models.user.Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
