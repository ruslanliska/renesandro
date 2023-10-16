from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(
    tags=['images'],
    prefix='/images',
)
