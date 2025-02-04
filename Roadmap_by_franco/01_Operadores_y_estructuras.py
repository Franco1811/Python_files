"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 """

"""Operadores Ariméticos"""
a=10
b=3

print (f"Suma: 10+3 ={a + b}")
print (f"Resta: 10-3 ={a - b}")
print (f"Multiplicación: 10*3 ={a * b}")
print (f"División: 10/3 ={a / b}")
print (f"Módulo: 10%3 ={a % b}") #vendria a ser el resto de la división
print (f"Exponente: 10**3 ={a ** b}")
print (f"División entera: 10//3 ={a // b}") #Devuelve el cociente

"""Operadores de comparación"""

print (f"Igualdad: 10 == 3 es {a == b}")  #comparar valores de variables , valores de cadenas de texto,etc
print (f"Desigualdad: 10 != 3 es {a != b}")  
print (f"Mayor que: 10 > 3 es {a > b}")
print (f"Menor que: 10 < 3 es {a < b}")
print (f"Mayor o igual que: 10 >= 10 es {a >= a}")
print (f"Menor o igual que: 10 <= 3 es {a <= b}")

"""Operadores de lógicos"""
print (f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}") # permite que 2 condiciones sean iguales
print (f"OR || : 10 + 3 == 14 and 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}") # pide q por lo menos una de las condiciones sea true
# || con alt 124
print (f"NOT ! :not  10 + 3 == 14 es {not 10 + 3 == 14 }") #esto indica que seria true en caso no se cumpliera la condición ya que esta negada

"""Operadores de asignación"""

my_number= 11
print (my_number)
my_number += 5 # suma y asignación
print (my_number)
my_number -= 1 # resta y asignación
print (my_number)
my_number *= 2 # multiplicación y asignación
print (my_number)
my_number /= 3 # división y asignación
print (my_number)
my_number %= 3 # módulo y asignación
print (my_number)
my_number **= 3 # exponente y asignación
print (my_number)
my_number //= 1 # división entera y asignación
print (my_number)

"""Operadores de identidad"""

#my_new_number = 1.0    en este caso salia false pq tienen diferentes direcciones de memoria
my_new_number = my_number
print (my_new_number)
print (f"my_number is my_new_number = {my_number is my_new_number}")
print (f"my_number is not my_new_number = {my_number is not my_new_number}")
# se puede aplicar a cadenas de texto, objetos , etc


"""Operadores de pertenencia"""

print (f"'f' in 'franco'= {'f' in 'franco'}")
print (f"'b' not in 'franco'= {'b' not in 'franco'}")

"""Operadores de bit"""

d=10 #1010 en binario ambps
e=3 #0011
print(f"AND : 10 & 3 = {10 & 3}") #  compara bit con bit y si ambos son 1 entonces es 1, caso contrario es 0
#daria como respuesta 0010 que vendria a ser el 2

print(f"OR : 10 | 3 = {10 | 3}") #compara y si uno de los 2 bits es 1 es igual a 1
#daria como respuesta 1011 que vendria a ser el 11

print(f"XOR : 10 ^ 3 = {10 ^ 3}") #compara y si los bits son dif es resultado es 1
#daria como respuesta 1001 que vendria a ser el 9
#alt94 = ^  codigo ascii

print(f"NOT : ~10 = {~10}") #invierte el valor bit a bit sobre la representacion del 10
#alt126 = ~  codigo ascii

print(f"Desplazamiento a la derecha : 10 >> 2 = {10 >> 2}") #1010 = 0010 que vendria a ser 2
print(f"Desplazamiento a la derecha : 10 << 2 = {10 << 2}") #1010 = 101000 eso seria 40 en binario 


"""
Estructuras de control

"""

#Condicionales

my_string= "Emerson" 
if my_string == "Franco":
    print("my_string es 'franco'")
elif my_string == "Emerson":        # es una comprobacion intermedia
    print("my_string es ´Emerson´")
else:
    print("my_string no es 'Franco' ni 'Emerson´")

#Iterativas

print("TRABAJANDO CON FOR ")
for i in range (11): # nos bota los numeros hasta uno menos el q colocamos en el rango
    print(i)

print("TRABAJANDO CON WHILE ")
i=0
while i<=10:
    print(i) 
    i+=1

#Manejo de excepciones

try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


""""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 """

for number in range(10,56):
    if(number % 2 ==0 and number !=16 and number %3 !=0): #si el modulo(restos) con  3 es distinto de 0 entra en la condicion
        print(number)
    