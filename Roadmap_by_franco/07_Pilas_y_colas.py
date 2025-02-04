#7 PILAS Y COLAS
#Estructuras básicas/fundamentales 
"""
* EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
"""

#PILAAAA
"""
    Pila/stack(LIFO:last in first out): Estructura que va apilando elementos de forma descendente, osea ultimo
    en ingresar , primero en salir.
"""

stack = []
#PUSH
#cada vez que metemos un elemento =push
stack.append("1") 
stack.append("2")  
stack.append("3")
print(stack)


#POP
#accion de desapilar un elemento= pop
stack_item=stack[len(stack)-1] #aqui seria 3 elementos -1 = 2 pq seria la posicion 2 en la lista 
del stack[len(stack)-1]  #del para eliminar el elemento del indice 2 que seria el 3
print(stack_item)

print(stack.pop()) #en python ya tiene el mecanismo de pop en la lista, q elimina el ultimo elemento

print(stack)


#COLAAA
"""
    Cola/Queue(FIFO:firts in first out): Estructura que va apilando elementos de forma ascendente,primero 
    en ingresar , primero en salir.
"""

queue= []

#Enqueue
#Accion de añadir elementos = encolar
queue.append(4)
queue.append(5)
queue.append(6)
print(queue)

#Denqueue
#Accionar de quitar elementos = desencolar
queue_item=queue[0]
del queue[0]
print(queue_item) #manera de eliminar el primer elemento de forma manual

print(queue.pop(0)) # tenemos que colocar 0 para q elimine el primer elemento de la lista

print(queue)

"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
"""
#WEB
def web_navigation():
    stack = []
    while True: #para que esto se ejecute en un bucle infinito

        action = input("Añada una URL o interactúa con palabras adelante/atrás/salir : ")

        if action == "salir":
            print("SALIENDO DEL NAVEGADOR WEB")
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack)>0: #tiene que ser positivo
               stack.pop()   #se ha cargado al ultimo elemento y ha sido capaz de quedarse con el anterior      
        else: 
            stack.append(action)

        if len(stack)>0:
            print(f"Haz navegado a la web: {stack[len(stack)-1]}")  #se van almaccenando lo que vas llenando
        else:
            print("Estas en la página de inicio")


#web_navigation()


"""
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

def shared_printed():
    queue=[]
    while True: #para que esto se ejecute en un bucle infinito

        action = input("Añade un documento o selecciona imprimir/salir : ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue)>0: #para que imprima siempre y cuando tenga mas de un elemento
               print(f"Imprimiento: {queue.pop(0)}")  #de esta manera imprime el primer elemento
        else: 
            queue.append(action) #le agrega un documento

        print(f"Cola de impresion: {queue}")



shared_printed()