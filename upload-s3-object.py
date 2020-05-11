import boto3
from botocore.client import Config
s3 = boto3.resource('s3')

data =  open('hello.csv','rb')
bucket_name = 'cbz-b15'

s3.Bucket(bucket_name).put_object(Key='test.py', Body=data)
print('done')