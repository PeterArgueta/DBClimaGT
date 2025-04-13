# Paso 6 — Ejecutar la Carga y Verificar los Datos Importados

> **Objetivo:**  
> En este paso vamos a ejecutar el script de importación para cargar los datos climatológicos en la base de datos, y luego verificaremos que la carga haya sido exitosa consultando directamente en PostgreSQL.

---

## 🖥️ Requisitos previos

- Haber completado:
  - **Paso 1 — Instalación de PostgreSQL y PostGIS en Ubuntu**
  - **Paso 2 — Creación de la Base de Datos y la Tabla Climatológica**
  - **Paso 3 — Configuración de la Contraseña para el Usuario de la Base de Datos**
  - **Paso 4 — Preparar el Entorno Python e Instalar Dependencias**
  - **Paso 5 — Crear el Script de Importación Masiva de Datos Climatológicos**

---

## 🛠️ Instrucciones paso a paso

### 1️⃣ Limpiar la tabla antes de cargar (buena práctica)

Antes de ejecutar el script, vaciamos la tabla para asegurarnos de que la carga sea limpia:

```bash
sudo -u postgres psql -d climatologia
```

Dentro de PostgreSQL, ejecuta:

```sql
TRUNCATE TABLE datos_climaticos;
\q
```

---

### 2️⃣ Ejecutar el script de importación

En la terminal, dentro del directorio donde guardaste `01_postgres_load.py`, ejecuta:

```bash
python 01_postgres_load.py
```

> ✅ **Resultado esperado:**  
> Deberías ver una barra de progreso avanzando y, al finalizar:
> ```
> ✅ Importación completada.
> ```

> Tiempo estimado: ~23 segundos para ~841,000 registros (dependiendo de tu equipo).

---

### 3️⃣ Verificar que los datos se hayan importado correctamente

Vuelve a abrir PostgreSQL:

```bash
sudo -u postgres psql -d climatologia
```

Ejecuta la siguiente consulta para contar los registros:

```sql
SELECT COUNT(*) FROM datos_climaticos;
```

> ✅ Resultado esperado:
> ```
>  count  
> --------
>  841491
> (1 row)
> ```

Consulta algunas estaciones para verificar los datos:

```sql
SELECT nombre_estacion, COUNT(*)
FROM datos_climaticos
GROUP BY nombre_estacion
ORDER BY count DESC;
```

Salir de PostgreSQL:

```
\q
```

---

## 🚀 Paso completado

¡Excelente! 🎉  
Tu base de datos climatológica está completamente cargada y lista para usarse.

---

## ✅ Siguiente paso

Tu base de datos ya está operativa.  
Puedes continuar con:

- Automatización diaria de carga de nuevos datos.
- Backups automáticos de la base.
- Exposición de la base como API pública para consultas externas.

¡Estás listo para llevar tu proyecto al siguiente nivel! 🚀

