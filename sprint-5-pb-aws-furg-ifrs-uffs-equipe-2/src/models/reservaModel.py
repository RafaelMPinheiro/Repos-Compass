from marshmallow import Schema, fields

class Reserva(Schema):
    no_of_adults = fields.Integer(required=True)
    no_of_children = fields.Integer(required=True)
    no_of_weekend_nights = fields.Integer(required=True)
    no_of_week_nights = fields.Integer(required=True)
    type_of_meal_plan = fields.Integer(required=True)
    required_car_parking_space = fields.Integer(required=True)
    room_type_reserved = fields.Integer(required=True)
    lead_time = fields.Integer(required=True)
    arrival_year = fields.Integer(required=True)
    arrival_month = fields.Integer(required=True)
    arrival_date = fields.Integer(required=True)
    market_segment_type = fields.Integer(required=True)
    repeated_guest = fields.Integer(required=True)
    no_of_special_requests = fields.Integer(required=True)
    
