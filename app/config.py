from pydantic_settings import BaseSettings

class settings(BaseSettings):
    app_name : str = "CodingAtom Health Dasboard" # Our app name 
    app_version: str = "1.0"
    environment : str = "Developpement stage that is mainly for testing " # i gonna change in production on render.io 

    class Config:
        env_file = ".env"

settings = Settings()