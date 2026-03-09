import requests
import socket
from datetime import datetime, timezone

API_URL = "http://127.0.0.1:8000/log"


def enviar_log(dominio):

    data = {
        "usuario": socket.gethostname(),
        "dominio": dominio,
        "fecha_cliente": datetime.now(timezone.utc).isoformat()
    }

    try:

        response = requests.post(API_URL, json=data, timeout=3)

        if response.status_code != 200:

            print("API error:", response.status_code)

    except requests.exceptions.RequestException as e:

        print("No se pudo enviar log:", e)