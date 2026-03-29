import os
from pathlib import Path
import pandas as pd
import requests
from dotenv import load_dotenv

TOKEN_URL = "https://acleddata.com/oauth/token"
DATA_URL = "https://acleddata.com/api/acled/read"


def obtener_token(email: str, password: str) -> str:
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "username": email,
        "password": password,
        "grant_type": "password",
        "client_id": "acled",
    }

    respuesta = requests.post(TOKEN_URL, headers=headers, data=data, timeout=30)
    if respuesta.status_code != 200:
        raise RuntimeError(f"Error de credenciales: {respuesta.status_code} - {respuesta.text}")

    payload = respuesta.json()
    token = payload.get("access_token")
    if not token:
        raise RuntimeError("No se recibió access_token en la respuesta de ACLED.")
    return token


def descargar_eventos(token: str) -> pd.DataFrame:
    params = {
        "_format": "json",
        "country": "Ukraine",
        "event_date": "2024-10-01|2025-01-31",
        "event_date_where": "BETWEEN",
        "limit": 0,
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    respuesta = requests.get(DATA_URL, params=params, headers=headers, timeout=60)
    if respuesta.status_code != 200:
        raise RuntimeError(f"Error al descargar datos: {respuesta.status_code} - {respuesta.text}")

    payload = respuesta.json()
    data = payload.get("data", [])
    if not isinstance(data, list):
        raise RuntimeError("Formato inesperado en la respuesta de ACLED: 'data' no es una lista.")

    return pd.DataFrame(data)


def preparar_dataset(df: pd.DataFrame) -> pd.DataFrame:
    columnas_clave = [
        "event_date",
        "event_type",
        "sub_event_type",
        "latitude",
        "longitude",
        "fatalities",
    ]

    # Reindex evita errores si alguna columna no viene en la respuesta.
    df_modelo = df.reindex(columns=columnas_clave).copy()

    # Limpieza mínima para evitar fallas en modelado geoespacial.
    df_modelo["latitude"] = pd.to_numeric(df_modelo["latitude"], errors="coerce")
    df_modelo["longitude"] = pd.to_numeric(df_modelo["longitude"], errors="coerce")
    df_modelo = df_modelo.dropna(subset=["latitude", "longitude"])

    return df_modelo


def main() -> None:
    load_dotenv()

    email = os.getenv("ACLED_EMAIL")
    password = os.getenv("ACLED_PASSWORD")

    if not email or not password:
        raise RuntimeError(
            "Faltan credenciales. Define ACLED_EMAIL y ACLED_PASSWORD en un archivo .env"
        )

    print("Validando credenciales de ACLED")
    token = obtener_token(email, password)
    print("Token de acceso concedido.")

    print("Descargando datos de eventos de ACLED para Ucrania (Oct 2024 - Ene 2025)")
    df = descargar_eventos(token)
    if df.empty:
        print("No se devolvieron registros para el rango solicitado.")
        return

    df_modelo = preparar_dataset(df)

    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "acled_ukraine_oct2024_jan2025.csv"
    df_modelo.to_csv(output_file, index=False, encoding="utf-8")

    print("Datos descargados con éxito.")
    print(f"Archivo generado: {output_file}")
    print(df_modelo.head())


if __name__ == "__main__":
    main()
