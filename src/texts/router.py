from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from renesandro.src.database.core import get_db
from renesandro.src.openai_client.client import OpenAIClient
from renesandro.src.texts import service
from renesandro.src.texts.exceptions import DescriptionAlreadyExists
from renesandro.src.texts.exceptions import DescriptionNotFound
from renesandro.src.texts.schemas import TextCollection
from renesandro.src.texts.schemas import TextDescriptionSchema
from renesandro.src.texts.schemas import TextDescriptionUpdateSchema
from renesandro.src.texts.schemas import TextSchema
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
router = APIRouter()


@router.post(
    '/create',
    status_code=status.HTTP_201_CREATED,
    response_description='Generate texts based on description',
    response_model=TextCollection,
)
def create_description(
    request: TextDescriptionSchema,
    db: Session = Depends(get_db),
):
    try:
        description_object = service.create_description(db, request)
    except IntegrityError:
        raise DescriptionAlreadyExists()

    texts = OpenAIClient().generate_texts(description=request)

    for i in texts:
        text = TextSchema(text=i, description_name=description_object.name)
        service.create_text(db=db, request=text)

    return TextCollection(texts=texts)


@router.get(
    '/description/{name}',
    status_code=status.HTTP_200_OK,
    response_description='Get description object',
)
def get_description_by_name(
    name: str,
    db: Session = Depends(get_db),
):
    return service.get_description_by_name(db, name.lower())


@router.get(
    '/description/{name}/all',
    status_code=status.HTTP_200_OK,
    response_description='Get list of all texts for description',
    response_model=TextCollection,
)
def get_list_of_texts_by_name(
    name: str,
    db: Session = Depends(get_db),
):
    description = service.get_description_by_name(db, name.lower())
    texts_objs = service.get_texts_by_description(db, description)
    return TextCollection(texts=[text.text for text in texts_objs])


@router.post(
    '/description/{name}',
    status_code=status.HTTP_201_CREATED,
    response_description='Create text collection for specific description',
)
def create_text_for_description(
    name: str,
    db: Session = Depends(get_db),
):
    description_object = service.get_description_by_name(db, name.lower())
    texts = OpenAIClient().generate_texts(description=description_object)

    for i in texts:
        text = TextSchema(text=i, description_name=description_object.name)
        service.create_text(db=db, request=text)

    return TextCollection(texts=texts)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_description='Create text object',
)
def create_single_text(
    request: TextSchema,
    db: Session = Depends(get_db),
):
    return service.create_text(db, request)


@router.post(
    '/description/{name}/modify',
    status_code=status.HTTP_200_OK,
    response_description='Modify description',
)
def modify_description(
    name: str,
    request: TextDescriptionUpdateSchema,
    db: Session = Depends(get_db),
):
    description_object = service.get_description_by_name(db, name)
    if not description_object:
        raise DescriptionNotFound()
    updated = service.update_description(db, name, request)
    return updated
