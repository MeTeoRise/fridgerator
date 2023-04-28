from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_CONNECTION_URL: str

    class Config:
        env_file = '.env'
        case_sensitive = True


settings = Settings()
