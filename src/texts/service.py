from __future__ import annotations

from fastapi import HTTPException
from fastapi import status
from renesandro.src.texts.models import Text
from renesandro.src.texts.models import TextDescription
from renesandro.src.texts.schemas import TextDescriptionSchema
from renesandro.src.texts.schemas import TextSchema
from sqlalchemy.orm import Session


def create_description(db: Session, request: TextDescriptionSchema):
    _description = TextDescription(
        description=request.description, name=request.name,
    )
    db.add(_description)
    db.commit()
    db.refresh(_description)
    return _description


def get_description_by_id(db: Session, description_id: int):
    description = db.query(TextDescription).get(description_id)
    if not description:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Description with ID {description_id} not found.',
        )
    return description


def create_text(db: Session, request: TextSchema):
    _text = Text(text=request.text, description_id=request.description_id)
    db.add(_text)
    db.commit()
    db.refresh(_text)
    return _text
