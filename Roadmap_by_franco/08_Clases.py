# Clases

"""
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
"""

class Programmer:

    surname:str = None
    # inicializador: es lo que define lo valores iniciales de nuestra clase/objeto
    def __init__(self, name: str, age:int, languages:list) -> None:  #funcion reservada propia del sistema
        self.name = name           #le asignamos el parámetro 
        self.age=age
        self.languages=languages   #ahora son propiedades de clase

    def print(self):
        print(f"Nombre:{self.name} | Apellido: {self.surname} | Edad:{self.age} | Lenguaje: {self.languages} ") #accedo a los parametros mediante self

my_programmer = Programmer("Franco",22,["python","c#","SQL"])  #OBJETO INTELIGENTE
my_programmer.print() #ahora podemos acceder a las funciones de la clase programa

my_programmer.surname= "Gonzalez"  #agregamos parametros nuevos
my_programmer.print()

my_programmer.age= 23  #modificamos parametros
my_programmer.print()

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */
"""

#LIFO
print("CASO DE STACK/PILA ") 
class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, item):         #funciones de mi pila /stack
        self.stack.append(item)

    def pop(self):          #ponemos self para que todas las funciones se reciben a ellas mismas para poder interactuar con el contenido de la clase
        if self.count==0:
            return None
        
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
           print(item)

my_Stack= Stack()
my_Stack.push("A")
my_Stack.push("B")
my_Stack.push("C")

print(my_Stack.count())

my_Stack.print()

my_Stack.pop()   #desapila la c
print(my_Stack.pop()) #desapila la b
print(my_Stack.count())



#FIFO
print("CASO DE QUEUE/COLA ")

class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.count()==0:
            return None
        
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def print(self):
        for item in self.queue:
           print(item)


my_queue=Queue()
my_queue.enqueue("A")   #encolamos / agregramos valores
my_queue.enqueue("B")
my_queue.enqueue("C")

print(my_queue.count())

my_queue.print()

my_queue.dequeue()  #cumple la funcion dequeue ELIMINA LA A
print(my_queue.count())  #contamos cuantos tenemos
my_queue.print()  #se cumple FIFO (firs in first out)



 