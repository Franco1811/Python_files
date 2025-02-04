#mas ejercicios

# 1. Eliminar duplicados: Escribe un programa que pida al usuario una lista de números (separados por comas) y elimine cualquier número duplicado, mostrando el resultado sin repeticiones.


def eliminar_duplicados():
    lista = input("Ingrese una lista de numeros separados por comas: ")
    lista = lista.split(",") #separo los numeros por comas
    lista = list(set(lista)) #convierto la lista en un conjunto para eliminar los duplicados y luego la vuelvo a convertir en lista
    print(lista)
#eliminar_duplicados()


# 2 . Invertir una cadena: Crea un programa que reciba una cadena de texto del usuario y la imprima al revés.

def invertir_cadena():
    cadena= input("Introduce una cadena de texto: ")
    cadena_invertida=cadena[::-1]
    print(cadena_invertida)
#invertir_cadena()


# 3 . Palíndromo: Pide al usuario una palabra y determina si es un palíndromo (una palabra que se lee igual al derecho y al revés).

def buscador_palindromo():
    palabra= input("Introduce una palabra: ")
    print(f"La palabra {palabra} es palindromo : {palabra == palabra[::-1]}")
#buscador_palindromo()


# 4 . Fibonacci hasta N: Pide al usuario un número N y genera la secuencia de Fibonacci hasta que el valor sea mayor o igual a N.

def fibonacci():
    numero=int(input("Ingrese un numero: "))
    a,b=0,1                       #defino los dos primeros numeros de la secuencia
    while a<numero:               #mientras el numero sea menor al numero ingresado
        print(a) 
        a,b=b,a+b                 #la suma de los dos numeros anteriores
#fibonacci()

# 5 . Sumar solo números positivos: Solicita al usuario una lista de números separados por comas y calcula la suma de solo los números positivos.

def suma_positivos():
    lista = input("Ingrese una lista de numeros separados por comas: ")
    lista = lista.split(",") #separo los numeros por comas
    suma= 0
    for numero in lista:
        numero=int(numero) #convierto el numero en entero
        if numero>0: 
            suma+=numero
    print(f"La suma de los numeros positivos es: {suma}")
#suma_positivos()

# 6 . Conversión de mayúsculas y minúsculas: Pide al usuario una oración y luego muestra la misma oración alternando mayúsculas y minúsculas (ejemplo: "Hola Mundo" → "hOlA mUnDo").

def conversion_mayusculas_minusculas():
    oracion=input("Ingrese una oracion: ")
    oracion=oracion.swapcase() #convierto las mayusculas en minusculas y viceversa
    print(oracion)
#conversion_mayusculas_minusculas()

# 7 . Calculadora de descuento: Crea un programa que solicite al usuario el precio de un producto y un porcentaje de descuento. Calcula y muestra el precio final después de aplicar el descuento.

def calculadora():
    precio= input("Ingresa el precio del producto: ")
    descuento= input ("Ingresa el descuento a aplicar: ")
    precio_final= float(precio) - (float(precio)*float(descuento)/100) #calculo el precio final
    print(f"El precio final con el descuento aplicado seria de: {precio_final} soles")
#calculadora()

# 8 . Adivina la palabra: Define una palabra secreta en el código y permite que el usuario intente adivinarla. Por cada intento, informa si la palabra es alfabéticamente mayor o menor que la palabra secreta, hasta que el usuario acierte.

def adivina_palabra():
    palabra_secreta = "python"
    while True: #bucle infinito
        palabra = input("Adivina la palabra secreta: ")
        if palabra == palabra_secreta:
            print("¡Adivinaste!")
            break
        elif palabra < palabra_secreta:
            print("La palabra secreta es mayor")
        else:
            print("La palabra secreta es menor")
#adivina_palabra()

# 9 . Pide al usuario un número de segundos y convierte esa cantidad en horas, minutos y segundos (ejemplo: 3600 segundos → 1 hora, 0 minutos, 0 segundos).

def convertidor():
    segundos = int(input("Ingrese una cantidad de segundos: "))
    horas = segundos // 3600 # la division entera de los segundos entre 3600, por ejemplo 60//80 es 0

    minutos = (segundos % 3600) // 60  # los minutos si fueran por ejemplo 120 %3600 seria 120, 120//60 seria 2
    segundos = (segundos % 3600) % 60  # los segunddos si fuera por ejemplo 120/3600 seria 120, 120%60 seria 0
    print(f"{horas} horas, {minutos} minutos, {segundos} segundos")
#convertidor()

# 10 . Crea un juego de "piedra, papel o tijeras" entre el usuario y la computadora. La computadora deberá hacer una elección aleatoria, y el programa debe informar quién ganó.

def juego():
    import random  #importo la libreria random para que la computadora elija una opcion aleatoria
    opciones = ["piedra", "papel", "tijeras"] #defino las opciones en una lista
    computadora = random.choice(opciones) #la computadora elige una opcion aleatoria
    usuario = input("Elige piedra, papel o tijeras: ")
    print(f"La computadora eligió: {computadora}")
    if usuario == computadora:
        print("Empate")
    elif usuario == "piedra" and computadora == "tijeras":
        print("Ganaste")
    elif usuario == "papel" and computadora == "piedra":
        print("Ganaste")
    elif usuario == "tijeras" and computadora == "papel":
        print("Ganaste")
    else:
        print("Perdiste")
#juego()