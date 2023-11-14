import boto3
import pandas as pd
import os

# Creditentials are store in environment variables

#Connect to AWS S3 bucket
s3 = boto3.resource(
    service_name='s3',
    region_name= os.getenv('region_name'),
    aws_secret_access_key= os.getenv('aws_secret_access_key'),
    aws_access_key_id= os.getenv('aws_access_key_id')
)   

#Read all the bucket names and upload the file in test bucket
for bucket in s3.buckets.all():
    if bucket.name == 'test1':
        print('Upload the file to the %s' %(bucket.name))
        s3.Bucket(bucket.name).upload_file(Filename='Dummy_Data.csv', Key='Dummy_Data.csv')

#Read the bucket contents and check if the file exists in the test bucket
for bucket in s3.buckets.all():
    for obj in s3.Bucket(bucket.name).objects.all():
        print('%s bucket has %s file' %(bucket.name, obj.key))
