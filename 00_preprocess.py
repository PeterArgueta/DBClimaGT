import pandas as pd

# Ruta del archivo
file_path = 'data_1960-2025.csv'

# Leer el CSV (separador ; )
df = pd.read_csv(file_path, sep=';')

# Mostrar primeras filas para verificar
print("Primeras filas de la base de datos:\n")
print(df.head())

print("\n--- INFORMACIÓN GENERAL ---\n")
print(df.info())

print("\n--- DESCRIPCIÓN ESTADÍSTICA GENERAL (NUMÉRICOS) ---\n")
print(df.describe(include=[float, int]))

print("\n--- DESCRIPCIÓN ESTADÍSTICA GENERAL (CATEGÓRICOS) ---\n")
print(df.describe(include=[object]))

print("\n--- CONTEO DE VALORES NULOS POR COLUMNA ---\n")
print(df.isnull().sum())

print("\n--- CONTEO DE VALORES ÚNICOS POR COLUMNA ---\n")
print(df.nunique())

print("\n--- ESTADÍSTICAS POR VARIABLE NUMÉRICA ---\n")
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
    print(f"\nEstadísticas para: {col}")
    print(f"Media: {df[col].mean()}")
    print(f"Máximo: {df[col].max()}")
    print(f"Mínimo: {df[col].min()}")
    print(f"Mediana: {df[col].median()}")
    print(f"Desviación estándar: {df[col].std()}")
    print(f"Valores únicos: {df[col].nunique()}")

print("\n--- PROPORCIÓN DE VALORES NULOS EN % POR COLUMNA ---\n")
print((df.isnull().sum() / len(df)) * 100)
