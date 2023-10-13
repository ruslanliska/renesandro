from __future__ import annotations

from boto3.session import Session
from renesandro.src.config import AWS_ACCESS_KEY
from renesandro.src.config import AWS_SECRET_ACCESS_KEY


class S3Client:
    def __init__(self, bucket_name):
        session = Session(
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )
        s3 = session.resource('s3')
        self.bucket = s3.Bucket(bucket_name)

    def list_files(self):
        for s3_file in self.bucket.objects.all():
            print(s3_file.key)

    def upload_file(self, file_body, file_name):
        self.bucket.put_object(
            Key=f'{file_name}.jpg',
            Body=open(file_body, 'rb'),
        )
