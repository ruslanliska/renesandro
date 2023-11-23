from __future__ import annotations

from pydantic import BaseModel


class TextsListResult(BaseModel):
    texts: list[str]
