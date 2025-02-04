#Reto #03 ESTRUCTURAS DE DATOS
"""
EJERCICIO: ESTRUCTURAS DE DATOS
 - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 - Utiliza operaciones de inserción, borrado, actualización y ordenación.
   DIFICULTAD EXTRA (opcional):
  Crea una agenda de contactos por terminal.
 - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 - Cada contacto debe tener un nombre y un número de teléfono.
 - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
   los datos necesarios para llevarla a cabo.
 - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
   (o el número de dígitos que quieras)
 - También se debe proponer una operación de finalización del programa.
 """

"""
Estructuras por defecto en python
"""

#LISTAS 
print("LISTAS")
#estructura que sirve para guardar datos de manera ordenada
#listas siempre con corchetes

my_list= ["Franco", "Emerson","Max","Joshua"]
print(my_list)

#podemos manipular los datos de la sgnte manera:
my_list.append("Gonza") # INSERCION
print(my_list)          # agregamos un valor al final por defecto
my_list.remove("Franco") # ELIMINACIÓN
print(my_list)  
print(my_list[1]) #ACCESO  con los corchetes accedo a la posiciones

my_list[1]= "Cuervillo" #ACTUALIZACIÓN
print(my_list)

my_list.sort() #ORDENACIÓN sigue un criterio para ordenarlo
print(my_list) #como no hay nada lo hace alfabeticamente, en caso de numeros: ascendentemente
print(type(my_list))


#TUPLAS 
print("TUPLAS")
#estructuras para guardas datos pero son inmutables (muy seguras)
#tuplas siempre con parentesis

my_tuple = ("franco","gonzalez","conejo","22")
print(my_tuple[1])   #solo puedo acceder a los datos pero no cambiarlos
print(my_tuple[3])
print(type(my_tuple))

my_tuple=sorted(my_tuple)  #con sorted convertimos una tupla en una lista 
print(type(my_tuple))

my_tuple=tuple(sorted(my_tuple))  # poniendo() con el constructor tuple y volverlo tupla nuevamente
print(type(my_tuple))
print(my_tuple)


#SETS
print("SETS")
#estructuras desordenada / no te puedes confiar del orden / no es optimo para buscar datos
#siempre con llaves los sets

my_set= {"franco","gonzalez","conejo","22"}
print(my_set)
print(type(my_set)) 
my_set.add("Gonzalezpoma18@gmail.com")   #INSERCIÓN
my_set.add("Gonzalezpoma18@gmail.com")   #serializa los datos para evitar duplicador por lo que no aparecen 2 veces 1 dato
print(my_set)

my_set.remove("franco")  #ELIMINACIÓN
print(my_set)

my_set =set(sorted(my_set))   #no se puede ordenar
print(type(my_set))
#print(my_set[0])  no se puede pq no hay orden en los sets

 
#DICCIONARIOS
print("DICCIONARIOS")
#aqui no hay posiciones , aqui tenemos claves y valores
# tambien va con llaves como los sets

my_dic: dict= {
    "name":"franco",
    "surname":"gonzalez",
    "apodo":"conejo",
    "edad":"22"}
print(type(my_dic))

# my_dic[0] no hay posiciones
print(my_dic["name"])  #ACCESO :puedo acceder a los valores mediante las claves

my_dic["email"]="franco@gmail.com"  #INSERCION : de esta manera puedo incluir valores

my_dic["edad"]="25"   #ACTUALIZACION : mediante la clave puedo ingresar a cambiar el valor 
print(my_dic)

del my_dic["surname"]  #ELIMINACION : mediante la clave igualmente
print(my_dic)

my_dic=dict(sorted(my_dic.items())) #ORDENACION para diccionarios pero lo transforma en lsita a menos que ponga dic()
print(my_dic)
print(type(my_dic))


"""
EJERCICIO: ESTRUCTURAS DE DATOS
  Crea una agenda de contactos por terminal.
 - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 - Cada contacto debe tener un nombre y un número de teléfono.
 - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
   los datos necesarios para llevarla a cabo.
 - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
   (o el número de dígitos que quieras)
 - También se debe proponer una operación de finalización del programa.
 """


agenda = {
    "Ivan" : 625325408,
    "Juan" : 634728376,
    "Blanca" : 623746342,
    "Pepe" : 637289476,
    "David" : 671829354
}

def buscar(nombre):
    if nombre not in agenda:
        return "El contacto no existe"
    else:
        print(f"El numero de {nombre} es {agenda[nombre]}")

def insertar(nombre, telefono):
    agenda[nombre] = telefono

def actualizar(nombre, telefono):
    agenda[nombre] = telefono

def eliminar(nombre):
    agenda.pop(nombre)


while True:
    print("Que operacion desea realizar:")
    print("1. BUSCAR")
    print("2. INSERTAR")
    print("3. ACTUALIZAR")
    print("4. ELIMINAR")
    print("5. SALIR")
    opcion_elegida = int(input())

    if opcion_elegida == 1:
        nombre = input("Introduzca el nombre del contacto: ").capitalize()
        print(buscar(nombre))

    elif opcion_elegida == 2:
        nombre = input("Introduzca el nombre del nuevo contacto: ").capitalize()
        telefono = input("Introduzca el telefono: ")

        if len(telefono) > 9 or not telefono.isdigit():
            print("Error al introducir el telefono")
        else:
            insertar(nombre, telefono)

    elif opcion_elegida == 3:
        nombre = input("Introduzca el nombre del contacto que quiera actualizar: ").capitalize()
        telefono = input("Introduzca el nuevo telefono: ")
        actualizar(nombre, telefono)

    elif opcion_elegida == 4:
        nombre = input("Introduzca el nombre del contacto que quiera eliminar: ").capitalize()
        eliminar(nombre)

    elif opcion_elegida == 5:
        print("Salió del programa")
        break







   


