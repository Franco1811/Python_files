import os #Importamos la librería os que es un modulo capaz de interactuar con el sistema operativo
#MANEJO DE FICHEROS

"""
* EJERCICIO:
* Desarrolla un programa capaz de crear un archivo que se llame como
* tu usuario de GitHub y tenga la extensión .txt.
* Añade varias líneas en ese fichero:
* - Tu nombre.
* - Edad.
* - Lenguaje de programación favorito.
* Imprime el contenido.
* Borra el fichero.
*
"""


file_name = "Franco1811.txt" #Nombre del archivo que vamos a crear


with open (file_name,"w") as file:  
    #creamos un fichero con el nombre que hemos definido y con permisos de escritura
    file.write("Franco\n")  #\n es un salto de línea
    file.write("20\n")     
    file.write("Python\n")


with open (file_name,"r") as file:
    #Leemos el fichero
    print(file.read())  #nos muestra el contenido del fichero (leerlo)
 

os.remove(file_name) #Borramos el fichero 1
print(f"El archivo {file_name} ha sido borrado.")


#forma de trabajar con ficheros de manera segura : trabajar con with ... as y podremos accede al fichero mediante una variable que se llama file en este caso

"""
* DIFICULTAD EXTRA (opcional):
* Desarrolla un programa de gestión de ventas que almacena sus datos en un 
* archivo .txt.
* - Cada producto se guarda en una línea del arhivo de la siguiente manera:
*   [nombre_producto], [cantidad_vendida], [precio].
* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
*   actualizar, eliminar productos y salir.
* - También debe poseer opciones para calcular la venta total y por producto.
* - La opción salir borra el .txt.
"""

file_name = "Franco1811_shop.txt" #Le doy otro nombre al fichero para asegurarme de que no se sobreescriba el anterior y se borre y ejecute varias veces el programa
open (file_name,"a") #esto me sirve para abrir el fichero en modo append (añadir) para que no se sobreescriba el contenido del fichero

while True: #uso while true para que el programa se ejecute de manera indefinida
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Introduce una opción: ")

    if option == "1":
        name= input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")

        with open (file_name, "a") as file:   #el a nos permite añadir contenido al fichero (append|añadir)
           file.write(f"{name}, {quantity}, {price}\n") 


    elif option == "2":
        name = input("Nombre: ")
        with open(file_name, "r") as file: #solo queremos leer el fichero

            for line in file.readlines():
                if line.split(", ")[0] == name:  # el split nos permite separar los elementos de la línea por la coma y el [0] nos permite acceder solo al primer elemento
                    print(line)
                    break #para que no siga buscando una vez que ha encontrado el producto


    elif option == "3":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")

        with open(file_name, "r") as file:  #reutilizo parte del codigo de la opcion 2 para buscar el producto en mode lectura
            lines = file.readlines() #almacenamos todas las lineas del fichero en la variable lines

        with open(file_name, "w") as file:
            for line in lines:              #recorremos las lineas del fichero y si el nombre coincide con el que hemos introducido, lo actualizamos y si no lo dejamos igual
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n") #si el nombre coincide con el que hemos introducido, lo actualizamos
                else:
                    file.write(line) #si no coincide, lo dejamos igual

        #lo que hizo aqui nuestro fichero fue primero leer todo el contenido, guardado en la variable lines que es un array con los datos introducidos, y luego paso a write , que lo hace es borrar el fichero y volver a escribirlo con las lineas que le hemos pasado


    elif option == "4":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name: #si el nombre no coincide con el que hemos introducido, lo dejamos igual y si coincide lo eliminamos por eso le dejo con !=
                    file.write(line)
        
        #hace el mismp procedimiento solo que en este caso si el nombre coincide con el que hemos introducido, lo eliminamos 

    elif option == "5":
        with open (file_name,"r") as file:
            print(file.read())  #asi ya podemos ver el contenido del fichero por terminal


    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():  #revision de todas las lineas del fichero
                components = line.split(", ") #almacenamos en la variable components los elementos de la linea separados por la coma que se volveria un array
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)

        #lo que pasa aqui es que recorremos todas las lineas del fichero y vamos sumando el precio por la cantidad de cada producto , gracias a split que nos permite separar los elementos de la linea por la coma y acceder a ellos por su indice


    elif option == "7":
        name = input("Nombre: ")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
                    break
        print(total)

       #en este caso es el mismo procedimiento que en la opcion 6 solo que en este caso solo sumamos el precio por la cantidad del producto que hemos introducido  

    elif option == "8":
        os.remove(file_name)
        break
    else:
        print("Selecciona una de las opciones disponibles.")
        

