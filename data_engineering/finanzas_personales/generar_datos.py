"""
Genera un dataset "sucio" de gastos personales para practicar limpieza de datos.
Ejecutalo una vez: python generar_datos.py
Crea data/gastos.csv con problemas típicos de datos reales:
- categorías con mayúsculas/minúsculas inconsistentes y espacios extra
- fechas en dos formatos distintos (YYYY-MM-DD y DD/MM/YYYY)
- montos con símbolo "$" como texto
- valores de monto faltantes
- filas duplicadas
"""
import random
import csv

random.seed(42)

categorias = ["Comida", "Transporte", "Ocio", "Salud", "Vivienda", "Educacion", "Otros"]
variantes_categoria = {
    "Comida": ["Comida", "comida", "COMIDA", " Comida "],
    "Transporte": ["Transporte", "transporte", "Transporte "],
    "Ocio": ["Ocio", "ocio", " Ocio"],
    "Salud": ["Salud", "salud"],
    "Vivienda": ["Vivienda", "vivienda"],
    "Educacion": ["Educacion", "educacion", "EDUCACION"],
    "Otros": ["Otros", "otros"],
}
descripciones = {
    "Comida": ["Supermercado", "Restaurante", "Delivery", "Cafeteria"],
    "Transporte": ["Uber", "Gasolina", "Transporte publico", "Taxi"],
    "Ocio": ["Cine", "Streaming", "Videojuego", "Concierto"],
    "Salud": ["Farmacia", "Consulta medica", "Gimnasio"],
    "Vivienda": ["Alquiler", "Luz", "Agua", "Internet"],
    "Educacion": ["Curso online", "Libros", "Matricula"],
    "Otros": ["Regalo", "Varios", "Suscripcion"],
}
metodos_pago = ["Tarjeta", "Efectivo", "Transferencia"]

rango_monto = {
    "Comida": (5, 60),
    "Transporte": (3, 40),
    "Ocio": (8, 80),
    "Salud": (10, 120),
    "Vivienda": (50, 600),
    "Educacion": (15, 300),
    "Otros": (5, 100),
}

filas = []
for mes in [1, 2, 3]:
    for _ in range(50):
        cat = random.choice(categorias)
        dia = random.randint(1, 28)
        monto_min, monto_max = rango_monto[cat]
        monto = round(random.uniform(monto_min, monto_max), 2)

        # formato de fecha inconsistente
        if random.random() < 0.3:
            fecha = f"{dia:02d}/{mes:02d}/2026"
        else:
            fecha = f"2026-{mes:02d}-{dia:02d}"

        # categoria con variantes de formato
        categoria_texto = random.choice(variantes_categoria[cat])

        # monto a veces como texto con simbolo $
        if random.random() < 0.2:
            monto_texto = f"${monto}"
        else:
            monto_texto = str(monto)

        # a veces el monto falta
        if random.random() < 0.05:
            monto_texto = ""

        fila = {
            "fecha": fecha,
            "categoria": categoria_texto,
            "descripcion": random.choice(descripciones[cat]),
            "monto": monto_texto,
            "metodo_pago": random.choice(metodos_pago),
        }
        filas.append(fila)

# insertar duplicados a proposito
for _ in range(8):
    filas.append(random.choice(filas).copy())

random.shuffle(filas)

with open("data/gastos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["fecha", "categoria", "descripcion", "monto", "metodo_pago"])
    writer.writeheader()
    writer.writerows(filas)

print(f"Generadas {len(filas)} filas en data/gastos.csv")
