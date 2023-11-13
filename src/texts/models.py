from __future__ import annotations

from renesandro.src.database.core import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Texts(Base):
    __tablename__ = 'texts'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    name = Column(String, nullable=True)
    texts = Column(String)
