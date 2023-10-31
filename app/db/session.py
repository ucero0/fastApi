from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import settings
from sqlalchemy.exc import OperationalError

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.USERNAME_DB}:{settings.PASSWORD}@{settings.IP_ADRESS}:{settings.PORT}/{settings.DATABASE_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session =sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Session()
    try:
        yield db

    finally:
        db.close()
