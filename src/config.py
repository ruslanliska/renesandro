from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()

PRIVATE_PLACID_API_KEY = os.environ.get('PRIVATE_PLACID_API_KEY')
PUBLIC_PLACID_API_KEY = os.environ.get('PUBLIC_PLACID_API_KEY')

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


class Settings:
    PROJECT_NAME: str = 'Renesandro'
    PROJECT_VERSION: str = '1.0.0'

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER', 'localhost')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT', 5432)
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'postgres')
    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'


settings = Settings()
