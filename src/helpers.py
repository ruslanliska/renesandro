from __future__ import annotations

from typing import Annotated
from uuid import UUID
from uuid import uuid4


UUIDStr = Annotated[str, lambda v: UUID(v, version=4)]


def generate_uuid() -> str:
    return str(uuid4())
