from __future__ import annotations

from dataclasses import dataclass

from fastapi import Form


@dataclass
class ImageGenerationData:
    customer_name: str = Form(...)
    images_count: int = Form(...)
    aspect: str = Form(...)
    style: str = Form(...)
