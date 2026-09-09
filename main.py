catalogo_negocio = [
    {"nombre": "Masaje corporales", "precio": 500.00, "disponibilidad": True},
    {"nombre": "Manicure", "precio": 200.00, "disponibilidad": True},
    {"nombre": "Pedicure", "precio": 300.00, "disponibilidad": False}
]



def main():
    while True:
        print("\n--- Menú ---")
        print("1. Ver catálogo completo")
        print("0. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            print("\n--- Catálogo ---")
            for producto in catalogo_negocio:
                print(f"{producto['nombre']}: ${producto['precio']}")
        
        elif opcion == "0":
            print("¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
