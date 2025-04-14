#!/bin/bash

echo "🧹 Vamos a detener y limpiar los contenedores del proyecto..."

# Detener contenedores y limpiar volúmenes y redes huérfanas
docker compose down --volumes --remove-orphans

echo "✅ Todo limpio. Tu proyecto fue detenido correctamente."
echo "ℹ️ Si querés volver a levantarlo, usá: ./start.sh"
