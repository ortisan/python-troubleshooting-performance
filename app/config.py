from pydantic import BaseSettings

class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 3306
    db_username: str = "root"
    db_password: str = "123456"
    db_databasename: str = "tickdb"

settings = Settings()