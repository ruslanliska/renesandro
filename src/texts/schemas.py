from __future__ import annotations

from pydantic import BaseModel
from pydantic import field_validator


class TextDescriptionSchema(BaseModel):
    description: str
    name: str
    max_characters: int
    texts_quantity: int
    product_description: str
    text_type: str
    auditory_description: str

    @field_validator('name')
    @classmethod
    def name_validator(cls, value: str):
        return value.lower()


class TextDescriptionUpdateSchema(BaseModel):
    max_characters: int
    texts_quantity: int
    text_type: str
    auditory_description: str


class TextSchema(BaseModel):
    text: str
    description_name: str


class TextCollection(BaseModel):
    texts: list[str]
