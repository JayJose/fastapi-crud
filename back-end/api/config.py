from functools import lru_cache
import pydantic


class Settings(pydantic.BaseSettings):

    # project config
    API_TITLE: str = "An API title"
    API_DESCRIPTION: str = "An API description"
    API_PREFIX: str = "/api/v0"
    API_VERSION: str = "0.0.0"
    API_LICENSE_NAME: str = "Apache 2.0"
    API_LICENSE_URL: str = "https://www.apache.org/licenses/LICENSE-2.0.html"

    # database config
    POSTGRES_HOST: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # env config
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
