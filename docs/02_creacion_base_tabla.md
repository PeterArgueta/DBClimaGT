# Paso 2 — Creación de la Base de Datos y la Tabla Climatológica

> **Objetivo:**  
> En este paso vamos a crear la base de datos principal llamada `climatologia` y una tabla específica `datos_climaticos` que contendrá toda la información climática, incluyendo soporte geoespacial con PostGIS.

---

## 🖥️ Requisitos previos

- Haber completado el **Paso 1 — Instalación de PostgreSQL y PostGIS en Ubuntu**.
- Tener acceso a la terminal con permisos de superusuario (`sudo`).

---

## 🛠️ Instrucciones paso a paso

### 1️⃣ Entrar a PostgreSQL como superusuario

En la terminal, ejecuta:

```bash
sudo -u postgres psql
```

Verás el prompt de PostgreSQL:

```
postgres=#
```

---

### 2️⃣ Crear la base de datos llamada `climatologia`

Dentro de PostgreSQL, ejecuta:

```sql
CREATE DATABASE climatologia;
```

> ✅ Resultado esperado: `CREATE DATABASE`

Conectarse a la base de datos recién creada:

```sql
\c climatologia
```

> ✅ Resultado esperado: `You are now connected to database "climatologia"...`

---

### 3️⃣ Activar la extensión PostGIS en la base de datos

Ejecuta:

```sql
CREATE EXTENSION postgis;
```

> ✅ Resultado esperado: `CREATE EXTENSION`

---

### 4️⃣ Crear la tabla `datos_climaticos`

Ahora vamos a crear la tabla donde almacenaremos los registros climáticos:

```sql
CREATE TABLE datos_climaticos (
    id SERIAL PRIMARY KEY,
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
    latitud DOUBLE PRECISION,
    longitud DOUBLE PRECISION,
    altitud REAL,
    fuente TEXT,
    geom GEOMETRY(Point, 4326)
);
```

> ✅ Resultado esperado: `CREATE TABLE`

---

### 5️⃣ Salir de PostgreSQL

Una vez creada la base y la tabla, sal del cliente PostgreSQL:

```
\q
```

---

## 🚀 Paso completado

¡Felicidades! 🎉  
La base de datos y la tabla están listas para recibir datos climatológicos.

---

## ✅ Siguiente paso

Continúa con: **Paso 3 — Configurar la contraseña para el usuario de la base de datos**

