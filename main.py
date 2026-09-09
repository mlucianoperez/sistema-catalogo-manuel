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


def producto_disponible(catalogo):
    while True:
        print("\n--- Menú ---")
        print("1. Ver catálogo completo")
        print("2. Buscar un producto")
        print("3. Agregar un producto nuevo")
        print("4. Ver solo los productos disponibles")
        print("0. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            print("\n--- Catálogo ---")
            for producto in catalogo:
                print(f"{producto['nombre']}: ${producto['precio']}")
        
        elif opcion == "2":
            nombre = input("\nIngresa el nombre del producto a buscar: ")
            resultado = buscar_producto(catalogo, nombre)
            if resultado:
                print(f"\nProducto encontrado: {resultado['nombre']}: ${resultado['precio']}")
            else:
                print("\nProducto no encontrado")
        
        elif opcion == "3":
            nombre = input("\nIngresa el nombre del producto: ")
            try:
                precio = float(input("Ingresa el precio: "))
                agregar_producto(catalogo, nombre, precio, True)
                print(f"\n✓ Producto '{nombre}' agregado correctamente al catálogo")
            except ValueError:
                print("\nError: El precio debe ser un número válido")
        
        elif opcion == "4":
            disponibles = [producto for producto in catalogo if producto['disponibilidad']]
            if disponibles:
                print("\n--- Productos Disponibles ---")
                for producto in disponibles:
                    print(f"{producto['nombre']}: ${producto['precio']}")
            else:
                print("\nNo hay productos disponibles")
        
        elif opcion == "0":
            print("¡Hasta luego!")
            break


def main():
    producto_disponible(catalogo_negocio)


if __name__ == "__main__":
    main()
