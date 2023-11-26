import os 
import sys
import argparse
from Extract import dataExtract
from TransformLoad import TransformLoad



def main(bucket_name):
    dataExtract(bucket_name)
    TransformLoad()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Database engineering project")
    parser.add_argument("s3SourceBucketName", help="Database configuration", type=str)
    args = parser.parse_args()    
    main(args.s3SourceBucketName)