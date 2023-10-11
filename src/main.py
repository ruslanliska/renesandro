from __future__ import annotations

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'Connection': 'Success'}
