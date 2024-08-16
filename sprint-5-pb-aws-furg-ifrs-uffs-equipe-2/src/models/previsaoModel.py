from marshmallow import Schema, fields

class Previsao(Schema):
    result = fields.Integer(required=True)
