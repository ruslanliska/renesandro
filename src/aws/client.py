from __future__ import annotations

from boto3.session import Session
from renesandro.src.config import AWS_ACCESS_KEY
from renesandro.src.config import AWS_REGION
from renesandro.src.config import AWS_SECRET_ACCESS_KEY


class S3Client:
    def __init__(self, bucket_name):
        _session = Session(
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )
        self.region = AWS_REGION
        s3 = _session.resource('s3')
        self.bucket = s3.Bucket(bucket_name)
        self.bucket_name = bucket_name

    def list_files(self, prefix=None):
        """
        Lists files in an Amazon S3 bucket.

        Args:
            prefix (str, optional): A prefix to filter files
            by folder path. If provided, only files within the
            specified folder will be listed. The prefix must end with
            a forward slash ('/').

        Returns:
            list: A list of file names or full S3
                  file objects in the specified folder.

        Note:
            - If `prefix` is provided, only files within
              the specified folder will be listed.
            - If no `prefix` is provided, all files
              in the bucket will be listed.

        Example:
            To list all files in the root of the bucket:
            s3_manager.list_files()

            To list files in a specific folder (e.g., 'images/'):
            s3_manager.list_files(prefix='images/')
        """
        files = []
        if prefix:
            for object_summary in self.bucket.objects.filter(Prefix=prefix):
                file_path = object_summary.key.strip()
                file_name = file_path.split('/')[-1]
                try:
                    if file_name:
                        files.append(file_name)
                except IndexError:
                    continue
            return files
        for s3_file in self.bucket.objects.all():
            files.append(s3_file)
        return files

    def upload_file(self, file_body, file_name):
        self.bucket.put_object(
            Key=f'{file_name}.jpg',
            Body=open(file_body, 'rb'),
        )

    def get_file_url(self, prefix, filename):
        url = f'https://{self.bucket_name}.s3.amazonaws.com/{prefix}{filename}'
        return url
