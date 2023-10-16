from __future__ import annotations

from fastapi import APIRouter
from renesandro.src.formats.router import router as formats_router
from renesandro.src.images.router import router as images_router

api_router = APIRouter()

api_router.include_router(images_router, prefix='/images', tags=['images'])
api_router.include_router(formats_router, prefix='/formats', tags=['formats'])
