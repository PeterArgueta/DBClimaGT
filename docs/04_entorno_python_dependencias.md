# Paso 4 — Preparar el Entorno Python e Instalar Dependencias

> **Objetivo:**  
> En este paso vamos a preparar el entorno de Python e instalar todas las librerías necesarias para que podamos ejecutar el script de importación de datos climatológicos hacia la base de datos PostgreSQL.

---

## 🖥️ Requisitos previos

- Haber completado:
  - **Paso 1 — Instalación de PostgreSQL y PostGIS en Ubuntu**
  - **Paso 2 — Creación de la Base de Datos y la Tabla Climatológica**
  - **Paso 3 — Configuración de la Contraseña para el Usuario de la Base de Datos**

- Tener Python 3.x instalado en tu sistema.

---

## 🛠️ Instrucciones paso a paso

### 1️⃣ Verificar que Python esté instalado

En la terminal, ejecuta:

```bash
python3 --version
```

> ✅ Resultado esperado: algo como `Python 3.10.x` o superior

Si no está instalado, puedes instalarlo con:

```bash
sudo apt install python3 python3-pip
```

---

### 2️⃣ (Opcional pero recomendado) Crear un entorno virtual para el proyecto

Esto ayudará a mantener las dependencias del proyecto aisladas:

```bash
python3 -m venv venv
source venv/bin/activate
```

> ✅ Si ves que el prompt de tu terminal cambia a `(venv)`, significa que tu entorno virtual está activo.

---

### 3️⃣ Instalar las dependencias necesarias

Ejecuta el siguiente comando para instalar las librerías que utilizará tu script:

```bash
pip install pandas sqlalchemy psycopg2-binary geopandas tqdm
```

> ✅ Explicación rápida de las librerías:
> - **pandas**: manipulación y análisis de datos.
> - **sqlalchemy**: conexión y gestión de bases de datos.
> - **psycopg2-binary**: conector PostgreSQL para Python.
> - **geopandas**: manejo de datos espaciales.
> - **tqdm**: barra de progreso para ver el avance de la carga masiva.

---

### 4️⃣ Verificar instalación de las librerías

Puedes verificar que las librerías se instalaron correctamente ejecutando:

```bash
pip freeze
```

Deberías ver listadas las librerías mencionadas.

---

## 🚀 Paso completado

Tu entorno de Python ya está listo y con todas las dependencias necesarias para continuar con la creación y ejecución del script de importación.

---

## ✅ Siguiente paso

Continúa con: **Paso 5 — Crear el script de importación masiva de datos climatológicos**

