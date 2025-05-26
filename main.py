from db_init import inicializar_base_de_datos
from interface import iniciar_interface

def main():
    inicializar_base_de_datos()
    iniciar_interface()

if __name__ == "__main__":
    main()