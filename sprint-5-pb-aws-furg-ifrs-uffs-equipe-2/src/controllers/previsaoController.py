import os
from models.reservaModel import Reserva
from models.previsaoModel import Previsao

"""
Essa função recebe o corpo do objeto post, e valida os tipos que foram inseridos através da lib marshmallow, retornando uma instância
da classe Reserva.

Args:
    data (dict): Um dicionário contendo os dados de reserva a serem validados.
Returns:
        Reserva / None: Retorna uma instância Reserva se os dados forem válidos, caso contrário,
        retorna None.
"""
def validarDadosDaReserva(data) -> Reserva:
    try:
        reserva = Reserva()
        errors = reserva.validate(data)
        if errors:
            raise TypeError(os.environ.get("TYPE_ERROR_MESSAGE"))
    except Exception:
        return None
    else:
        return reserva.load(data)