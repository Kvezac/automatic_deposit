from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DATE_FORMAT: str

    @property
    def ASYNC_DATABASE_URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATE_FOMAT(self):
        return self.DATE_FORMAT

    class Config:
        env_file = ".env"


settings = Settings() # type: ignore
