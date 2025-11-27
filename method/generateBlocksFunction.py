from datetime import datetime as dt, timedelta


def create_time_slots(date_str, start_str, end_str, duration_minutes=30):
    """
    Genera bloques de duración fija dentro del rango [start, end).

    date_str: 'YYYY-MM-DD'
    start_str / end_str: 'HH:MM'
    duration_minutes: duración de cada bloque en minutos (ej. 30)
    """
    start_dt = dt.strptime(f"{date_str} {start_str}", "%Y-%m-%d %H:%M")
    end_dt = dt.strptime(f"{date_str} {end_str}", "%Y-%m-%d %H:%M")

    if end_dt <= start_dt:
        raise ValueError("La hora final debe ser mayor que la hora inicial.")

    slots = []
    current = start_dt
    delta = timedelta(minutes=duration_minutes)

    while current < end_dt:
        slot_end = current + delta
        if slot_end > end_dt:
            break
        slots.append((current, slot_end))
        current = slot_end

    return slots


def create_event(service, calendar_id, summary, start_dt, end_dt, tz="America/Bogota", color_id=None):
    """
    Crea un solo evento en Google Calendar usando el service ya autenticado.

    Si color_id está definido, asigna ese color al evento.
    """
    event_body = {
        'summary': summary,
        'start': {
            'dateTime': start_dt.isoformat(),
            'timeZone': tz,
        },
        'end': {
            'dateTime': end_dt.isoformat(),
            'timeZone': tz,
        },
    }

    if color_id is not None:
        event_body['colorId'] = str(color_id)

    event = service.events().insert(
        calendarId=calendar_id,
        body=event_body
    ).execute()

    print(f"Evento creado {start_dt.strftime('%Y-%m-%d %H:%M')} - {end_dt.strftime('%H:%M')}: {event.get('htmlLink')}")


def _overlaps(a_start, a_end, b_start, b_end):
    """
    Retorna True si el rango A se cruza con el rango B.
    """
    return a_start < b_end and b_start < a_end


def filter_free_slots(slots, busy_periods):
    """
    Recibe
        slots: lista de tuplas (start_dt, end_dt)
        busy_periods: lista de tuplas (busy_start, busy_end)
    Retorna solo los slots que NO se cruzan con ningún busy_period.
    """
    free = []
    for start_dt, end_dt in slots:
        hay_conflicto = any(
            _overlaps(start_dt, end_dt, b_start, b_end)
            for b_start, b_end in busy_periods
        )
        if not hay_conflicto:
            free.append((start_dt, end_dt))
    return free


def parse_busy_periods(freebusy_response, calendar_id):
    """
    Convierte la respuesta de freebusy en una lista de (start_dt, end_dt)
    sin tzinfo para poder compararla con los slots.

    freebusy_response: resultado de service.freebusy().query(...).execute()
    """
    busy_ranges = freebusy_response.get("calendars", {}).get(calendar_id, {}).get("busy", [])
    result = []

    for item in busy_ranges:
        start = item["start"]
        end = item["end"]

        
        if start.endswith("Z"):
            start = start.replace("Z", "+00:00")
        if end.endswith("Z"):
            end = end.replace("Z", "+00:00")

        start_dt = dt.fromisoformat(start).replace(tzinfo=None)
        end_dt = dt.fromisoformat(end).replace(tzinfo=None)
        result.append((start_dt, end_dt))

    return result
