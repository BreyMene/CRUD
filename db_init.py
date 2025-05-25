import mariadb
from config import DB_CONFIG

def inicializar_base_de_datos():
    try:
        # Conectar sin especificar la base de datos
        conn = mariadb.connect(
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port']
        )
        cursor = conn.cursor()

        # Crear base de datos si no existe
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        conn.commit()
        print(f"✅ Base de datos '{DB_CONFIG['database']}' verificada o creada.")
        cursor.close()
        conn.close()

        # Conectar a la base de datos para crear tabla si no existe
        conn = mariadb.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100),
                descripcion TEXT,
                precio FLOAT,
                cantidad INT
            )
        """)
        conn.commit()
        print("✅ Tabla 'productos' verificada o creada.")
        cursor.close()
        conn.close()

    except mariadb.Error as e:
        print(f"❌ Error al inicializar la base de datos: {e}")
