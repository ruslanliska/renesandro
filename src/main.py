from __future__ import annotations

from fastapi import FastAPI
from renesandro.src.api import api_router
from renesandro.src.config import BASE_API_URL
from renesandro.src.database.core import engine
from renesandro.src.database.manage import init_database

app = FastAPI(title='Renesandro')

app.include_router(api_router, prefix=BASE_API_URL)


init_database(engine)


@app.get('/')
def read_root():
    return {'Connection': 'Success'}
