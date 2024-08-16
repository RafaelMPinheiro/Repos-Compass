import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table_name = "sprint6-equipe1"


def dynamodb_upload(received_phrase, url_s3, hash_phrase):
    table = dynamodb.Table(table_name)

    # Faz o upload do audio no DynamoDB
    table.put_item(Item={
        "id": hash_phrase,
        "phrase": received_phrase,
        "url": url_s3,
        "created_audio": datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    })

def dynamodb_get_audio(hash_phrase):
    table = dynamodb.Table(table_name)

    # Verifica se o hash já existe no DynamoDB
    response = table.get_item(Key={
        "id": hash_phrase
    })

    if "Item" in response:
        return response["Item"]
    else:
        return None