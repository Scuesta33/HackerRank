"""
Fase 2: Almacenamiento inicial
Lee los JSON crudos de data/raw/, los aplana a una tabla limpia
(formato tidy) y los guarda en data/processed/ como CSV.
"""
import json
import os
import pandas as pd

INDICADORES = ["pib_per_capita", "inflacion", "desempleo"]


def cargar_indicador(nombre_archivo):
    ruta = f"data/raw/{nombre_archivo}.json"
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)
    return datos[1]  # datos[0] son metadatos, datos[1] es la lista de registros


def aplanar_registros(registros, nombre_indicador):
    filas = []
    for r in registros:
        filas.append({
            "pais": r["country"]["value"],
            "codigo_pais": r["countryiso3code"],
            "anio": int(r["date"]),
            "indicador": nombre_indicador,
            "valor": r["value"],
        })
    return filas


def main():
    todas_las_filas = []
    for nombre in INDICADORES:
        registros = cargar_indicador(nombre)
        todas_las_filas.extend(aplanar_registros(registros, nombre))

    df = pd.DataFrame(todas_las_filas)

    antes = len(df)
    df = df.dropna(subset=["valor"])
    print(f"Filas sin valor eliminadas: {antes - len(df)}")

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/economia_nordica.csv", index=False)
    print(f"Guardado data/processed/economia_nordica.csv ({len(df)} filas)")
    print(df.head(10))


if __name__ == "__main__":
    main()
