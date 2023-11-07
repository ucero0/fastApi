# hash password
from passlib.context import CryptContext
from ..core.config import tokenSetings
from datetime import datetime, timedelta
from jose import JWTError, jwt
from ..api.schemas.user import TokenPayload, Token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    '''
    return true if password is correct'''
    return pwd_context.verify(plain_password, hashed_password)

#TOKEN-----------------------------------------------------------------------------------------------------------------

def create_access_token(payload: dict):
    to_encode = payload.copy()
    expire = datetime.utcnow() + timedelta(minutes=tokenSetings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, tokenSetings.SECRET_KEY, algorithm=tokenSetings.ALGORITHM)
    return token 

def decode_token(token: Token):
    payload = jwt.decode(token.access_token, tokenSetings.SECRET_KEY, algorithms=tokenSetings.ALGORITHM)
    payload = TokenPayload(**payload)
    return payload
        