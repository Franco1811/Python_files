### Sets ###

my_set = set()
my_other_Set = {}
"Tendriamos la creacion de un set"
"con parentesis sale set, con llaves sale dictionary y con corchetes sale list"
"Tener cuidado con los tipados"

print(type(my_set))
print(type(my_other_Set)) #nos dice inicialmente q es un dict

my_other_Set = {"Franco", "Gonzalez", 22}
print(type(my_other_Set))

print(len(my_other_Set)) 
"Contar los elementos"

my_other_Set.add("Artanis")
print(my_other_Set)
"Un set no es una estructura ordenada y no es inmutable"
"Por eso no se puede accedder a la ubicacion exacta de los elementos 0 o 1 como en las listas"
"La forma que tienen los sets de guardar elementos es desordenado"

my_other_Set.add("Artanis")
print(my_other_Set)
"Un set no admite repeticiones"
"Tuplas y list admiten repetidos"
"Tuplas y list son ordenados"


print("Franco" in my_other_Set) 
print("France" in my_other_Set)
"tenemos la posibilidad de hacer busquedas y nos suelta el true or false"

my_other_Set.remove("Franco")
print(my_other_Set)
"Podemos eliminar elementos"

my_other_Set.clear()
print(len(my_other_Set))
"el clear borra todos los elementos, lo deja en 0"

del my_other_Set #del sirve para eliminar completamente 
#print(my_other_Set) 
"Nos hemos cargado el programa"
"Borrar un objeto por completo"

my_set = {"Franco", "Gonzalez", 22}
my_list=list(my_set)
print(my_list)
print(my_list[0]) 
"Transformaciones de set a list pero es muy arriesgado pq no sabemos las posiciones de los valores correctos"
 
my_other_Set = {"Kotlin", "Swift", "Python"}
my_new_Set= my_set.union(my_other_Set)
print(my_new_Set.union(my_new_Set).union(my_set).union({"JavaScript", "Ca"}))
"Le tratamos de agregar nuevamente el mismo valor pero no se puede pq no se duplican"


"No sale javascript pq lo pusimos en el print, no lo almacenamos"
print(my_new_Set.difference(my_set))

