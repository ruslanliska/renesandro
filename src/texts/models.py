from __future__ import annotations

from renesandro.src.database.core import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String


class TextDescription(Base):
    __tablename__ = 'text_description'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String)
    name = Column(String, nullable=True)

    def __repr__(self):
        return f'<TextDescription(id={self.id}, description={self.description}, name={self.name})>'


class Text(Base):
    __tablename__ = 'text'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    description = Column(ForeignKey('text_description.id'))
