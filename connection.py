import mariadb
import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

def obtener_conexion():
    try:
        conexion = mariadb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            database=os.getenv("DB_NAME")
        )
        return conexion
    except mariadb.Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        raise
