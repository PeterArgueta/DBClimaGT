# 🐳 Imagen base: PostgreSQL con PostGIS (para soporte geoespacial)
FROM postgis/postgis:16-3.4

# 📝 Variables de entorno para la base de datos
ENV POSTGRES_DB=climatologia
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=gEdal&{+A0pu9hN=fA~)

# 🧩 Instalamos Python 3 y las utilidades necesarias
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl unzip && \
    python3 -m pip install --upgrade pip

# 📂 Creamos directorios de trabajo dentro del contenedor
RUN mkdir -p /scripts /data

# 📦 Copiamos el archivo de requerimientos Python
COPY ./requirements.txt /scripts/requirements.txt

# 🧩 Instalamos dependencias Python dentro del contenedor
RUN python3 -m pip install -r /scripts/requirements.txt

# 📂 Copiamos tu script Python de carga
COPY ./scripts/01_postgres_load.py /scripts/01_postgres_load.py

# 📂 Copiamos el script de inicialización de la base
COPY ./scripts/init-db.sh /scripts/init-db.sh
RUN chmod +x /scripts/init-db.sh


# 🚀 Indicamos que se ejecute el servicio de PostgreSQL al iniciar el contenedor
CMD ["docker-entrypoint.sh", "postgres"]


