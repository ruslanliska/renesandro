from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from renesandro.src.database.core import get_db
from renesandro.src.formats import service
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['format'],
    prefix='/format',
)
router_placid = APIRouter(
    tags=['placid'],
    prefix='/placid',
)


@router_placid.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_description='Templates from Placid client',
)
def get_templates():
    return service.PlacidClient().get_templates()


@router.post(
    '/',
    status_code=status.HTTP_200_OK,
)
def create_template(db: Session = Depends(get_db)):
    return service.create_format(db)


router.include_router(router_placid)
