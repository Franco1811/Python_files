### Exception Handling ###
"""Manejo de errores"""
 #tipado dinamico: significa que podemos cambiar los tipados de texto como string a entero, etc

numberOne = 5 
numberTwo = 1
numberTwo = "1"

if type(numberTwo) == int:
    print(numberOne + numberTwo)  #Python no es capaz de sumar 2 tipos de datos diferentes
else:
    print("No se cumplió")


#try except
try:
    print(numberOne + numberTwo)  #cuando usas try, la linea que da error al darse al cuenta salta a lo q tenemos en el except
    print("No se ha producido error") #No hemos podido sumar pero el programa no ha muerto ya que lo tenemos controlado contra los errores
except: 
    #Se ejecuta si se produce una excepcion                             
    print("Se ha producido un error")  #En caso no haya problema se ejecutara normalmente


#try except else
try:
    print(numberOne + numberTwo)
    print("No se ha producido error") 
except:                               
    print("Se ha producido un error")
else:
    #Se ejecuta si no se produce una excepcion
    #Solo se ejecuta si en el bloque de codigo entre el try y el except no se ha producido un ERROR
    print("La ejecución continúa correctamente") 

 
 #try except else finally
try:
    print(numberOne + numberTwo)
    print("No se ha producido error") 
except:                               
    print("Se ha producido un error")
else: #opcional
    print("La ejecución continúa correctamente") 
finally: #opcional
    #Se ejecuta siempre pase lo que pase
    print("La ejecución continúa")
                                               
#todos son bloques para manejar errores.
#No puedo evitar poner el except(si hay un try, hay un except) 
#de forma opcional el else y el finally
    


#Excepciones por tipo
try:
    print(numberOne + numberTwo)   
    print("No se ha producido error")
except ValueError:  #este bloque se ejecuta solo si se produce ValueError                   
    print("Se ha producido un ValueError")      
except TypeError:   #este bloque se ejecuta solo si se produce typeError(solo con este tipo de error)                  
    print("Se ha producido un TypeError") 

#Para poder controlar el tipo de error se produce, porque segun el tipo de error que se produzca nosotros
#queremos ejecutar un codigo muy concreto
    


#Captura de la informacion de la excepción
#Excepciones por tipo pero muy muy muy concretos
try:
    print(numberOne + numberTwo)   
    print("No se ha producido error")
except ValueError as error:        #tenemos un objeto error que nos dara informacion       
    print(error) 
except Exception as error: #si no es valueerror se ira por exceptcion 
    #ese error puede ser cualquier palabra(es un nombre que le damos a la variable que contiene la info del error)
    print(error)     
    

