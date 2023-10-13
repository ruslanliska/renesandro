from __future__ import annotations

from fastapi import FastAPI
from renesandro.src.database.core import engine
from renesandro.src.database.manage import init_database
from renesandro.src.formats.router import router as format_router

app = FastAPI()
app.include_router(format_router)
init_database(engine)


@app.get('/')
def read_root():
    return {'Connection': 'Success'}
