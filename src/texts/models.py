from __future__ import annotations

from renesandro.src.database.core import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class TextDescription(Base):
    __tablename__ = 'text_description'

    description = Column(String)
    name = Column(String, primary_key=True, unique=True, index=True)
    max_characters = Column(Integer, default=50)
    texts_quantity = Column(Integer, default=5)
    product_description = Column(String, nullable=True)
    text_type = Column(String, default='quote')
    auditory_description = Column(String, nullable=True)

    def __repr__(self):
        return f'<TextDescription(description={self.description}, name={self.name})>'


class Text(Base):
    __tablename__ = 'text'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    description_name = Column(
        String, ForeignKey(
            'text_description.name',
        ), nullable=False,
    )
    description = relationship('TextDescription', backref='texts')
