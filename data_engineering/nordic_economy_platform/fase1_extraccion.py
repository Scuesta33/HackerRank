"""
Fase 1: Extraccion
Descarga indicadores economicos de Suecia y Noruega desde la API
publica del Banco Mundial (no requiere clave de acceso) y los
guarda tal cual llegan en data/raw/ (datos "crudos", sin procesar).
"""
import requests
import json
import os

PAISES = "SWE;NOR"  # codigos ISO3 de Suecia y Noruega

INDICADORES = {
    "NY.GDP.PCAP.CD": "pib_per_capita",
    "FP.CPI.TOTL.ZG": "inflacion",
    "SL.UEM.TOTL.ZS": "desempleo",
}


def descargar_indicador(codigo, nombre):
    url = f"https://api.worldbank.org/v2/country/{PAISES}/indicator/{codigo}"
    params = {"format": "json", "per_page": 1000}

    respuesta = requests.get(url, params=params)
    respuesta.raise_for_status()
    datos = respuesta.json()

    os.makedirs("data/raw", exist_ok=True)
    ruta = f"data/raw/{nombre}.json"
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

    num_registros = len(datos[1]) if len(datos) > 1 and datos[1] else 0
    print(f"Guardado {ruta} ({num_registros} registros)")


if __name__ == "__main__":
    for codigo, nombre in INDICADORES.items():
        descargar_indicador(codigo, nombre)
