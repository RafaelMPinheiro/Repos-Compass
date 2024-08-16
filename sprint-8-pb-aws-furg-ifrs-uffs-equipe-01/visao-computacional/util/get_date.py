import boto3

s3 = boto3.client('s3', region_name="us-east-1")


def get_date(bucket, imageName):
    try:
        response = s3.head_object(Bucket=bucket, Key=imageName)
        date = response['LastModified'].strftime('%d-%m-%Y %H:%M:%S')
        return date
    except Exception as e:
        raise e
