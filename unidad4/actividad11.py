def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

inventario = []

def ingresar_cantidad_producto():
    producto = input("Ingrese el nombre del producto: ")
    cantidad = get_int("Ingrese la cantidad de {} en stock: ".format(producto))
    inventario.append((producto, cantidad))

while True:
    print("\nMenú Principal:")
    print("1. Ingresar Inventario")
    print("2. Ver Inventario")
    print("3. Salir")

    opcion = get_int("Seleccione una opción: ")

    if opcion == 1:
        ingresar_cantidad_producto()
    elif opcion == 2:
        print("\nInventario Actual:")
        for producto, cantidad in inventario:
            print("{}: {}".format(producto, cantidad))
    elif opcion == 3:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")