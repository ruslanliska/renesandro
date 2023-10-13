from __future__ import annotations

from renesandro.src.database.core import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Format(Base):
    __tablename__ = 'formats'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default='Default Name')
