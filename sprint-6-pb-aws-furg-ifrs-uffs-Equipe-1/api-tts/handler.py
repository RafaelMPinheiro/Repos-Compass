from datetime import datetime
import json
import s3_upload
import create_hash
import dynamodb_upload
import dynamodb_get_audio


def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200,
                "body": json.dumps(body),
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/json"
                }}

    return response


def v1_description(event, context):
    body = {
        "message": "TTS api version 1."
    }

    response = {"statusCode": 200,
                "body": json.dumps(body),
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/json"
                }}

    return response


def v2_description(event, context):
    body = {
        "message": "TTS api version 2."
    }

    response = {"statusCode": 200,
                "body": json.dumps(body),
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/json"
                }}

    return response


def v1_tts(event, context):
    try:
        # Recebe o body da requisição
        body = json.loads(event["body"])

        # Recebe a frase e a data de criação
        # phrase = data.get("phrase", "") Usar para puxar a frase do html talvez
        received_phrase = body["phrase"]
        created_time = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

        # Chama a função para o upload do audio no S3
        audio_s3 = s3_upload(received_phrase, created_time)

        response_body = {
            "received_phrase": received_phrase,
            "url_to_audio": audio_s3,
            "created_audio": created_time,
        }

        response = {"statusCode": 200,
                    "body": json.dumps(response_body),
                    "headers": {
                        "Access-Control-Allow-Origin": "*",
                        "Content-Type": "application/json"
                    }}

        return response
    except Exception as e:
        response = {"statusCode": 500,
                    "body": json.dumps(f"Error: {e}"),
                    "headers": {
                        "Access-Control-Allow-Origin": "*",
                        "Content-Type": "application/json"
                    }}
        return response


def v2_tts(event, context):
    try:
        # Recebe o body da requisição
        body = json.loads(event["body"])

        # Recebe a frase e a data de criação
        # phrase = data.get("phrase", "") Usar para puxar a frase do html talvez
        received_phrase = body["phrase"]
        created_time = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

        # Chama a função para o upload do audio no S3
        audio_s3 = s3_upload(received_phrase, created_time)

        # Cria o hash da frase
        hash_phrase = create_hash(received_phrase)

        # Chama a função para o upload do audio no DynamoDB
        dynamodb_upload(received_phrase, audio_s3, hash_phrase)

        response_body = {
            "received_phrase": received_phrase,
            "url_to_audio": audio_s3,
            "created_audio": created_time,
            "unique_id": hash_phrase
        }

        response = {"statusCode": 200,
                    "body": json.dumps(response_body),
                    "headers": {
                        "Access-Control-Allow-Origin": "*",
                        "Content-Type": "application/json"
                    }}

        return response
    except Exception as e:
        response = {"statusCode": 500,
                    "body": json.dumps(f"Error: {e}"),
                    "headers": {
                        "Access-Control-Allow-Origin": "*",
                        "Content-Type": "application/json"
                    }}

        return response


def v3_tts(event, context):
    try:
        # Recebe o body da requisição
        body = json.loads(event["body"])

        # Recebe a frase
        # phrase = data.get("phrase", "") Usar para puxar a frase do HTML talvez
        received_phrase = body["phrase"]

        # Cria o hash da frase
        hash_phrase = create_hash(received_phrase)

        item_dynamo = dynamodb_get_audio(hash_phrase)

        # Verifica se o hash já existe no DynamoDB
        if item_dynamo:
            response_body = {
                "received_phrase": received_phrase,
                "url_to_audio": item_dynamo["url"],
                "created_audio": item_dynamo["created_audio"],
                "unique_id": hash_phrase
            }
        else:
            # Caso o hash não exista, faz a geração do áudio e atualiza o DynamoDB
            created_time = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

            audio_s3 = s3_upload(received_phrase, created_time)

            # Chama a função para o upload do áudio no DynamoDB
            dynamodb_upload(received_phrase, audio_s3, hash_phrase)

            response_body = {
                "received_phrase": received_phrase,
                "url_to_audio": audio_s3,
                "created_audio": created_time,
                "unique_id": hash_phrase
            }

        response = {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            }
        }

        return response

    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps(f"Error: {e}"),
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            }
        }

        return response
