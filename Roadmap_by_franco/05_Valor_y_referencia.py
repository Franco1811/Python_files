"""
Valor y referencia(value & pointers)
"""
'''
 * EJERCICIO:
 * X Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * X Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes) 
"""

"""
DEFINICIÓN:
Parámetros por referencia y valor, son aquellos parámetros que al entrar en una función se comportan de una
determinada forma, ya sea creando una copia de una variable y operando sobre ella (por valor) o bien operando 
directamente sobre el valor original y modificando la variable (por referencia)

Si bien los objetos que se obtienen en una variable original por referencia y el valor que resulta despues de entrar a una función
parecieran ser diferentes lo cierto es que son el mismo, ya que comparten la misma dirección en la memoria, esto lo podemos notar si
usamos la función "id()" que nos entrega el valor de memoria de cada objeto

'''
#Tipos de dato por valor (son mas que todo tipos de datos primitivos) valores / elementos unicos

#Las variables en un tipo de dato por valor estan en diferentes direcciones de memoria osea son independientes
#la una de la otra, cada una ocupa su posición de memoria

my_int_a=10
my_int_b=my_int_a
my_int_b=20
#my_int_a=30
print(my_int_a)
print(my_int_b)

#Tipos de dato por referencia (en python son todos los tipos de datos que no son primitivos como:listas, tuplas, dict,set,etc)

# ya que son datos que actuan como referencia estan en la misma dirección de memoria
# no se copia el valor, se queda con la direccion de memoria de la variable original , cuando se modifica
# la nueva variable , se modifica tmbn la variable original

my_list_a=[10,20]
my_list_b=my_list_a
my_list_b.append(30) #para agregar un valor

print(my_list_a) #los datos por referencia no copian el valor, heredan su posicion de memoria
print(my_list_b)


#Funciones con datos por valor
my_int_c=10

def my_int_func(my_int: int):
    my_int=20
    print(my_int)

my_int_func(my_int_c) #esta llamando la variable dentro de la funcion que lo modifica
print(my_int_c) #esta llamando solo la variable libre


#Funciones con datos por referencia
my_lits_c=[10,20]

def my_list_func(my_list : list): #el comportamiento es el mismo 
    my_list.append(30)

    my_list_d=my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_func(my_lits_c)  #aqui en ambos cason modifican el valor original por lo que es lo mismo en ambos casos
print(my_lits_c)

"""
 DIFICULTAD EXTRA (opcional):

 *   Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 *   Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 
 """

#POR VALOR

def value(value_a: int, value_b: int):
    temp=value_a
    value_a=value_b  # intercambiar valores de value_a y value_b
    value_b=temp
    return value_a,value_b

my_int_d=10
my_int_e=20   
my_int_f,my_int_g=value(my_int_d,my_int_e) #llamo los valores en otras 2 variables para luego mostrar el cambio luego de pasarlos por la funcion


print(f"{my_int_d}, {my_int_e}")  #se colocan variable f y g para mostrar el cambio 
print(f"{my_int_f}, {my_int_g}")


#POR REFERENCIA

def ref(value_a: list, value_b: list)-> tuple:
    temp=value_a
    value_a=value_b  # aqui funciona la logica pq almacenamos el value a en temp (nueva variable)
    value_b=temp
    value_b.append(50)  #si agregamos 50 se conserva el valor desde la variable original
   
    return value_a,value_b

my_list_e=[10,20]
my_list_f=[30,40]   
my_list_g,my_list_h=ref(my_list_e,my_list_f) #llamo los valores en otras 2 variables para luego mostrar el cambio luego de pasarlos por la funcion


print(f"{my_list_e}, {my_list_f}")  #se colocan variable f y g para mostrar el cambio 
print(f"{my_list_g}, {my_list_h}")

