from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    is_show_exception: bool = False
    is_show_sql: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
