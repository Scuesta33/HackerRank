import pandas as pd
import sqlite3

# ============================================================
# PASO 1: Cargar los datos crudos
# ============================================================
# TODO: lee "data/gastos.csv" en un DataFrame llamado df

df = pd.read_csv("data/gastos.csv")
# ============================================================
# PASO 2: Explorar (para entender qué está "sucio")
# ============================================================
# TODO: imprime df.info(), df.head(15) y df.isna().sum()
# Anota qué problemas ves: tipos de dato, nulos, formatos raros...
print(df.info())
print(df.head(15))
print(df.isna().sum())


# ============================================================
# PASO 3: Limpieza
# ============================================================
# TODO: normaliza "categoria" (quitar espacios, capitalizar igual para todas)
# TODO: convierte "monto" a float (quitar el simbolo "$" si aparece)
# TODO: convierte "fecha" a datetime (hay dos formatos mezclados)
# TODO: decide qué hacer con los montos faltantes (eliminar fila? poner 0? la media?)
# TODO: elimina filas duplicadas


# ============================================================
# PASO 4: Cargar el resultado limpio a SQLite
# ============================================================
# TODO: guarda df en una base "finanzas.db", tabla "gastos"
# pista: sqlite3.connect(...) + df.to_sql(...)


# ============================================================
# PASO 5: Consultas SQL sobre los datos ya limpios
# ============================================================
# TODO: total gastado por categoria
# TODO: mes con mayor gasto total
# TODO: gasto promedio por metodo de pago
