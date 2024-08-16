import os
from utils.helper import tratarColunasString
from flask import Blueprint, jsonify, request
from controllers.previsaoController import validarDadosDaReserva
from services.previsaoService import criarPrevisao

predict = Blueprint("predict", __name__)

@predict.route("/", methods=["POST"])
def index():
    data = request.json
    data = tratarColunasString(data)
    reserva = validarDadosDaReserva(data)
    if (reserva == None):
        return {'error': os.environ.get("BAD_REQUEST_MSG")}, 400

    previsao = criarPrevisao(reserva)
    
    if(previsao == None):
        return {'error': os.environ.get("INTERNAL_ERROR_MSG")}, 500

    return jsonify(previsao), 200
