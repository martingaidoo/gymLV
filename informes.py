import sqlite3
import pandas as pd

# Conectar a la base de datos SQLite
conn = sqlite3.connect("BaseDatos.db")

# Consulta SQL para obtener todos los datos de la tabla "Clientes"
consulta = "SELECT * FROM Clientes;"

# Leer los datos en un DataFrame de pandas
df = pd.read_sql_query(consulta, conn)

# Guardar el DataFrame en un archivo Excel
df.to_excel("clientes_data.xlsx", index=False)

# Cerrar la conexión a la base de datos
conn.close()
