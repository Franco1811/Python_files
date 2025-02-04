### Lists ###
"si escribimos solo corchete es una lista"
"si escribimos list con parentesis es una lista"
"los corchetes se usan con las listas. si pones my_tuple[]= es una lista"
"Tuplas y list admiten repetidos"
"Tuplas y list son ordenados"
my_list = list()
my_other_list = []

print(len(my_list))
"Sale 0 pq la lista sirve para añadir elementos y todavia no tiene"
"En programacion siempre se empieza desde 0"

my_list = [35,24 ,62 ,52 , 30, 30 , 17]
print(len(my_list))

my_other_list = [22, 1.72, "Franco", "Gonzalez"]
"Puedo guardar en la lista todo tipo de datos"

print(type(my_list ))
print(type(my_other_list ))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30))
print(my_other_list.count("Franco"))
#print(my_other_list[-4]) IndexError
#print(my_other_list[-5]) IndexError
"Si me pasara de los rango seria error"


age, height, name, surname = my_other_list
print(name)

name, height, age , surname = my_other_list[2],my_other_list[1],my_other_list[0],my_other_list[3],
print(name)
print(age)
"Tener mucho cuidado con eso ya q induce a errores y complicarse"

print(my_list+my_other_list)
#print(my_list-my_other_list)

my_other_list.append("FrancoGonz")
print(my_other_list)
"Sirve para insertar al final de una lista"

my_other_list.insert(1, "Rojo")
print(my_other_list)
"Sirve para insertar un valor a la lista en el orden q gustes"

my_other_list[1]="Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)
"Sirve para remover un valor que sabemos q esta ahi"

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)
"Sirve para eliminar el ultimo valor por defecto"

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)
"De esta manera podemos eliminar un elemento de un lugar concreto pero retornando ese elemento"

del my_list[2]
print(my_list)
"con del podemos borrar el valor concreto poniendo su ubicacion(indice)"

my_new_list =my_list.copy()
"Sirve para copiar"

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)
"Sirve para ordenar los valores al reves "

my_new_list.sort()
print(my_new_list)
"Ordena la lista por defecto de menor a mayor"

print(my_new_list[1:3])
"Para crear sublistas"

my_list = "Hola Python"
print(my_list)
print(type(my_list))
"Se le llama tipado dinámico"
"Si le pongo corchetes se vuelve una lista"
