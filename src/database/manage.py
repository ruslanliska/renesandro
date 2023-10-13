from __future__ import annotations

from renesandro.src.config import settings
from renesandro.src.database.core import Base
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL


def init_database(engine):
    """Initializes the database."""
    if not database_exists(str(SQLALCHEMY_DATABASE_URL)):
        create_database(str(SQLALCHEMY_DATABASE_URL))

    Base.metadata.create_all(bind=engine)
