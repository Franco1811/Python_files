# Variables

my_string_variable = "My string variable"
print(my_string_variable)

"""Forma correcta de nombrar una variable / string significa cadena """

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

""""El str me sirvio para transformar my int variable 
en una cadena de texto """

my_bool_variable = True
print(my_bool_variable)
""""No es una compilación, es una interpretación de python"""

# Concatenación de variables en un print 
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:",my_bool_variable)
"""Se le puede concatenar variables"""

# Funciones del sistema
#Funcion len
print(len(my_int_to_str_variable))
print(len(my_string_variable))
"""Len cuenta los caracteres segun sus valores/ incluye los espacios"""

# Variables en una sola linea ¡Cuidado con abusar de esta sintaxis!
name , surname , alias , age = "Franco" , "Gonzalez" , "Yo" , 22
print("me llamo:",name,surname,"mi edad es:" ,age, "y mi alias es:", alias)

#Funcion input
"""Introducir datos mas que todo para aplicaciones, scripts
o algo q ejecute"""
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

name_tag= input("introduce tu id de dotita")
print ("su name tag es: ",name_tag )

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address: int = 32
print(type(address))