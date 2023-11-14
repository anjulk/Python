import boto3
import pandas as pd
import os
import sqlalchemy as sa

# Creditentials are store in environment variables

#Connect to AWS S3 bucket
s3 = boto3.resource(
    service_name='s3',
    region_name= os.getenv('region_name'),
    aws_secret_access_key= os.getenv('aws_secret_access_key'),
    aws_access_key_id= os.getenv('aws_access_key_id')
)   

#Download the text file to be used for uploading in MySql database
for bucket in s3.buckets.all():
    for obj in s3.Bucket(bucket.name).objects.all():
        print('%s bucket has %s file' %(bucket.name, obj.key))
        if '.txt' in obj.key:
            bucket_name = bucket.name 
            filename = obj.key
            break

#Get all the data from the S3 bucket object
file_data = s3.Bucket(bucket_name).Object(filename).get()

#Read the data into the pandas dataframe and print all the column names
file_data_pd = pd.read_csv(file_data['Body'], index_col=0, sep='\t')
print(file_data_pd.columns)

#drop the garbage column name
file_data_pd.drop('记录数', inplace=True, axis=1)
print(file_data_pd.columns)

#Create an instance  of mysql database
engine = sa.create_engine('mysql+mysqlconnector://root:password@[localhost]/database', echo=False)

#Upload the file in the database and table Global_Superstore
try:
    file_data_pd.to_sql(name='Global_Superstore', con=engine, if_exists = 'replace', index=False)
except Exception as e:
    print(e)