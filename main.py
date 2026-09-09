catalogo_negocio = [
    {"nombre": "Masaje corporales", "precio": 500.00, "disponibilidad": True},
    {"nombre": "Manicure", "precio": 200.00, "disponibilidad": True},
    {"nombre": "Pedicure", "precio": 300.00, "disponibilidad": False}
]


def buscar_producto(catalogo, nombre_buscado):
    for producto in catalogo:
        if producto['nombre'].lower() == nombre_buscado.lower():
            return producto
    return None


def agregar_producto(catalogo, nombre, precio, disponible):
    catalogo.append({"nombre": nombre, "precio": precio, "disponibilidad": disponible})


def main():
    while True:
        print("\n--- Menú ---")
        print("1. Ver catálogo completo")
        print("2. Buscar un producto")
        print("3. Agregar un producto nuevo")
        print("0. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            print("\n--- Catálogo ---")
            for producto in catalogo_negocio:
                print(f"{producto['nombre']}: ${producto['precio']}")
        
        elif opcion == "2":
            nombre = input("\nIngresa el nombre del producto a buscar: ")
            resultado = buscar_producto(catalogo_negocio, nombre)
            if resultado:
                print(f"\nProducto encontrado: {resultado['nombre']}: ${resultado['precio']}")
            else:
                print("\nProducto no encontrado")
        
        elif opcion == "3":
            nombre = input("\nIngresa el nombre del producto: ")
            try:
                precio = float(input("Ingresa el precio: "))
                agregar_producto(catalogo_negocio, nombre, precio, True)
                print(f"\n✓ Producto '{nombre}' agregado correctamente al catálogo")
            except ValueError:
                print("\nError: El precio debe ser un número válido")
        
        elif opcion == "0":
            print("¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
