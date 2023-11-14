from __future__ import annotations

from renesandro.src.database.core import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class TextDescription(Base):
    __tablename__ = 'text_description'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String)
    name = Column(String, nullable=True, unique=True)
    max_characters = Column(Integer, default=50)
    texts_quantity = Column(Integer, default=5)
    product_description = Column(String, nullable=True)
    text_type = Column(String, default='quote')
    auditory_description = Column(String, nullable=True)

    def __repr__(self):
        return f'<TextDescription(id={self.id}, description={self.description}, name={self.name})>'


class Text(Base):
    __tablename__ = 'text'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    description_id = Column(
        Integer, ForeignKey(
            'text_description.id',
        ), nullable=False,
    )
    description = relationship('TextDescription', backref='texts')
