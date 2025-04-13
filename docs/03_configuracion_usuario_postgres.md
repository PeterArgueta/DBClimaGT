# Paso 3 — Configurar la Contraseña para el Usuario de la Base de Datos

> **Objetivo:**  
> En este paso vamos a establecer una contraseña segura para el usuario `postgres` de la base de datos, lo que nos permitirá conectarnos desde aplicaciones externas como Python de forma segura.

---

## 🖥️ Requisitos previos

- Haber completado:
  - **Paso 1 — Instalación de PostgreSQL y PostGIS en Ubuntu**
  - **Paso 2 — Creación de la Base de Datos y la Tabla Climatológica**

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

### 2️⃣ Establecer la contraseña del usuario `postgres`

Ejecuta el siguiente comando, reemplazando por la contraseña que desees:

```sql
ALTER USER postgres WITH PASSWORD 'gEdal&{+A0pu9hN=fA~)';
```

> ✅ **Recomendaciones para la contraseña:**
> - Usa una contraseña segura que combine letras, números y símbolos.
> - Guarda la contraseña en un lugar seguro.

> ✅ Resultado esperado: `ALTER ROLE`

---

### 3️⃣ Salir de PostgreSQL

Cuando hayas establecido la contraseña, sal del cliente PostgreSQL:

```
\q
```

---

### 4️⃣ (Opcional pero recomendado) Reiniciar PostgreSQL para asegurar la configuración

Aunque no siempre es necesario, reiniciar el servicio asegura que la configuración se aplique correctamente:

```bash
sudo systemctl restart postgresql
```

---

## 🚀 Paso completado

La contraseña para el usuario `postgres` se ha configurado exitosamente.  
Ahora podrás conectarte desde Python o cualquier otra aplicación externa usando estas credenciales.

---

## ✅ Siguiente paso

Continúa con: **Paso 4 — Preparar el entorno Python e instalar las dependencias necesarias para la importación**

