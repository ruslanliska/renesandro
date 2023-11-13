from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from renesandro.src.images.schemas import ImageGenerationData
router = APIRouter()


@router.post(
    '/generate',
    status_code=status.HTTP_200_OK,
)
def generate_images(image_data: ImageGenerationData = Depends()):
    return {'image_data': image_data}
