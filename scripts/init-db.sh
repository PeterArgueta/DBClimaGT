#!/bin/bash
set -e

echo "🕒 Iniciando espera para PostgreSQL..."

# Espera inicial fija de seguridad
sleep 5

# Esperamos que PostgreSQL se inicie completamente
until pg_isready -h db -p 5432 -U postgres; do
  echo "⏳ Esperando que PostgreSQL esté listo..."
  sleep 2
done

echo "✅ PostgreSQL está listo."

# Ruta del archivo CSV dentro del contenedor
DATA_FILE="/data/data_1960-2025.csv"

# URL de descarga del CSV
DATA_URL="https://www.dropbox.com/scl/fi/k1458ldv1uj2zkbmmugkc/data_1960-2025.csv?rlkey=x3ekvqta7zlnikek0q9enj1j9&st=gjashjw0&dl=0"


# Verificar si el archivo CSV existe
if [ ! -f "$DATA_FILE" ]; then
  echo "⬇️ Archivo CSV no encontrado. Descargando desde: $DATA_URL"
  curl -L -o "$DATA_FILE" "$DATA_URL"
  echo "✅ Archivo CSV descargado exitosamente."
else
  echo "📂 Archivo CSV ya existe en /data/, no es necesario descargarlo."
fi

# Ejecutar el script de carga de datos
echo "🚀 Iniciando importación de datos climatológicos..."
python3 /scripts/01_postgres_load.py
echo "✅ Importación completada exitosamente."
