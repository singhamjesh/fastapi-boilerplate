import os
import boto3


class S3Client:

    def __init__(self):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
            region_name=os.environ['AWS_REGION'])

    def get_s3_object(self, bucket_name: str, key: str):
        return self.s3.get_object(Bucket=bucket_name, Key=key)
