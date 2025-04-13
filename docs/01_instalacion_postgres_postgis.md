# Paso 1 — Instalación de PostgreSQL y PostGIS en Ubuntu

> **Objetivo:**  
> En este paso instalaremos PostgreSQL y PostGIS en una computadora con sistema operativo Ubuntu.  
> PostgreSQL será nuestra base de datos robusta para almacenar la información climática y PostGIS añadirá capacidades geográficas para trabajar con coordenadas de las estaciones meteorológicas.

---

## 💻 Requisitos previos

- Computadora con **Ubuntu** instalado (versión 20.04 o superior recomendada).
- Acceso a la terminal con permisos de superusuario (`sudo`).

---

## 🛠️ Instrucciones paso a paso

### 1️⃣ Actualizar los paquetes del sistema

Siempre es buena práctica actualizar antes de instalar nuevos paquetes:

```bash
sudo apt update
```

---

### 2️⃣ Instalar PostgreSQL y sus componentes adicionales

```bash
sudo apt install postgresql postgresql-contrib
```

---

### 3️⃣ Instalar PostGIS para capacidades geoespaciales

```bash
sudo apt install postgis
```

---

### 4️⃣ Verificar que PostgreSQL esté corriendo correctamente

Ejecuta:

```bash
sudo systemctl status postgresql
```

> ✅ **Resultado esperado:**  
> Deberías ver algo como:
> ```
> Active: active (exited) ...
> ```

Si ves "active", significa que PostgreSQL está instalado correctamente y listo para usar.

---

## 🚀 Paso completado

Con esto, ya tienes PostgreSQL y PostGIS listos en tu máquina Ubuntu.  
Podrás crear bases de datos, activar extensiones geográficas, y comenzar a almacenar y consultar datos climatológicos.

---

## ✅ Siguiente paso

Continúa con: **Paso 2 — Crear la base de datos y la tabla climatológica**

