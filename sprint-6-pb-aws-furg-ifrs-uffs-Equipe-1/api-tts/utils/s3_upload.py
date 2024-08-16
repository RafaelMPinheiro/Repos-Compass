import boto3
import text_converter

s3_client = boto3.client("s3", region_name="us-east-1")
bucket = "sprint6-equipe1"


def s3_upload(received_phrase, created_time):

    if received_phrase == "":
        raise Exception("A frase não pode ser vazia")

    created_time_file = f"{created_time}.mp3"

    # Cria o audio a partir da função text_converter
    audio_data = text_converter(received_phrase)

    # Faz o upload do audio no S3
    s3_client.put_object(
        Body=audio_data,
        Bucket=bucket,
        Key=created_time_file
    )

    url = f"https://{bucket}.s3.amazonaws.com/{created_time_file}"

    return url
