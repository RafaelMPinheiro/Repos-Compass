from sagemaker.serializers import CSVSerializer
from models.reservaModel import Reserva
from models.previsaoModel import Previsao
from utils.helper import converteParaCsv
import sagemaker
import boto3
import os


"""
Cria uma previsão com base em uma reserva usando um modelo treinado no AWS SageMaker.

Args:
        reserva (Reserva): Uma instância da classe Reserva contendo dados da reserva.

Returns:
        previsao (Previsao) / None: Uma instância da classe previsão no formato {"result": previsao}, se tiver erro retorna None.
"""


def criarPrevisao(reserva) -> Reserva:
    try:
        AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
        AWS_SESSION_TOKEN = os.environ.get("AWS_SESSION_TOKEN")
        REGION_NAME = os.environ.get("REGION_NAME")
        ENDPOINT = os.environ.get("ENDPOINT")

        boto_session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                     aws_session_token=AWS_SESSION_TOKEN,
                                     region_name=REGION_NAME)

        session = sagemaker.Session(boto_session=boto_session)
        endpoint = ENDPOINT
        previsor = sagemaker.predictor.Predictor(
            endpoint_name=endpoint, sagemaker_session=session)

        csv_data = converteParaCsv(reserva)

        previsor.serializer = CSVSerializer()
        previsao = previsor.predict(csv_data)
        previsao = previsao.decode("utf-8")

        previsao = float(previsao)
        previsao = int(previsao)

        previsao = Previsao().load({"result": previsao})

        return previsao
    except Exception as e:
        return None
