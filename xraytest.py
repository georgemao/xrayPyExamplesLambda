import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

patch(['boto3'])   

# Create an S3 client
s3 = boto3.client('s3')

xray_recorder.configure(
    sampling=False,
    context_missing='LOG_ERROR'
    #plugins=('EC2Plugin', 'ECSPlugin', 'ElasticBeanstalkPlugin'),
    #daemon_address='127.0.0.1:3000',
    #dynamic_naming='*mysite.com*'
)


def handler(event, context):
    # Lambda functions only need to begin and end subsegments. Lambda emits a segment as the root.
    subsegment = xray_recorder.begin_subsegment('subsegment_name')

    # Call S3 to list current buckets
    response = s3.list_buckets()

    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Print out the bucket list
    print("Bucket List: %s" % buckets)

    xray_recorder.end_subsegment()

    return { "body" : "hello from Python" }