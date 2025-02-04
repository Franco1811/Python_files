# #04 CADENAS DE CARACTERES
"""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 */
"""

s1= "Hola"
s2= "Python"

#Concatenación 
print(s1 + ", " + s2 + "!")

#Repetición
print(s1 + s1 + s1)
print(s1 * 3)

#Indexación (acceder a un carácter completo de una cadena de texto)
print(s1[0]+s1[1]+s1[2]+s1[3]) 
print(s1[0])

#Longitud
print(len(s2))

#Slicing(porción)
print(s2[2:6])
print(s2[2:]) #llega hasta el final
print(s2[:2]) #empieza desde el comienzo de la cadena de texto 

#Búsqueda
print("a" in s1) 
print("hon" in s2)

#Reemplazo
print(s1.replace("o", "a")) #el segundo valor reemplaza al primero

#División 
print(s2.split("t")) #Corta por el valor q introduzco

#Mayusculas, minusculas y letras en mayúscula
print(s1.upper())
print(s1.lower())
print("franco gonzalez".title()) #primera letra de cada palabra en mayúscula
print("franco gonzalez".capitalize()) #solo la primera letra

#Eliminación de espacios al principio y al final
print(" franco gonzalez ".strip())

#Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3="Franco Emerson Gonzalez Poma"

#Búsqueda de posicion
print("Franco Emerson Gonzalez Poma".find("Emerson"))
print("Franco Emerson Gonzalez Poma".find("Gonzalez"))
print("Franco Emerson Gonzalez Poma".find("G"))  #se queda con la primera ocurrencia que coincide con el criterio de busqueda

#Búsqueda de ocurrencias
print(s3.lower().count("m")) #nos cuenta la cantidad del caracter que coloquemos

#Formateo
print("Saludo: {} , lenguaje: {} !".format(s1,s2)) #concatena 

#Interpolación
print(f"Saludo: {s1} , lenguaje: {s2} !") #con la f todo lo que este entre llaves es una variable

#Transformación en lista de carácteres
print(list(s3))  #crea una lista con cada uno de los carácteres

lista1=[s1, ", ", s2, "!"]

#Transformación de lista en cadena de texto
print("".join(lista1)) #una esta lista siguiendo el criterio del espacio en blanco

#Tranformaciones númericas
s4="123456.123"
s4=float(s4)
print(s4)

#Comprobaciones varias
s4="123456"
print(s1.isalnum()) #si contiene letras y/o numeros vota true
print(s1.isalpha()) #si contiene solo letras vota true
print(s4.isalpha())
print(s4.isnumeric()) #si es un numero vota true


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos(palabra o frase que esta dispuesta que se lee de la mismo forma este recto o al reves)
 * - Anagramas(Cambio en el orden de las letras de una palabra o frase que da lugar a otra palabra.)
 * - Isogramas( palabra o frase en la que cada letra aparece el mismo número de veces)quiere decir cada letra se repite una vez
"""

def check(word1:str , word2:str):

    #Palíndromos
    #print(word2[::-1]) #usando slicing para ir de atras hacia adelante
    print(f"¿{word1.title()} es un palíndromo=: {word1 == word1[::-1]}")
    print(f"¿{word2.title()} es un palíndromo=: {word2 == word2[::-1]}")

    #Anagramas
    print(f"¿{word1.title()} es anagrama de {word2.title()} : {sorted(word1) == sorted(word2)}")
    #print(sorted(word1))  #retorna la cadena de caracteres en orden en una nueva lista

    #Isograma
    print(f"¿{word1.title()} es un isograma : {len(word1) == len(set(word1))}") #pongo set ya que si se repite entonces los sets lo consideran como uno y no tendria igualdad con el len
    print(f"¿{word2.title()} es un isograma : {len(word2) == len(set(word2))}")


    word_dict = dict() 
    for word in word1:
        word_dict[word] = word_dict.get(word, 0) + 1 #cada vez que acceda le sume 1 pero empiece de 0 para contar cada uno de sus caracteres

    print (word_dict)
    
    word_dict = dict() 
    for word in word2:
        word_dict[word] = word_dict.get(word, 0) + 1 #cada vez que acceda le sume 1 pero empiece de 0 para contar cada uno de sus caracteres

    print (word_dict)


check("radar", "pythonpythonpythonpython")
#check("amor", "roma")

