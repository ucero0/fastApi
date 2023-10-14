from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    USERNAME : str
    PASSWORD :str 
    IP_ADRESS :int|str 
    PORT :int     
    DATABASE_NAME:str 

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()

