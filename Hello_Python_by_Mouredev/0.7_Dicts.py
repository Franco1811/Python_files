### Dictionaries ###

# ojo #
"""La forma corta de definir listas es con corchete[], tuplas son
parentesis() y en el caso de los sets son las llaves{}"""

my_dict = dict()
my_other_dict= {}
print(type(my_dict))
print(type(my_other_dict))


"forma para empezar a trabajar con un diccionario"
my_other_dict = {"Nombre":"Franco","Apellido":"Gonzalez","Edad":22, 1:"Python"}

"se acomodan los valores en relacion de tipo clave-valor"
"como definimos una clave y le asocio un valor"
"Una estructura para relacionar datos"
"no es fuertemente tipado"

my_dict = {
    "Nombre":"Franco",
    "Apellido":"Gonzalez",
    "Edad":22, 
    "Lenguaje":{"Python","Swift","Kotlin"},
    1:1.77
    }
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
"Esta es la peculariedad de los diccionarios"
"Facilidad para acceder a un elemento"

my_dict["Nombre"]="Emerson"
print(my_dict["Nombre"])
"Actualizamos la clave de esta manera en nombre"

print(my_dict[1])

my_dict["Calle"]="Daniel Alcides"
print(my_dict)
"Se le puede agregar un nuevo valor al diccionario asi"

#Operaciones#
del my_dict["Calle"]
print(my_dict)
"Podemos eliminar un elemento del diccionario de esta forma"
"Los delete no se pueden recuperar"

print("Franco" in my_dict)
"Sale falso pq de esta forma estamos buscando por clave, no por valor"
print("Apellido" in my_dict)
"Ahora si colocamos por clave"

print(my_dict["Apellido"])
"Esta si es la forma directa de acceder a un valor"
print("Francu" in my_dict)

#Operaciones#
print(my_dict.items())
"Nos retorna el diccionario de items en un listado"

print(my_dict.keys())
"Solo nos retorna las keys osea nombre,apellido,etc"

print(my_dict.values())
"Solo nos retorna todos los valores como emerson,gonzalez,etc"



my_new_dict = dict.fromkeys(("Nombre",1,"Piso"))
print(my_new_dict)
"Se ha creado un diccionario nuevo sin valores"
"De esta forma podemos crear un diccionario"


