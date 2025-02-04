#Primera practica con Franco

# Documentacion de python
# https://python.org


# Nivel Básico (5 Ejercicios)
# 1 . Saludo personalizado: Crea un programa que pida al usuario su nombre y luego imprima un mensaje de saludo personalizado.

def saludo():
    name=input("Ingrese su nombre: ")
    print(f"Hola como esta, {name}?")
#saludo()


def saludo2(name):
    print(f"Hola como esta, {name}?")
saludo2("Franco")


# 2 . Edad en el futuro: Pide al usuario su edad y calcula cuántos años tendrá en 10 años.

def edad_actual():
    edad_Actual=int(input("Ingrese su edad: "))
    edad_futura=edad_Actual+10
    print(f"En 10 años tendras {edad_futura} años")
#edad_actual()


def edad_futura():
    actual=input("Que edad tienes?")
    print(f"Tu edad en 10 años será: {int(actual) + 10}")
#edad_futura()

def calculo_rapido(age):
    print (age +10)
calculo_rapido(20)


# 3 . Conversión de unidades: Escribe un programa que convierta una distancia en kilómetros a millas.

def conversion_km_to_milles():
    km= float(input("Ingrese la distancia en km:"))
    milles=km*0.621371
    print(f"La distancia ingresada en millas sera de : {milles}")
#conversion_km_to_milles()


#km=input("Ingrese la distancia en km:")
#print(f"La distancia en millas sera de: {float(km)*0.621371}")



# 4 . Adivina el número: Pide al usuario que ingrese un número del 1 al 10. Si el número es igual a 5, imprime "¡Adivinaste!" De lo contrario, imprime "Intenta de nuevo."

def adivina_numero():
    while True:
      numero=(float(input("Ingrese un numero del 1 al 10: ")))
      if numero>10 or numero<1:
          print("Elige un numero del 1 al 10")
      elif numero == 5:
          print("¡Adivinaste!")
          break
      else:
          print("Intenta nuevamente")
#adivina_numero()


# 5 . Cálculo de área de un rectángulo: Solicita al usuario ingresar el ancho y el alto de un rectángulo y luego calcula el área.

def area_rectangulo():
    largo=float(input("Ingrese el largo del rectangulo: "))
    ancho=float(input("Ingrese el ancho del rectangulo: "))
    area=largo*ancho
    print(f"El area del rectangulo es: {area}")
#15area_rectangulo()


# Nivel Intermedio (5 Ejercicios)

# 6 . Número par o impar: Crea un programa que pida al usuario un número y le indique si es par o impar.

def par_or_impar():
    numero=int(input("Ingrese un numero: "))
    if numero%2==0:
      print("El numero es par")
    else:
      print("El numero es impar")
#par_or_impar()


# 7 . Conteo regresivo: Haz un programa que reciba un número del usuario y cuente regresivamente desde ese número hasta cero, imprimiendo cada número.

def conteo_regresivo():
    numero = int(input("Ingrese un numero: "))
    while numero > 0:
        print(numero)
        numero = numero - 1  #or numero -= 1
#conteo_regresivo()

# 8 . Generador de tablas de multiplicar: Crea un programa que pida un número y genere la tabla de multiplicar de ese número, del 1 al 10.

def tabla_multiplicar():
    numero= int (input("Ingrese su numero:"))
    for i in range(1,11):  # el i va a ir subiendo hasta el rango que le indico 
        print(f"{numero} x {i} = {numero*i}") 
#tabla_multiplicar()

def tabla_multiplicar():
    numero= int (input("Ingrese su numero:"))
    n=1
    while n<=10:
        total=numero*n
        print(f"{numero} x {n} = {total}")
        n+=1
#tabla_multiplicar()

# 9 . Suma de elementos en una lista: Solicita al usuario ingresar varios números y almacénalos en una lista. Luego, calcula y muestra la suma total de esos números.

def suma_lista():
    lista=[]
    suma=0
    cantidad=int(input("Cuantos numeros desea ingresar: "))
    for i in range(cantidad):
        numero=int(input("Ingrese un numero: "))
        lista.append(numero)
        suma+=numero
    print(f"La suma de los numeros ingresados es: {suma}")

#suma_lista()

# 10 . Contador de vocales: Escribe un programa que pida una frase al usuario y cuente cuántas vocales hay en la frase.

def contador_vocales():
    frase=input("Ingrese una frase: ")
    vocales="aeiou"   #defino las vocales
    contador=0
    for letra in frase: #letra es una variable que va a ir recorriendo cada letra de la frase
        if letra in vocales:
            contador+=1
    print(f"La cantidad de vocales en la frase es: {contador}")
#contador_vocales()

#Nivel Avanzado (5 Ejercicios)

# 11. Ordenador de palabras: Pide al usuario una lista de palabras separadas por comas y ordénalas alfabéticamente, mostrándolas de nuevo separadas por comas.

def ordenador_palabras():
    palabras=input("Ingrese una lista de palabras separadas por comas: ")
    lista=palabras.split(",") #separa las palabras por comas
    lista.sort() #ordena la lista en forma alfabetica
    print(",".join(lista)) #une las palabras con comas nuevamente
#ordenador_palabras()

#join sirve para unir elementos de una lista en un string

# 12 . Números primos hasta N: Pide al usuario un número N y muestra todos los números primos hasta ese número.

def numeros_primos():
    numero= int(input("Ingrese un numero: "))
    for i in range(2,numero+1): #el rango va desde 2 hasta el numero ingresado
        for j in range(2,i): #el rango va desde 2 hasta el numero anterior al numero que estoy evaluando que en el primer caro seria 2, luego 3, 4, 5, etc hasta el numero ingresado, y el otro bucle va a ir recorriendo cada numero anterior al numero que estoy evaluando por ejemplo si estoy evaluando el 5 en el primer bucle el segundo bucle va a ir recorriendo desde 2 hasta 4 y si fuera el 6 va a ir recorriendo desde 2 hasta 5, y si fuera el 2 no va a recorrer ningun numero porque no hay numeros anteriores a 2 y seria primo
            if i%j==0: #si el numero es divisible por otro numero que no sea 1 o el mismo, no es primo
                break
        else:        #si no se cumple la condicion anterior, el numero es primo
            print(i)
#numeros_primos()


# 13 . Contador de palabras: Crea un programa que reciba una frase y cuente cuántas palabras contiene.

def contador_palabras():
    frase=input("Ingrese una frase: ")
    contador=1
    for letra in frase:
       if letra==" ":
            contador+=1
    print(f"La cantidad de palabras en la frase es: {contador}")
#contador_palabras()


# 14 . Diccionario de precios: Crea un pequeño diccionario de productos con precios. Luego pide al usuario el nombre de un producto y muestra su precio. Si el producto no existe, muestra un mensaje de error.

def diccionario_precios():
    productos={"manzana":10,"pera":20,"platano":50}
    producto=input("Ingrese el nombre de un producto: ")
    if producto in productos:
        print(f"El precio de {producto} es: {productos[producto]}")
    else:
        print("El producto no existe")
#diccionario_precios()


# 15 . Calculadora de promedio: Crea una calculadora que pida al usuario ingresar varias notas (separadas por comas), calcule el promedio y muestre el resultado.

def calculadora_de_promedio():
    notas=input("Ingrese varias notas separadas por comas: ")
    notas=notas.split(",")  # separa las notas por comas
    suma=0
    for i in notas: #for se usa en los casos donde lo que tengo que hacer se va a repetir una cantidad de veces determinada y si no fuera determinada se usaria while
        suma+=float(i) #suma las notas ingresadas y las convierte a float
    promedio=suma/len(notas) #calcula el promedio de las notas ingresadas dividiendo la suma de las notas por la cantidad de notas
    print(f"El promedio de las notas ingresadas es: {promedio}")
#calculadora_de_promedio()

lista= [1,2,3,4,5,6,7,8,9,10]
print(len(lista)) 