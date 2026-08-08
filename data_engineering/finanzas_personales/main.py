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
df["categoria"] = df["categoria"].str.strip().str.title()
df["monto"] = df["monto"].str.replace("$", "", regex=False).astype(float)
df["fecha"] = pd.to_datetime(df["fecha"], format="mixed", dayfirst=True)
df = df.dropna(subset=["monto"])
df = df.drop_duplicates()
print(df.info())
# ============================================================
# PASO 4: Cargar el resultado limpio a SQLite
# ============================================================
# TODO: guarda df en una base "finanzas.db", tabla "gastos"
# pista: sqlite3.connect(...) + df.to_sql(...)
conn = sqlite3.connect("finanzas.db")
df.to_sql("gastos", conn, if_exists="replace", index=False)
conn.close()

# ============================================================
# PASO 5: Consultas SQL sobre los datos ya limpios
# ============================================================
# TODO: total gastado por categoria
conn = sqlite3.connect("finanzas.db")
total_por_categoria = pd.read_sql("""
    SELECT categoria, SUM(monto) AS total
    FROM gastos
    GROUP BY categoria
    ORDER BY total DESC
""", conn)
print(total_por_categoria)
# TODO: mes con mayor gasto total
gasto_por_mes = pd.read_sql("""
   SELECT strftime('%Y-%m', fecha) AS mes, SUM(monto) AS total
   FROM gastos
   GROUP BY mes
   ORDER BY total DESC
""", conn)
print(gasto_por_mes)
# TODO: gasto promedio por metodo de pago
promedio_por_metodo = pd.read_sql("""
   SELECT metodo_pago, AVG(monto) AS promedio
   FROM gastos
   GROUP BY metodo_pago
""", conn)
print(promedio_por_metodo)

