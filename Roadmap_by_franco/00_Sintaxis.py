# 1. Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación

# https://python.org

# 2. Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias)

# Esto es  un comentario en una línea

"""
Esto también es  
un comentario 
en varias líneas
"""

'''
Tambien se pueden 
poner comentarios
de esta forma
'''

# 3. Crea una variable (y una constante si el lenguaje lo soporta).

""" 
Para definir una varible en python solo tenemos que inicializar nombrando la variable y 
definir su valor despues de un signo igual:
"""
my_var = "Mi variable" 
my_var = "Nuevo valor de variable"


"""
No se puede definir una constante en python pero es una convención el nombrar una 
variable solo con mayusculas para establecer que no se debe modificar el valor de dicha variable:
"""
MY_CONSTANT = "Mi constante"  #Por convencion


# 4. Crea variables representando todos los tipos de datos primitivos del lenguaje 
# (cadenas de texto, enteros, booleanos...).

my_int = 150
my_float = 12.5
my_bool = True  #or false
my_string = "Wenas a todos" 
my_string = 'Hola, pythonn' #sale la segunda variable pq python es debilmente tipado

print (my_string)

# De esta manera llamamos al tipo de dato 
print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))