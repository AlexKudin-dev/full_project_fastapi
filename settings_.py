from dotenv import find_dotenv
from functools import lru_cache
from pydantic.types import StrictStr
from pydantic_settings  import BaseSettings


class Settings(BaseSettings):
    HOST: StrictStr
    PORT: StrictStr
    DB_USER: StrictStr
    DB_PASSWORD: StrictStr
    DB_NAME: StrictStr


@lru_cache()
def get_settings(env_file: str = '.env') -> Settings:
    """Create settings instance."""
    return Settings(_env_file=find_dotenv(env_file))

SETTINGS = get_settings()