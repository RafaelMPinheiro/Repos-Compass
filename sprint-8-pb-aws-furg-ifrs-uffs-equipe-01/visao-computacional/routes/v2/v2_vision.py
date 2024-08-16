import json
import boto3
from util.get_date import get_date
from util.detect_faces import detect_faces

rekognition = boto3.client("rekognition", region_name="us-east-1")

def v2_vision (event, context):
    try:

        body = json.loads(event["body"])
        bucket = body['bucket']
        imageName = body['imageName']

        faces  = detect_faces(imageName, bucket, rekognition)
        url_to_image = f"https://{bucket}.s3.amazonaws.com/{imageName}"
        created_image = get_date(bucket, imageName)

        response_body = {
            "url_to_image": url_to_image,
            "created_image": created_image,
            "faces": faces
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(response_body)
        }
        print(response)
    except Exception as e:
        error_message = str(e)
        print("Error:", error_message)
        if error_message == "An error occurred (InvalidImageFormatException) when calling the DetectFaces operation: Request has invalid image format":
            response ={
                "statusCode": 400,
                "body": json.dumps({"message": "A imagem possui um formato inválido, o rekognition aceita arquivos do tipo png e jpeg, verifique o arquivo e tente novamente."})
            }
        elif error_message == "An error occurred (InvalidS3ObjectException) when calling the DetectFaces operation: Unable to get object metadata from S3. Check object key, region and/or access permissions.":
            response = {
                "statusCode": 404,
                "body": json.dumps({"message": "Arquivo ou bucket não encontrado, verifique o nome do arquivo e tente novamente."})
            }
        elif error_message == "'bucket'" or error_message == "'imageName'":
            response = {
                "statusCode": 400,
                "body": json.dumps({"message": "Parâmetros errados, por favor informe o 'bucket' e 'imageName' na solicitação."})
            }
        else:
            response = {
                "statusCode": 500,
                "body": json.dumps({"message": error_message})
            }
    return response
