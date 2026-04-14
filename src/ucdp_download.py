import os
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

DATA_URL = "https://ucdpapi.pcr.uu.se/api/gedevents/25.1"


def obtener_token(token: str | None) -> str:
    if not token:
        raise RuntimeError(
            "Falta credencial. Define UCDP_TOKEN en un archivo .env"
        )
    return token


def descargar_eventos(token: str) -> pd.DataFrame:
    headers = {"x-ucdp-access-token": token}
    params_base = {
        "StartDate": "2024-10-01",
        "EndDate": "2025-01-31",
        "pageSize": 1000,
    }

    eventos_ucrania: list[dict] = []
    pagina = 0

    while True:
        params = params_base | {"page": pagina}
        respuesta = requests.get(DATA_URL, headers=headers, params=params, timeout=30)

        if respuesta.status_code == 401:
            raise RuntimeError("Token de UCDP invalido o no autorizado.")
        if respuesta.status_code != 200:
            raise RuntimeError(
                f"Error al descargar datos de UCDP: {respuesta.status_code} - {respuesta.text}"
            )

        payload = respuesta.json()
        eventos = payload.get("Result", [])

        if not isinstance(eventos, list):
            raise RuntimeError("Formato inesperado en la respuesta de UCDP: 'Result' no es una lista.")

        if not eventos:
            break

        eventos_ucrania.extend(
            evento for evento in eventos if evento.get("country") == "Ukraine"
        )
        print(f"Pagina {pagina} procesada. Incidentes acumulados: {len(eventos_ucrania)}")
        pagina += 1

    return pd.DataFrame(eventos_ucrania)


def preparar_dataset(df: pd.DataFrame) -> pd.DataFrame:
    columnas_clave = [
        "id",
        "date_start",
        "date_end",
        "latitude",
        "longitude",
        "type_of_violence",
        "best",
    ]

    df_modelo = df.reindex(columns=columnas_clave).copy()
    df_modelo["latitude"] = pd.to_numeric(df_modelo["latitude"], errors="coerce")
    df_modelo["longitude"] = pd.to_numeric(df_modelo["longitude"], errors="coerce")
    df_modelo = df_modelo.dropna(subset=["latitude", "longitude"])

    return df_modelo


def main() -> None:
    load_dotenv()

    token = obtener_token(os.getenv("UCDP_TOKEN"))

    print("Descargando datos de UCDP para Ucrania (Oct 2024 - Ene 2025)")
    df = descargar_eventos(token)
    if df.empty:
        print("No se devolvieron registros para el rango solicitado.")
        return

    df_modelo = preparar_dataset(df)

    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "ucdp_ukraine_oct2024_jan2025.csv"
    df_modelo.to_csv(output_file, index=False, encoding="utf-8")

    print("Datos descargados con exito.")
    print(f"Archivo generado: {output_file}")
    print(df_modelo.head())


if __name__ == "__main__":
    main()