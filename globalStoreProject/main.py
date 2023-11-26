import os 
import sys
import argparse
from utility.AWS.download_from_S3 import *
from utility.AWS.s3ClientProvider import *
from utility.logging_util.loggingConfig import *
from config import config

from utility.encryptDecrypt.encrypt_decrypt import encrypt , decrypt



def main(bucket_name):
    print(os.path.join(os.getcwd(),"utility/AWS"))
   # sys.path.insert(0, os.path.dirname(
    logger.info("Running main function Step 1. Decrypting AWS keys ")
    aws_access_key= decrypt(config.aws_access_key)
    aws_secret_access_key = decrypt(config.aws_secret_key)
    logger.info("Running main function step 1 completed successfully ")
    logger.info("Running main function Step 2. Connecting to S3 Client bucket {0}".format(bucket_name))
    s3Client = s3ClientProvider( aws_access_key, aws_secret_access_key)
    s3ClientObj = s3Client.get_client()
    logger.info("Running main function Step 2. Connected to s3 Client and Bucket Successfully {0}"
                .format(s3ClientObj.buckets.all()))
    
"""
    Testing S3 Bucket
    for bucket in s3ClientObj.buckets.all():
        for obj in s3ClientObj.Bucket(bucket.name).objects.all():
            print('%s bucket has %s file' %(bucket.name, obj.key))
""" 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Database engineering project")
    parser.add_argument("s3SourceBucketName", help="Database configuration", type=str)
    args = parser.parse_args()    
    main(args.s3SourceBucketName)