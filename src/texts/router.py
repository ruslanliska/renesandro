from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from renesandro.src.database.core import get_db
from renesandro.src.texts import service
from renesandro.src.texts.schemas import TextDescriptionSchema
from renesandro.src.texts.schemas import TextSchema
from sqlalchemy.orm import Session
router = APIRouter()


@router.post(
    '/description',
    status_code=status.HTTP_201_CREATED,
    response_description='Create description object',
)
def create_description(
    request: TextDescriptionSchema,
    db: Session = Depends(get_db),
):
    return service.create_description(db, request)


@router.get(
    '/description/{id}',
    status_code=status.HTTP_201_CREATED,
    response_description='Create description object',
)
def get_description(
    id: int,
    db: Session = Depends(get_db),
):
    return service.get_description_by_id(db, id)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_description='Create text object',
)
def create_text(
    request: TextSchema,
    db: Session = Depends(get_db),
):
    return service.create_text(db, request)
