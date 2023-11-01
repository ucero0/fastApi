
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...db.session import get_db
from ..models import user as modelsUser
from ..schemas import user as  userSchema
from ...core.security import verify_password,create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
auth = APIRouter(
    prefix="/login",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)
# login user
@auth.post("", response_model=userSchema.Token)
def login_user(user: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    def get_user_by_email(db: Session, username: str):
        return db.query(modelsUser.User).filter(modelsUser.User.email == username).first()
    
    db_user = get_user_by_email(db, username=user.username)
    incorrectPassOrEmail = HTTPException(status_code=400, detail="username or password incorrect")
    if not db_user:
        raise incorrectPassOrEmail
    if not verify_password(user.password, db_user.password):
        raise incorrectPassOrEmail
    payload = userSchema.TokenPayload.model_validate(db_user)
    token = create_access_token(payload.model_dump())
    token = userSchema.Token(access_token=token, token_type="bearer")
    return token
