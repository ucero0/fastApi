from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    USERNAME_DB : str
    PASSWORD :str 
    IP_ADRESS :int|str 
    PORT :int     
    DATABASE_NAME:str 

    class Config:
        env_file = 'app\.env'
        env_file_encoding = 'utf-8'

settings = Settings()

if __name__ == '__main__':
    settings = Settings()
    print(settings.__dict__.keys())
    print(settings.USERNAME_DB)