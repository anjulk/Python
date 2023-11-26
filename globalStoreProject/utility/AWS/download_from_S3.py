import boto3
import traceback
import os
import sys
from utility.logging_util.loggingConfig import *





class S3FileDownloader:
    def __init__(self,s3_client, s3_bucket_name, s3_local_directory):
        self.s3_client = s3_client
        self.s3_bucket_name = s3_bucket_name
        self.s3_local_directory = s3_local_directory
        
    def s3_download_file(self, list_files):
        logger.info("Running download from {0} bucket containing files {1}".format(self.s3_bucket_name, list_files))

def loggingConfig():
    filePath = os.path.join(os.getcwd(),"utility/logging_util/")
    sys.path.insert(0,filePath)
    logger.error("Got this error : %s","hellp")

