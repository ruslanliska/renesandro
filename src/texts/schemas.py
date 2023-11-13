from __future__ import annotations

from pydantic import BaseModel


class TextDescriptionSchema(BaseModel):
    description: str
    name: str


class TextSchema(BaseModel):
    text: str
    description_id: int
