from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ...db.session import get_db
from ..models import user as modelsUser
from ..schemas import user as  userSchema
from ...core.security import verify_password,get_password_hash

userRoute = APIRouter(
    prefix="/user",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)
# create user
@userRoute.post('',status_code=status.HTTP_201_CREATED, response_model=userSchema.UserResponse)
def create_user(user: userSchema.UserLogin, db: Session = Depends(get_db)):
    def get_user_by_email(db: Session, email: str):
        return db.query(modelsUser.User).filter(modelsUser.User.email == email).first()
    
    def create_user(db: Session, user: userSchema.UserLogin):
        user.password = get_password_hash(user.password)
        db_user = modelsUser.User(**user.dict())
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

@userRoute.get('',response_model=List[userSchema.UserResponse])
def get_users(db: Session = Depends(get_db)):
    def get_users(db: Session):
        return db.query(modelsUser.User).all()
    return get_users(db)