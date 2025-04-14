# 🌧️ DBClimaGT — Base de Datos Climatológica de Guatemala

Creación de una base de datos PostgreSQL + PostGIS para datos climatológicos de Guatemala, usando Docker.

---

## 🚀 ¿Qué hace este proyecto?

- 🔥 Levanta una base de datos PostgreSQL lista para usar.
- 🔥 Importa automáticamente el dataset climatológico masivo (1960-2025 (Marzo)).
- 🔥 Protege la base para que no se duplique la información si lo volvés a correr.
- 🔥 Todo el flujo está automatizado y limpio con Docker.
- 🐳 Ideal para ciencia de datos, análisis climático, o proyectos de consulta pública.

---

## 🧹 Requisitos previos

- Tener instalado Docker y Docker Compose en tu computadora.

Verificá que Docker esté instalado:

```bash
docker --version
docker compose version
```

Si no, instalalo siguiendo la guía oficial: https://docs.docker.com/get-docker/

---

## ⚙️ Instrucciones de uso

### 1. Cloná este repositorio

```bash
git clone https://github.com/PeterArgueta/DBClimaGT.git
cd DBClimaGT
```

### 2. Dale permisos de ejecución al script

```bash
chmod +x start.sh stop.sh
```

### 3. Ejecutar el proyecto

Ejecutá el script de inicio automático:

```bash
./start.sh
```

✅ Esto va a:
- Construir la imagen de Docker.
- Levantar la base de datos.
- Importar automáticamente los datos climatológicos.
- La base de datos quedará lista para usar en `localhost:5432`.

### 5. Verificá la carga

Para conectarte a la base de datos:

```bash
docker exec -it dbclimagt psql -U postgres -d climatologia
```

Consultá la cantidad de registros importados:

```sql
SELECT COUNT(*) FROM datos_climaticos;
```

### 6. Cuando quieras detener y limpiar el proyecto

Corré el script de parada automática:

```bash
./stop.sh
```

> 🧹 **Importante:** Este comando limpia **solo** los contenedores, volúmenes y redes del proyecto DBClimaGT. Docker seguirá instalado en tu computadora y otros proyectos que tengas no se verán afectados.

---

## 📂 Estructura del proyecto

```
DBClimaGT/
├── data/                     # Tu archivo data_1960-2025.csv va aquí
├── scripts/
│   └── 01_postgres_load.py   # Script de importación de datos
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── start.sh                  # Script para construir y ejecutar el proyecto
├── stop.sh                   # Script para detener y limpiar el proyecto
└── README.md                 # Este documento
```

---

## 🛠️ Comandos útiles

| Acción                         | Comando |
|--------------------------------|----------|
| Detener y limpiar el proyecto  | `./stop.sh` |
| Ver contenedores activos       | `docker ps` |
| Ver registros de la base de datos | `docker exec -it dbclimagt psql -U postgres -d climatologia -c "SELECT COUNT(*) FROM datos_climaticos;"` |
| Ejecutar solo la importación manualmente | `docker compose run --rm init` |

---

## ✅ Notas finales

- ✔️ El proyecto está preparado para no sobreescribir la base de datos si la carga ya fue realizada.
- ✔️ Si querés reiniciar todo desde cero, ejecutá:

```bash
./stop.sh
```

- ✔️ Una vez configurado, tu base queda funcionando en `localhost:5432`, lista para conectar con herramientas como DBeaver, PgAdmin, Python, etc.

---

