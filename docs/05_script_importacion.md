# Paso 5 — Crear el Script de Importación Masiva de Datos Climatológicos

> **Objetivo:**  
> En este paso vamos a crear un script en Python que importará de manera eficiente los datos climáticos desde un archivo CSV hacia la base de datos PostgreSQL que ya configuramos.

---

## 🖥️ Requisitos previos

- Haber completado:
  - **Paso 1 — Instalación de PostgreSQL y PostGIS en Ubuntu**
  - **Paso 2 — Creación de la Base de Datos y la Tabla Climatológica**
  - **Paso 3 — Configuración de la Contraseña para el Usuario de la Base de Datos**
  - **Paso 4 — Preparar el Entorno Python e Instalar Dependencias**

- Tener listo el archivo de datos: `data_1960-2025.csv`

---

## 🛠️ Instrucciones paso a paso

### 1️⃣ Crear el archivo del script

En tu carpeta de proyecto, crea un archivo llamado:

```
01_postgres_load.py
```

---

### 2️⃣ Pega el siguiente código optimizado en el archivo

```python
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from io import StringIO
from tqdm import tqdm

# Configuración de conexión a la base de datos
db_user = 'postgres'
db_password = 'gEdal&{+A0pu9hN=fA~)'
db_host = 'localhost'
db_port = '5432'
db_name = 'climatologia'
table_name = 'datos_climaticos'
csv_file = '/ruta/completa/data_1960-2025.csv'  # Cambia esta ruta por la ubicación real de tu CSV

# Función para carga masiva eficiente
def copy_from_stringio(conn, df, table):
    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False, sep=',')
    buffer.seek(0)
    cursor = conn.cursor()
    try:
        cursor.copy_expert(
            f"""
            COPY {table} (
                fecha, nombre_estacion, codigo, codigo_insivumeh, precipitacion,
                temperatura_maxima, temperatura_minima, temperatura_media, evaporacion_tanque,
                evaporacion_piche, humedad_relativa, brillo_solar, nubosidad,
                velocidad_viento, direccion_viento, presion_atmosferica,
                temperatura_suelo_5cm, temperatura_suelo_50cm, temperatura_suelo_100cm,
                radiacion, latitud, longitud, altitud, fuente, geom
            )
            FROM STDIN WITH CSV DELIMITER ','
            """, buffer
        )
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    cursor.close()

# Proceso de lectura y carga del CSV
def process_and_insert():
    chunksize = 50000
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    conn = engine.raw_connection()

    with tqdm(total=sum(1 for line in open(csv_file, encoding='utf-8')) - 1, desc='Importando') as pbar:
        for chunk in pd.read_csv(csv_file, sep=';', chunksize=chunksize, encoding='utf-8'):
            chunk.columns = [c.strip().lower().replace('á', 'a').replace('é', 'e').replace('í', 'i')
                             .replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n')
                             .replace(' ', '_') for c in chunk.columns]

            if chunk.iloc[0].astype(str).str.contains('FECHA', case=False).any():
                chunk = chunk.iloc[1:]

            chunk = chunk.where(pd.notnull(chunk), None)

            chunk['geom'] = chunk.apply(lambda row: f"SRID=4326;POINT({row['longitud']} {row['latitud']})", axis=1)

            columns_order = [
                'fecha', 'nombre_estacion', 'codigo', 'codigo_insivumeh', 'precipitacion',
                'temperatura_maxima', 'temperatura_minima', 'temperatura_media', 'evaporacion_tanque',
                'evaporacion_piche', 'humedad_relativa', 'brillo_solar', 'nubosidad',
                'velocidad_viento', 'direccion_viento', 'presion_atmosferica',
                'temperatura_suelo_5cm', 'temperatura_suelo_50cm', 'temperatura_suelo_100cm',
                'radiacion', 'latitud', 'longitud', 'altitud', 'fuente', 'geom'
            ]
            chunk = chunk[columns_order]

            copy_from_stringio(conn, chunk, table_name)
            pbar.update(len(chunk))

    conn.close()
    print('✅ Importación completada.')

if __name__ == '__main__':
    process_and_insert()
```

> ✅ **Recuerda cambiar la ruta del CSV** en la variable `csv_file` por la ruta correcta de tu archivo de datos.

---

### 3️⃣ Guardar y cerrar el archivo

Guarda los cambios y cierra tu editor.

---

## 🚀 Paso completado

¡Excelente! 🎉  
Ahora tienes listo tu script profesional de importación masiva de datos climatológicos hacia PostgreSQL.

En el siguiente paso lo ejecutaremos para cargar tus datos.

---

## ✅ Siguiente paso

Continúa con: **Paso 6 — Ejecutar la carga y verificar los datos importados**

