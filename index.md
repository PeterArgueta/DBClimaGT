# 🌧️ DBClimaGT — Base de Datos Climatológica de Guatemala

Automatiza una base de datos PostgreSQL + PostGIS para datos climatológicos de Guatemala, usando Docker.

---

## 📋 Índice

- [¿Qué hace este proyecto?](#-qué-hace-este-proyecto)
- [Requisitos previos](#-requisitos-previos)
- [Cómo instalar Docker y Docker Compose en Ubuntu](#-cómo-instalar-docker-y-docker-compose-en-ubuntu)
- [Instrucciones de uso](#-instrucciones-de-uso)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Comandos útiles](#-comandos-útiles)


---

## 🚀 ¿Qué hace este proyecto?

- 🔥 Levanta una base de datos PostgreSQL lista para usar.
- 🔥 Importa automáticamente el dataset climatológico masivo (1960 - Marzo2025).
- 🔥 Protege la base para que no se duplique la info si lo volvés a correr.
- 🔥 Todo el flujo está automatizado y limpio con Docker.
- 🐳 Ideal para ciencia de datos, análisis climático, o proyectos de consulta pública.

---

## 🧹 Requisitos previos

- Tener instalado Docker y Docker Compose en tu compu.

Verificá que Docker esté instalado:

```bash
docker --version
docker compose version
```

Si no, seguí la guía más abajo para instalarlo 🚀

---

## 🐳 Cómo instalar Docker y Docker Compose en Ubuntu

Si es la primera vez que usás Docker, seguí estos pasos para instalarlo en tu máquina Ubuntu.

### 1. Actualizá tus paquetes

```bash
sudo apt update
sudo apt install ca-certificates curl gnupg lsb-release
```

### 2. Agregá la clave GPG oficial de Docker

```bash
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

### 3. Agregá el repositorio de Docker

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### 4. Instalá Docker Engine y Docker Compose plugin

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 5. Verificá que Docker se haya instalado correctamente

```bash
docker --version
docker compose version
```

### 6. (Opcional) Usá Docker sin sudo

Agregá tu usuario al grupo `docker` para no tener que usar sudo cada vez que ejecutás Docker:

```bash
sudo usermod -aG docker $USER
```

> 🔄 **Importante:** Cerrá sesión y volvé a iniciar para que se apliquen los cambios.

---

## ⚙️ Instrucciones de uso

### 1. Cloná este repositorio

```bash
git clone https://github.com/tu-usuario/DBClimaGT.git
cd DBClimaGT
```


### 2. Dale permisos de ejecución al script

```bash
chmod +x start.sh stop.sh
```

### 3. Corré el proyecto

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

> 🧹 **Importante:** Este comando limpia **solo** los contenedores, volúmenes y redes del proyecto DBClimaGT. Docker seguirá instalado en tu compu y otros proyectos que tengas no se verán afectados.

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
