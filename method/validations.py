from datetime import datetime as dt
from googleapiclient.errors import HttpError  
from .generateBlocksFunction import parse_busy_periods

def _max_time_str(t1, t2):
    """
    Devuelve la mayor de dos horas 'HH:MM' como string.
    """
    d1 = dt.strptime(t1, "%H:%M")
    d2 = dt.strptime(t2, "%H:%M")
    return (d1 if d1 >= d2 else d2).strftime("%H:%M")


def _min_time_str(t1, t2):
    """
    Devuelve la menor de dos horas 'HH:MM' como string.
    """
    d1 = dt.strptime(t1, "%H:%M")
    d2 = dt.strptime(t2, "%H:%M")
    return (d1 if d1 <= d2 else d2).strftime("%H:%M")




def get_busy_periods_for_day(service, calendar_id, date_str, start_time_str, end_time_str, tz="America/Bogota"):
    """
    Consulta a Google Calendar los rangos ocupados (busy) para un día y horario dado.
    Retorna lista de (start_dt, end_dt) sin tzinfo.
    """
    # offset fijo -05:00 (Colombia)
    time_min = f"{date_str}T{start_time_str}:00-05:00"
    time_max = f"{date_str}T{end_time_str}:00-05:00"

    body = {
        "timeMin": time_min,
        "timeMax": time_max,
        "timeZone": tz,
        "items": [{"id": calendar_id}],
    }

    try:
        response = service.freebusy().query(body=body).execute()
    except HttpError as e:
        print("Error al llamar a freebusy:")
        print("Body enviado:", body)
        print("Detalle:", e)
        raise

    busy_periods = parse_busy_periods(response, calendar_id)
    return busy_periods