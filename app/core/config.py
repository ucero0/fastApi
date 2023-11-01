from pydantic_settings import BaseSettings


class DbSettings(BaseSettings):
    USERNAME_DB : str
    PASSWORD :str 
    IP_ADRESS :int|str 
    PORT :int     
    DATABASE_NAME:str 

    class Config:
        env_file = 'app\.env.db'
        env_file_encoding = 'utf-8'

class TokenSetings(BaseSettings):
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    TOKEN_TYPE : str

    class Config:
        env_file = 'app\.env'
        env_file_encoding = 'utf-8'

dbSetings = DbSettings()
tokenSetings = TokenSetings()


