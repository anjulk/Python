import boto3

class s3ClientProvider:
    def __init__(self, aws_access_key=None, aws_secret_access_key=None):
        self.aws_access_key = aws_access_key
        self.aws_secret_access_key = aws_secret_access_key
        try:
            self.s3_client = boto3.resource(
                    service_name='s3',
                    region_name= 'us-east-2',
                    aws_secret_access_key= self.aws_secret_access_key,
                    aws_access_key_id= self.aws_access_key
                )
           
        except Exception as SessionError:
            print('Session Error: %s' % SessionError)    
    def get_client(self):
        return self.s3_client