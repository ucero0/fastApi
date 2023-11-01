# hash password
from passlib.context import CryptContext
from ..core.config import tokenSetings
from datetime import datetime, timedelta
from jose import JWTError, jwt

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

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, tokenSetings.SECRET_KEY, algorithms=tokenSetings.ALGORITHM)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenPayload(email=email)
    except JWTError:
        raise credentials_exception
    return token_data