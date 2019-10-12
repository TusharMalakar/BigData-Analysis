import boto3
from pprint import pprint
from pymongo import MongoClient
# from google.cloud import storage
# from google.cloud import bigquery
# from google.oauth2 import service_account

###################################################################
# # google-cloud-storage
#
# rawPath = r"C:\Users\tusha\AppData\Roaming\gcloud\key.json"
# client = storage.Client.from_service_account_json(rawPath)
#
# bucket_name = 'hunterbucker'
# bucket = client.get_bucket(bucket_name)
#
#
# def upload_blob(file_name):
#     """Downloads a blob from the bucket."""
#     blob = bucket.blob(file_name)
#     with open('requirements.txt', 'rb') as my_file:
#         blob.upload_from_file(my_file)
#
#
# def download_blob(file_name):
#     """Downloads a blob from the bucket."""
#     blob = bucket.blob(file_name)
#     blob.download_to_filename(file_name)
#
#
# # upload_blob("requirements.txt")
# # download_blob("test.txt")

####################################################################
# run = "dont run"
#
# if run is None:
client = MongoClient(
    "mongodb+srv://tushar:<PASSWORD>@cluster0-d2vx4.mongodb.net/test?retryWrites=true&w=majority")
database = client.BlockChain
username = "user3"
record = database.users.find({"username": username})
if record is not None:
    print("Database is connected")
    pprint(record.__dict__)
else:
    print("None")

# client = MongoClient("mongodb://capstone:<PASSWORD>@cluster0-shard-00-00-we2hu.mongodb.net:27017,cluster0-shard-00-01-we2hu.mongodb.net:27017,cluster0-shard-00-02-we2hu.mongodb.net:27017/client_example?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
# database = client.hunter_collab
# username = "testuser99@myhunter.cuny.edu"
# record = database.users.find({"username": username})
#
# cursor = database.users.find({"username":username})
# for document in cursor:
#     pprint(document)

###################################################################

# myDB = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="mySql123"
# )
#
# print(mysql)

###############################################################
# Amazon s3 => sss => Simple Storage Service
# https://realpython.com/python-boto3-aws-s3/
# https://docs.aws.amazon.com/code-samples/latest/catalog/code-catalog-python-example_code-s3.html
# https://s3.console.aws.amazon.com/s3/buckets/simplestorageservicesbucket/pro/?region=us-east-2&tab=overview

"""
$ aws configure
        AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
        AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
        Default region name [None]: us-west-2
        Default output format [None]: json
"""
"""
    Client: low-level service access
    Resource: higher-level object-oriented service access
"""
run = "dont run"
if run is None:
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')

    """GET REQUEST : 
    
        # from botocore.exceptions import ClientError
        # import logging, boto3
        
        def get_object(bucket_name, object_name):
        # Retrieve an object from an Amazon S3 bucket
        # 
        # :param bucket_name: string
        # :param object_name: string
        # :return: botocore.response.StreamingBody object. If error, return None.
        
    
        # Retrieve the object
        s3 = boto3.client('s3')
        try:
            response = s3.get_object(Bucket=bucket_name, Key=object_name)
        except ClientError as e:
            # AllAccessDisabled error == bucket or object not found
            logging.error(e)
            return None
        # Return an open StreamingBody object
        return response['Body']
        
    """

    """Create Bucket
        s3_resource.create_bucket(Bucket=YOUR_BUCKET_NAME,CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
    """
    # s3_resource.create_bucket(Bucket='YOUR_BUCKET_NAME',CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})

    """Upload File : Before uploading change filename as "username.extension"
        # os.rename('test.txt', 'username.txt')
        s3_resource.Bucket(first_bucket_name).upload_file(Filename=first_file_name, Key=first_file_name)
    """
    s3_resource.Object('simplestorageservicesbucket', 'profilePicture/README.md').upload_file(Filename='README.md')

    """Download file
        s3_resource.Object(first_bucket_name, first_file_name).download_file(f'/tmp/{first_file_name}')
    """
    s3_resource.Object('simplestorageservicesbucket', 'README.md').download_file('README.md')

    """
        s3_resource.Object(first_bucket_name, first_file_name).delete()
    """
    # s3_resource.Object('simplestorageservicesbucket', 'test').delete()

    """Find all the objects inside a bucket
        for key in s3_client.list_objects(Bucket='simplestorageservicesbucket')['Contents']:
            print(key['Key'])
    """
    for key in s3_client.list_objects(Bucket='simplestorageservicesbucket')['Contents']:
        print(key['Key'])

    print("s3 connection established")
###########################################################
