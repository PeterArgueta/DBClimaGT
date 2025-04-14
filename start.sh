#!/bin/bash

echo "🚀 Construyendo la imagen de Docker..."
docker compose build

echo "✅ Imagen construida correctamente."

echo "🗄️ Levantando la base de datos en background..."
docker compose up -d db

echo "⌛ Esperando que PostgreSQL esté listo..."
# Esperamos que el servicio de base de datos esté healthy
until docker inspect --format='{{.State.Health.Status}}' dbclimagt | grep "healthy"; do
  sleep 2
done

echo "✅ Base de datos lista."

echo "⬇️ Iniciando la importación de datos..."
docker compose run --rm init

echo "✅ Importación completada."

echo "🎉 Todo listo. La base de datos está disponible en localhost:5432"
echo "ℹ️ Si deseas detener los contenedores, ejecuta: docker compose down"
