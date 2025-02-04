### Strings (cadenas) ###

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string= """Este es un string \n con salto de linea"""
"\n = es un indicativo de un salto de linea(\=alt92)"
print(my_new_line_string)

my_tab_string= "\t Este es un string con tabulacion"
"""\t = es un indicativo de tabulacion(\=alt92)"""
print(my_tab_string)

my_scape_string= "\\t Este es un string \\n escapado"
"Es un string con salto de linea y tabulacion"
"Con doble barra se cancela el salto o tabulacion"
print(my_scape_string)


# Formateo
name,surname,age= "franco","gonzalez",22

print("Mi nombre es: {} {} y mi edad es {}".format(name,surname,age))
"alt123:para poner corchetes" 


print("Mi nombre es: %s %s y mi edad es %d" %(name,surname,age)) 

"nos ayuda ya que asegura q nuestros datos van a tener sentido"
"%s - String (or any object with a string representation, like numbers)"
"%d - Integers /numeros enteros"
"%f - Floating point numbers"
"""%.number of digitsf" - Floating point numbers with fixed precision"""


print("Mi nombre es "+ name, " " + surname, "y mi edad es" + str(age))
"No es la manera mas eficiente de hacerlo"


print(f"Mi nombre es: {name} {surname} y mi edad es {age}")
"poner la f sirve para formatear y para q infiera el valor de las variables"
"si estamos formateando es mejor definir el tipo de formato"


#Desempaquetado de caracteres
languaje= "python"  #tiene 6 caracteres la palabra python pa crear un desempaquetado
a,b,c,d,e,f = languaje
print(a)
print(b)

#División 
"p=0 y=1 t=2 h=3 o=4 n=5"
languaje_slice = languaje[1:3]
print(languaje_slice)
"para hacer corchetes alt91 y alt93"

languaje_slice = languaje[1:]
print(languaje_slice)

languaje_slice = languaje[-2]
print(languaje_slice)

languaje_slice = languaje[-1]
print(languaje_slice)

languaje_slice = languaje[0:6:2] #del 0 al 6 de 2 en 2
print(languaje_slice)

#Reverse

reversed_languaje = languaje[::-1] #empieza por -1 pq no hay un -0 como tal
print(reversed_languaje)

#Funciones

print(languaje.capitalize()) #pone en mayuscula la primera letra
print(languaje.upper())  #pone en mayuscula toda la palabra
print(languaje.count("t")) #me indica cuantas palabras hay segun la letra escogida
print(languaje.isnumeric()) #nos indica si es un numero o no
print("1".isnumeric())

print(languaje.lower()) #nos pone las palabras en minusculas
print(languaje.upper().isupper()) #Se concatenaron dos funciones
print(languaje.lower().isupper())
#upper es para poner en mayuscula
#issuper es para indicarnos si estan en mayuscula o no

print(languaje.startswith("Py")) 
#nos confirma si la palabra empieza de la manera q se indica