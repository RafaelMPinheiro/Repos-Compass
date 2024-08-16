import boto3

polly_client = boto3.client("polly", region_name="us-east-1")
voicePolly = "Camila"


def text_converter(text):
    # Converte o texto em fala
    response = polly_client.synthesize_speech(
        VoiceId=voicePolly,
        Text=text,
        OutputFormat="mp3",
        LanguageCode="pt-BR"
    )

    return response["AudioStream"].read()
