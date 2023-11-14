from __future__ import annotations

from fastapi import HTTPException
from fastapi import status
from fastapi.exceptions import RequestValidationError


class RequestException(RequestValidationError):
    ...


class DescriptionNotFound(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Description with such name does not exist.',
        )
