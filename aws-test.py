import boto3

# Your AWS Access Key ID and Secret Access Key
aws_access_key_id = 'AKIAWY56YWJJ6Z5VR6FN'
aws_secret_access_key = '99UWHW8OMxJHxPqDNABQ9nMdT1Klc8/oA4z1OVd9'

# Optionally, you can specify a region
region_name = 'us-east-2' # Example region

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Use the session to create a client for the S3 service
s3 = session.client('s3')

# List all S3 buckets
response = s3.list_buckets()

# Print the bucket names
print("S3 Buckets:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")
