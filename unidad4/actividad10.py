nombre_archivo = input("Ingrese el nombre del archivo: ")
# C:\Users\rbeze\VS Code Projects\python_cs50\python_cs50\unidad4\text.txt

while True:

    try:

        with open(nombre_archivo, "r") as archivo:

            datos = archivo.read()

    except FileNotFoundError:

        print("El archivo no se encuentra.")

        nombre_archivo = input("Ingrese un nombre de archivo válido: ")

    else:

        print("Contenido del archivo:")

        print(datos)

        break  # Sale del bucle si la operación tiene éxito