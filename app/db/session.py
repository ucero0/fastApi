from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from sqlalchemy.exc import OperationalError

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.USERNAME}:{settings.PASSWORD}@{settings.IP_ADRESS}:{settings.PORT}/{settings.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == '__main__':
    try:
        # # Attempt to create a database engine and connect to the database
        # engine = create_engine(SQLALCHEMY_DATABASE_URL)
        engine = create_engine('postgresql+psycopg2://postgres:4042@localhost:5432/API')
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        # # Create a Session
        session = SessionLocal()
        
        # # Use the session to try to execute a query
        session.close()
        # # Use the engine to execute a simple query to check the connection
        # connection = engine.connect()
        # result = connection.execute("SELECT 1")
        
        # If the query was successful, the connection is working
        print("Connection is working.")
        
        # Close the connection
        # connection.close()
    except OperationalError as e:
        print("Error:", e)
        print("Connection is not working.")