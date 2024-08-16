from io import StringIO
import csv

"""
    Converte valores de colunas de string em valores numéricos com base em mapeamentos predefinidos.

    Args:
        data (dict): Um dicionário contendo dados a serem processados.

    Returns:
        dict: Um dicionário com os valores das colunas convertidos para números.
"""


def tratarColunasString(data):
    type_of_meal_plan_mapping = {
        'Not Selected': 0,
        'Meal Plan 1': 1,
        'Meal Plan 2': 2,
        'Meal Plan 3': 3
    }

    data["type_of_meal_plan"] = type_of_meal_plan_mapping.get(
        data["type_of_meal_plan"], -1)

    room_type_reserved_mapping = {
        'Room_Type 1': 0,
        'Room_Type 2': 1,
        'Room_Type 3': 2,
        'Room_Type 4': 3,
        'Room_Type 5': 4,
        'Room_Type 6': 5,
        'Room_Type 7': 6
    }

    data["room_type_reserved"] = room_type_reserved_mapping.get(
        data["room_type_reserved"], -1)

    market_segment_type_mapping = {
        'Offline': 0,
        'Online': 1,
        'Complementary': 2,
        'Corporate': 3,
        'Aviation': 4
    }

    data["market_segment_type"] = market_segment_type_mapping.get(
        data["market_segment_type"], -1)

    return data


"""
    Converte um dicionário de dados em formato CSV.

    Args:
        booking (dict): Um dicionário contendo os dados a serem convertidos em formato CSV.

    Returns:
        str: Uma string contendo os dados no formato CSV.
"""
def converteParaCsv(booking):
    csv_output = StringIO()
    csv_writer = csv.DictWriter(csv_output, fieldnames=booking.keys())
    csv_writer.writerow(booking)

    csv_data = csv_output.getvalue()
    return csv_data
