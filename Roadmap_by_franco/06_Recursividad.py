#6 RECURSIVIDAD

#La recursividad es una función que se llama a ella misma(que se ejecute una vez tras otra) recurrente
#Podemos encontrar una semejanza con las funciones recursivas , pues con los conceptos de buble, ciclo ,while
#for , etc

#Se debe tener sentido de cuando usar recursividad(que se llame a ella misma y se detenega en algun punto) y cuando usar bucles
"""
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
"""

def cuenta_Atras(number: int):
    if number>=0:
       print(number)
       cuenta_Atras(number-1)


cuenta_Atras(100)

"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
"""
#factorial
def factorial(number: int)-> int:
   if number < 0:
      print("Los numeros negativos no son válidos")
      return 0
   elif number == 0:
      return 1
   else:
      return number*factorial(number-1) #acumulamos el resultado    
   
print(factorial((5)))
 
#OTRA FORMA PARECIDA 
def rec_factorial(num:int,result=1):
    if num == 0:
        print (f"El factorial de {x} = {result}")
    else:
        return rec_factorial(num-1,result*num)

#x=int( input("Ingrese número que desea saber el factorial: "))
#rec_factorial(x)



#sucesion de fibonacci 0,1,1,2,3,5,8,13,21,34,55,89,144
def fibonacci(number: int)-> int:
   if number <= 0:
      print("La posición tiene que ser mayor que cero")
      return 0
   #elif number ==1 : #la posicion 1 es 0
      #return 0
   #elif number == 2: #la posicion 2 es 1
      #return 1
   #entonces mejor:
   elif number<=2:
      return number-1
   else: 
      return fibonacci(number-1)+fibonacci(number-2) 
   
   #la funcion se repite hasta ir a los primeros valores que ya conocemos en el anterior elif
   #de esta manera se reduce , haciendo bucle sería mas complicado
       
print(fibonacci(5))