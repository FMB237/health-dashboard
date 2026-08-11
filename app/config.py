from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name : str = "CodingAtom Health Dashboard" # Our app name 
    app_version: str = "1.0"
    environment : str = "Development stage that is mainly for testing" # i gonna change in production on render.io 

    class Config:
        env_file = ".env"

settings = Settings()
