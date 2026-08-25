def limpiar_registro(registro):
    country = registro.get("country")
    year = registro.get("year")
    gdp = registro.get("gdp")

    if country is None or year is None or gdp is None:
        return None
    try:
        anio = int(year)
        gdp = float(gdp)
    except ValueError:
        return None

    resultado = {
        "pais": country.upper(),
        "anio": anio,
        "pib_per_capita": gdp
    }
    return resultado

def transformar_datos(datos):
    datos_limpios = []

    for registro in datos:
        limpio = limpiar_registro(registro)

        if limpio is None:
            continue

        datos_limpios.append(limpio)
    return datos_limpios