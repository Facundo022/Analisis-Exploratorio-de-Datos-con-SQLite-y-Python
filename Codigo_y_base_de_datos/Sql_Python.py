
# Importando las librerías necesarias.
import os
import sqlite3

# Obtener la ruta del directorio actual del script
directorio_script = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo de base de datos
ruta_base_datos = os.path.join(directorio_script, 'database.sqlite')

# Conectar a la base de datos
conn = sqlite3.connect(ruta_base_datos)


# Explorando la base de datos

# Crear un objeto cursor
cursor = conn.cursor()

# Consultar las tablas en la base de datos
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

# Mostrar el nombre de las tablas
print("En la base de datos tenemos estas tablas:")
for tabla in tablas:
    print(tabla[0])


# Viendo la estructura de algunas las tablas y sus tipos de datos

tabla = 'Team'

# Consultar la información sobre las columnas de la tabla seleccionada
cursor.execute(f"PRAGMA table_info({tabla});")
columnas = cursor.fetchall()

# Mostrar la información sobre las columnas
print(f"Tipos de datos en la tabla '{tabla}':")
for columna in columnas:
    nombre_columna = columna[1]
    tipo_dato = columna[2]
    print(f"Columna: {nombre_columna}, Tipo de Dato: {tipo_dato}")

# Consultar la cantidad de registros por cada tabla
# Obtener la lista de tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

# Consultar y mostrar la cantidad de registros por tabla
for tabla in tablas:
    nombre_tabla = tabla[0]
    cursor.execute(f"SELECT COUNT(*) FROM {nombre_tabla};")
    cantidad_registros = cursor.fetchone()[0]
    print(f"Tabla: {nombre_tabla}, Cantidad de Registros: {
          cantidad_registros}")

# Cerrando el cursor y la conexión
cursor.close()
conn.close()
