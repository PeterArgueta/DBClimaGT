import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from io import StringIO
from tqdm import tqdm

# Configura tus datos de conexión
db_user = 'postgres'
db_password = 'gEdal&{+A0pu9hN=fA~)'
db_host = 'localhost'
db_port = '5432'
db_name = 'climatologia'
table_name = 'datos_climaticos'


# Ruta a tu archivo CSV
csv_file = 'data_1960-2025.csv'

# Define función para cargar en bloque
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
        return
    cursor.close()

# Procesa los datos
def process_and_insert():
    # Lee el CSV por bloques para que no se sature la RAM
    # Lee el CSV por bloques para que no se sature la RAM
    chunksize = 50000  # Puedes ajustar según tu RAM
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    conn = engine.raw_connection()
    with tqdm(total=sum(1 for line in open(csv_file, encoding='utf-8')) - 1, desc='Importando') as pbar:
        for chunk in pd.read_csv(csv_file, sep=';', chunksize=chunksize, encoding='utf-8'):
            # Normaliza nombres de columnas
            chunk.columns = [c.strip().lower().replace('á', 'a').replace('é', 'e').replace('í', 'i')
                            .replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n')
                            .replace(' ', '_') for c in chunk.columns]

            # Verifica si el primer valor de la fila es un encabezado y elimina
            if chunk.iloc[0].astype(str).str.contains('FECHA', case=False).any():
                chunk = chunk.iloc[1:]

            # Reemplaza NaN por NULL explícito para PostgreSQL
            chunk = chunk.where(pd.notnull(chunk), None)

            # Crear columna geom para PostGIS
            chunk['geom'] = chunk.apply(lambda row: f"SRID=4326;POINT({row['longitud']} {row['latitud']})", axis=1)

            # Ordena columnas como en la base de datos
            columns_order = [
                'fecha', 'nombre_estacion', 'codigo', 'codigo_insivumeh', 'precipitacion',
                'temperatura_maxima', 'temperatura_minima', 'temperatura_media', 'evaporacion_tanque',
                'evaporacion_piche', 'humedad_relativa', 'brillo_solar', 'nubosidad',
                'velocidad_viento', 'direccion_viento', 'presion_atmosferica',
                'temperatura_suelo_5cm', 'temperatura_suelo_50cm', 'temperatura_suelo_100cm',
                'radiacion', 'latitud', 'longitud', 'altitud', 'fuente', 'geom'
            ]
            chunk = chunk[columns_order]

            # Inserta bloque
            copy_from_stringio(conn, chunk, table_name)

            # Actualiza barra de progreso
            pbar.update(len(chunk))


    conn.close()
    print('✅ Importación completada.')

if __name__ == '__main__':
    process_and_insert()
