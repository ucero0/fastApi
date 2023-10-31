from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
import models
import schemas.user
from core.security import verify_password,get_password_hash

router = APIRouter(
    prefix="/user",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)
# create user
@router.post(status_code=status.HTTP_201_CREATED, response_model=schemas.user.UserCreateResponse)
def create_user(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    def get_user_by_email(db: Session, email: str):
        return db.query(models.user.User).filter(models.user.User.email == email).first()
    
    def create_user(db: Session, user: schemas.user.UserCreate):
        user.password = get_password_hash(user.password)
        db_user = models.user.User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Email already registered")
    else:
        user = create_user(db=db, user=user)
        return user

@router.get(response_model=List[schemas.user.UserCreateResponse])
def get_users(db: Session = Depends(get_db)):
    def get_users(db: Session):
        return db.query(models.user.User).all()
    return get_users(db)

# login user
@router.get("/login", response_model=schemas.user.UserCreateResponse)
def login_user(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    def get_user_by_email(db: Session, email: str):
        return db.query(models.user.User).filter(models.user.User.email == email).first()
    
    db_user = get_user_by_email(db, email=user.email)
    incorrectPassOrEmail = HTTPException(status_code=400, detail="Email or password incorrect")
    if db_user:
        if verify_password(user.password, db_user.password):
            return db_user
        else:
            raise incorrectPassOrEmail
    else:
        raise incorrectPassOrEmail