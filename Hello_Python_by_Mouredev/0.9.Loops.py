### Loops/Bucles/Ciclo ###
"""Nos sirve para iterar osea para repetir algo"""

# While 
my_condition = 0

#No se puede empezar con else

while my_condition < 10: #Repetira 0 en bucle pq la condicion se seguira cumpliendo
    print(my_condition)  #Si la condicion no cambia se mantendra en bucle
    my_condition += 2    #Va aumentando segun la cantidad q se coloca hasta q no cumpla la condicion
else: #Es opcional
    print("Mi condición es mayor o igual que 10") #Cuando pasa la condicion va por el else(algo que no tienen todos los lenguajes)

print("La ejecución continua")  


while my_condition < 20: #se va a repetir en funcion de una condicion
    my_condition += 1
    if my_condition==15:
        print("Mi condición es 15")
        break #sirve para detener la ejecucion si o si ya sea while o for

    print(my_condition)
print("La ejecución continua")



#For
"""nos sirve para iterar un listado de elementos"""
my_list= [35, 24, 62, 52, 30, 30, 17]

for element in my_list: #el for se va a repetir tantas veces como elementos tengamos iterables
    print(element)
""""Nos imprime cada uno de los elementos de la lista"""
""""Esta atado a un número finito de datos"""

my_tuple = (22, 1.77, "Franco", "Gonzalez", "Franco")
for element in my_tuple:
    print(element)

my_set= {"Franco", "Gonzalez", 22}
for element in my_set:
    print(element)

my_dict={"Nombre":"Franco","Apellido":"Gonzalez","Edad":35,1:"Python"}
for element in my_dict:
    print(element)
    if element == "Edad" :
        break #Si aparece un elemento llamado edad detiene el bucle
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continua")


#otro ejemplo con continue
for element in my_dict:
    print(element)
    if element == "Edad" :
        continue  #Ha realizado una especie de break, solo deteniendo la ejecucion en ese punto 
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continua")