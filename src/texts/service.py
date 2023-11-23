from __future__ import annotations

from renesandro.src.texts.exceptions import DescriptionNotFound
from renesandro.src.texts.models import Text
from renesandro.src.texts.models import TextDescription
from renesandro.src.texts.schemas import TextDescriptionSchema
from renesandro.src.texts.schemas import TextDescriptionUpdateSchema
from renesandro.src.texts.schemas import TextSchema
from sqlalchemy.orm import Session


def create_description(db: Session, request: TextDescriptionSchema):
    _description = TextDescription(
        description=request.description,
        name=request.name,
        max_characters=request.max_characters,
        texts_quantity=request.texts_quantity,
        product_description=request.product_description,
        text_type=request.text_type,
        auditory_description=request.auditory_description,
    )
    db.add(_description)
    db.commit()
    db.refresh(_description)
    return _description


def update_description(
    db: Session,
    description_name: str,
    request: TextDescriptionUpdateSchema,
):
    # get the existing data
    db_description = db.query(TextDescription).filter(
        TextDescription.name == description_name,
    ).one_or_none()
    if not db_description:
        return None

    # Update model class variable from requested fields
    for var, value in vars(request).items():
        setattr(db_description, var, value) if value else None

    db.add(db_description)
    db.commit()
    db.refresh(db_description)
    return db_description


def get_description_by_name(db: Session, description_name: str):
    description = db.query(TextDescription).get(description_name)
    if not description:
        raise DescriptionNotFound()
    return description


def create_text(db: Session, request: TextSchema):
    description = get_description_by_name(
        db=db, description_name=request.description_name.lower(),
    )
    _text = Text(text=request.text, description_name=description.name)
    db.add(_text)
    db.commit()
    db.refresh(_text)
    return _text


def get_texts_by_description(db: Session, description: TextDescription):
    texts = db.query(Text).filter(
        description == Text.description,
    ).all()
    return texts
