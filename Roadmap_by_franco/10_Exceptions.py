#EXCEPCIONES

#Controlar errores
#Es un mecanismo que permite manejar errores en tiempo de ejecución
#En python se manejan con try y except
#try: intenta hacer algo
#except: si no puede hacerlo hace algo
#finally: se ejecuta siempre

"""
/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
"""
#EJEMPLO PROPIO
try :
    print(10/1)
    my_list = [1,2,3,4]
    print(my_list[4])

except Exception as error: #Captura cualquier tipo de error
    print(f"Se ha producido un error: {error}({type(error).__name__})") #Este bloque solo se lanza si en el try se produce un error 
    #Captura el error y lo imprime
    #El e es una variable que guarda el error que se ha producido/ el sistema es capaz de identificar el error y lo guarda en e
    print(type(error))
finally:
    print("Fin de la ejecución")


#EJEMPLO CON LA DIVISIÓN

a = 5
b = 0
try:
    # Intenta ejecutar el código que podría generar un error
    resultado = a / b  # Intentando dividir por cero
except ZeroDivisionError as error:
    # Captura la excepción específica y maneja el error
    print(f"Error: {error}")
else:
    # Este bloque se ejecuta si no hay excepciones
    print(f"La división fue exitosa: {resultado}")
finally:
    # Este bloque se ejecuta siempre, independientemente de si hubo una excepción o no
    print("Fin del manejo de excepciones")


#EJEMPLO CON LA LISTA

lista = [1, 2, 3]
try:
    # Intenta acceder a un índice no existente de una lista
    elemento = lista[4]  # Intentando acceder a un índice no existente
except IndexError as error:
    # Captura la excepción específica y maneja el error
    print(f"Error: {error}")
else:
    # Este bloque se ejecuta si no hay excepciones
    print(f"Elemento obtenido: {elemento}")
finally:
    # Este bloque se ejecuta siempre, independientemente de si hubo una excepción o no
    print("Fin del manejo de excepciones")


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */
"""
print("EJERCICIO EXTRA")

#cuando me paso de indice es un error de tipo indexerror


#cree una clase que me sirva para controlar errores de tipo string
class StrTypeError(Exception): #creo una clase que hereda de la clase Exception
    pass

def process_params(parameters: list):
    if len(parameters) < 3:
        raise IndexError() #raise sirve para lanzar un error
    elif parameters[1] == 0:
        raise ZeroDivisionError() #capturo el error de división por cero
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser un string") #capturo el error de tipo string/ tengo una excepcion personalizada
    
    #es una manera manual de controlar errores
    #ya hemos por un lado EVITADO el error de división por cero y por otro lado el error de indice antes de que fallara el programa.


    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)

try:              #y aqui capturo el error que se ha producido
    process_params([1, 2, 3, 4])  #Brais estaba en el 3 para generar el error personalizado


except IndexError as error:  #capturo solo el tipo de error de indice
    print("El numero de elementos d ela lista debe ser mayor que dos")


except ZeroDivisionError as error:  #capturo solo el tipo de error de división por cero
    print("El segundo elemento de la lista no puede ser un cero")


except StrTypeError as error: #capturo mi excepcion personalizada de tipo string
    print(f" {error}")


except Exception as error: #Es buena practica capturar todos los errores haciando referencia a la clase padre de los errores (Exception)
    print(f"Se ha producido un error inesperado: {error}")


else: #este bloque se ejecuta si no se ha cumplido ninguna de las condiciones anteriores
    print("No se ha producido ningún error")


finally: #este bloque se ejecuta siempre
    print("El programa finaliza sin detenerse")

#se ha producito un error inesperado porque el tercer elemento de la lista es un string y no un número pero fue capturado por el bloque exception.

#En total tendriamos 4 bloques de excepciones, 2 son propias del sistema (indexerror y zerodivisionerror) y 1 personalidad y 1 general (exception) como buena practica
 #el else quizas no lo tengan todos los programas pero es una buena practica para saber si se ha producido un error o no  
