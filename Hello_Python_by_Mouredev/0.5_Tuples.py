### Tuples ###
"si escribimos solo parentesis es un tupla"
"si escribimos tupla con parentesis es una tupla"
"Estructura fija de valores"
"la tupla es un conjunto de valores"
"Tuplas y list admiten repetidos"
"Tuplas y list son ordenados"


my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.71, "Franco", "Gonzalez", "Franco")
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Franco"))
"para contar la cantidas de veces q se repite una palabra"

print(my_tuple.index("Gonzalez"))
"Sirve para ubicar el indice de la palabra ingresada"
"Si hubiese mas de uno se queda con el primero"

#my_tuple[1] = 1.80   'tuple' object does not support item assignment
print(my_tuple)
"La principal diferencia entre tuplas y listas es que es inmutable"
"Podemos guardar datos pero es un conjunto de valores cerrado"

my_sun_tuple = my_tuple + my_other_tuple
print(my_sun_tuple)
"No he podido modificarlas pero las he sumado"

print(my_sun_tuple[3:6])

my_tuple = list(my_tuple) 
print(type(my_tuple))
"Lo cambiamos de una tupla a una lista"

my_tuple[4]="Mouredev"
my_tuple.insert(1, "Azul")
print(my_tuple)
"Como ahora es una lista se le puede agregar y cambiar valores"

my_tuple =tuple(my_tuple)
"Lo volvi a cambiar a tupla"
"Cuanto mas inmutable mejor para que sea mas seguro"
"Pero en caso necesites cambios lo puedes cambiar a una lista"


print(my_tuple)
print(type(my_tuple))
"Lo volvi a cambiar a tupla"
"Cuanto mas inmutable mejor para que sea mas seguro"
"Pero en caso necesites cambios lo puedes cambiar a una lista"

#del my_tuple[2]
"No podemos eliminar un elemento de una tupla"

del my_tuple  #name 'my_tuple' is not defined
#print(my_tuple)
"del sirve para borrar la variable"




"La funcion clear sirve para eliminar todos los elementos de una lista, diccionario o conjunto"
