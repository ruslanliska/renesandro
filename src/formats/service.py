from __future__ import annotations

import json
import logging

import requests
from renesandro.src.config import AWS_ACCESS_KEY
from renesandro.src.config import AWS_SECRET_ACCESS_KEY
from renesandro.src.config import PRIVATE_PLACID_API_KEY
from renesandro.src.formats.models import Format
from sqlalchemy.orm import Session


class PlacidClient:
    endpoint_base = 'https://api.placid.app/api/rest/'

    @classmethod
    def auth(cls):
        return {
            'Authorization': f'Bearer {PRIVATE_PLACID_API_KEY}',
            'Content-Type': 'application/json; charset=utf-8',
        }

    @classmethod
    def get_templates(cls):
        endpoint = cls.endpoint_base + 'templates'
        headers = cls.auth()
        response = requests.get(endpoint, headers=headers).json()
        return response

    @classmethod
    def create_image(
        cls,
        bucket_name: str,
        template_uuid: str,
        layers: dict[str, str],
        format_generation_id: str,
        source_image: str,
        image_destination_folder: str = 'formats/result',
    ):
        endpoint = cls.endpoint_base + template_uuid
        data = {
            'create_now': 'true',
            'passthrough': 'null',
            'layers': layers,
            'transfer': {
                'to': 's3',
                'key': AWS_ACCESS_KEY,
                'secret': AWS_SECRET_ACCESS_KEY,
                'region': 'us-east-1',
                'bucket': bucket_name,
                'visibility': 'public',
                'path': f'{image_destination_folder}/{format_generation_id}/renesandro-{source_image}',
                'endpoint': 'https://s3.us-east-1.amazonaws.com',
            },
        }
        headers = cls.auth()
        response = requests.post(
            endpoint, headers=headers, data=json.dumps(data),
        ).json()
        logging.debug(response)
        return response

    @classmethod
    def get_image(cls, image_id):
        endpoint = cls.endpoint_base + f'/images/{image_id}'
        response = requests.get(endpoint, headers=cls.auth()).json()
        return response

    @staticmethod
    def download_image(url):
        img_data = requests.get(url).content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(img_data)


def create_format(db: Session):
    _format = Format()
    db.add(_format)
    db.commit()
    db.refresh(_format)
    return _format
