import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table_name = "sprint6-equipe1"


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
