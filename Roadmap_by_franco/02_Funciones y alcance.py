# Reto #02 FUNCIONES Y ALCANCE

""" * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

#funcion = bloque de codigo

"""
Funciones definidas por el usuario
"""

#SIMPLE 
def greet():
    print ("Hola, Python")
greet()  #De esta manera llamo a la función


#CON RETORNO
def return_greet():
    return "HOLA PYTHON!"
greet = return_greet()  #o tambien directamente solo pongo print("return_greet")
print (greet)


#CON UN ARGUMENTO
def arg_greet(greet , name):
    print(f"{greet} ,{name}! ") # lo interpolamos con el argumento

arg_greet("Hi","Franquito")  #ya le di el valor a los argumentos


#CON UN ARGUMENTO PREDETERMINADO
def default_arg_greet(name="Pythonxd"):  # de esta manera si no le damos un valor votara python por defecto
    print(f"Hola ,{name}! ") # lo interpolamos con el argumento

default_arg_greet()            #sin parametro 
default_arg_greet("franquis")  #con parametro


#CON RETORNO DE VARIOS VALORES
def multiple_return_greet():
    return "Hola" , "Python"
greet, name = multiple_return_greet()
print(greet)
print(name)  # de esta manera retorna los valores separados


#FUNCIONES CON UN NUMERO VARIABLE DE ARGUMENTOS
def variable_arg_greet(*names): # con el * indica que podemos pasarle mas de un nombre , separados por comas
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Emerson" , "Max", "Comunidad") #de esta manera le puedo pasar todos los argumentos q yo quiera


#CON UN NUMERO VARIABLE DE ARGUMENTOS CON PALABRA CLAVE
def variable_key_arg_greet(**names): #Esto significa que cada argumento esta formado por una clave y un valor(**)
    for key, value in names.items():
        print(f" {value} ({key})!")

variable_key_arg_greet(
    languaje="Python",
    name="Emerson" , 
    apellido="Gonzalez",
    edad= 22   #de esta manera devuelve los valores mediante la clave
    )


"""
Funciones dentro de funciones

"""
def outer_function():
    def inner_function():
        print ("Funcion interna: Hi, Python! ")
    inner_function() #llamo a la funcion dentro de la funcion

outer_function()

"""
Funciones del lenguaje (build-in)

"""

print(len("Franco"))  # cuenta el numero de datos
print(type(36))  # nos dice el tipo de dato
print("franco".upper())  #vuelve mayuscula



"""
Variables locales y globales

"""

#concepto de ambito

global_variable= "Python"

print(global_variable)

def hello_python():
    local_variable= "hola"
    print(f"{local_variable}, {global_variable}!")


hello_python()
print (global_variable)
#print (local_variable) No se puede acceder desde fuera de la función


"""
* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1,101):
        if number%5 == 0 and number%3 ==0:
             print (text_1 + text_2)  
        elif  number %3 == 0:
             print (text_1)
        elif number%5 == 0:
             print (text_2)
        else:
             print (number)
             count +=1
    return count

print(print_numbers("Fizz","Buzz"))

    