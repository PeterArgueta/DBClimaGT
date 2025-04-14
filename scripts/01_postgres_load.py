import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm
import unicodedata

# ✅ Función para eliminar acentos
def remove_accents(input_str):
    return ''.join(
        c for c in unicodedata.normalize('NFD', input_str)
        if unicodedata.category(c) != 'Mn'
    )

# Configuración de la base de datos
db_user = 'postgres'
db_password = 'gEdal&{+A0pu9hN=fA~)'
db_host = 'db'  # Docker service name
db_port = '5432'
db_name = 'climatologia'
table_name = 'datos_climaticos'

# Ruta del archivo CSV dentro del contenedor Docker
csv_file = '/data/data_1960-2025.csv'

def process_and_insert():
    try:
        print("📂 Leyendo archivo CSV...")
        df = pd.read_csv(csv_file, sep=';', encoding='utf-8')

        # ✅ Normalizamos columnas globales: quitamos acentos y minúsculas
        df.columns = df.columns.map(remove_accents).str.lower()
        print(f"✅ Archivo leído correctamente con {len(df)} registros.")

        # Conexión a PostgreSQL
        print("🔌 Estableciendo conexión con la base de datos PostgreSQL...")
        engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
        conn = engine.raw_connection()
        cursor = conn.cursor()

        # Crear tabla si no existe
        print("🧩 Verificando existencia de la tabla...")
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                fecha DATE,
                nombre_estacion TEXT,
                codigo TEXT,
                codigo_insivumeh TEXT,
                precipitacion REAL,
                temperatura_maxima REAL,
                temperatura_minima REAL,
                temperatura_media REAL,
                evaporacion_tanque REAL,
                evaporacion_piche REAL,
                humedad_relativa REAL,
                brillo_solar REAL,
                nubosidad REAL,
                velocidad_viento REAL,
                direccion_viento REAL,
                presion_atmosferica REAL,
                temperatura_suelo_5cm REAL,
                temperatura_suelo_50cm REAL,
                temperatura_suelo_100cm REAL,
                radiacion REAL,
                latitud REAL,
                longitud REAL,
                altitud REAL,
                fuente TEXT
            );
        ''')
        conn.commit()
        print("✅ Tabla verificada o creada correctamente.")

        # ✅ Verificar si la tabla ya tiene datos
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        row_count = cursor.fetchone()[0]

        if row_count > 0:
            print(f"⚠️ La tabla '{table_name}' ya contiene {row_count} registros. Se omite la carga de datos.")
            return

        # Proceso de carga en bloques con barra de progreso
        chunk_size = 50000
        total_rows = len(df)

        print(f"🚀 Iniciando carga de {total_rows} registros en bloques de {chunk_size}...")

        for start in tqdm(range(0, total_rows, chunk_size)):
            end = start + chunk_size
            chunk = df.iloc[start:end].copy()  # ✅ Copia segura del chunk

            # ✅ Limpiamos columnas del chunk (removemos sufijos, acentos, minúsculas)
            chunk.reset_index(drop=True, inplace=True)
            chunk.columns = chunk.columns.str.replace(r'_m\d+$', '', regex=True)
            chunk.columns = chunk.columns.map(remove_accents).str.lower()

            # Insertamos
            chunk.to_sql(table_name, engine, if_exists='append', index=False, method='multi')

        print("✅ Importación completada exitosamente.")

    except Exception as e:
        print(f"❌ Error durante la importación: {e}")

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

if __name__ == "__main__":
    process_and_insert()
