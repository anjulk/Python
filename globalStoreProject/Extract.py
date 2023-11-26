import os 
import sys
import argparse
from utility.AWS.download_from_S3 import *
from utility.AWS.s3ClientProvider import *
from utility.logging_util.loggingConfig import *
from utility.sqlDatabase.sqlDatabaseRawUpload import *
from config import config

from utility.encryptDecrypt.encrypt_decrypt import encrypt , decrypt



def dataExtract(bucket_name):
    
    
    
    logger.info("Running main function Step 1. Decrypting AWS keys ")
    aws_access_key= decrypt(config.aws_access_key)
    aws_secret_access_key = decrypt(config.aws_secret_key)
    logger.info("Running main function step 1 completed successfully ")
    
    logger.info("Running main function Step 2. Connecting to S3 Client bucket {0}".format(bucket_name))
    s3Client = s3ClientProvider( aws_access_key, aws_secret_access_key)
    s3ClientObj = s3Client.get_client()
    logger.info("Running main function Step 2. Connected to s3 Client and Bucket Successfully {0}"
                .format(s3ClientObj.buckets.all()))
    
    logger.info("Running main function Step 3. Downloading file from s3 bucket {0}".format(bucket_name))
    s3fileDownloadObj = S3FileDownloader(s3ClientObj, bucket_name)
    fileObj = s3fileDownloadObj.s3_download_file()
    logger.info("Running main function Step 3. Downloading is complete and file can be accessed file {0}\
                and Type is {1}"
                .format(fileObj, type(fileObj)))    
    
    logger.info("Running main function Step 4. Connecting to SQL database {0}".format(config.database_name) )
    mysqlObj = mySQLWrapper()
    (connection, engine) = mysqlObj.get_mySQL_Connection()
    
    logger.info("Running main function Step 4. Connected to SQL database {0} and ENGINE {1}"\
        .format(connection , engine) )

    logger.info("Running main function Step 5. upload raw file to SQL database {0}".format(config.database_name) )
    mysqlObj.upload_to_myqlServer(connection, engine, fileObj)

    logger.info("Running main function Step 5. upload complete {0} ".format(config.database_name) )
    
    
    
    
    curr = connection.cursor()
    curr.execute('SELECT * FROM  Global_Superstore LIMIT 10')
    print(curr.fetchall())
    curr.close()
    connection.close()
    
"""
    Testing S3 Bucket
    for bucket in s3ClientObj.buckets.all():
        for obj in s3ClientObj.Bucket(bucket.name).objects.all():
            print('%s bucket has %s file' %(bucket.name, obj.key))
""" 


