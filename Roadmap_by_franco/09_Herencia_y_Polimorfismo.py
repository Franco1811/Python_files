# Reto #09 Herencia y polimorfismo

#Herencia: 
# Es un mecanismo que permite generar una jerarquia entre clases (permiten heredar atributos,propiedades, metodos o funciones)
#Sirve para promover esa reutilizacion de código y permite crear nuevas clases basadas en las ya existentes
#UNA BUENA FORMA DE VERLO ES COMO UN PADRE QUE TIENE VARIOS HIJOS Y CADA HIJO HEREDA DIFERENTES PROPIEDADES O FUNCIONES POR OTRO LADO

#Polimorfismo
#Es la capacidad de un objeto para tomar muchas formas /permite acotar codigo y evitar errores
# y en POO es la capacidad que tienen las clases para ser tratadas como instancias de una clase padre, sin saber que es se comporta de manera distinta

"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
"""
#SUPERCLASE
class Animal:
    def __init__(self, name:str): #le coloque un parametro de nombre de animal
        self.name = name          #el nombre vendria a ser un atributo comun
    
    def sound (self): #creo una función pq quiero saber el sonido
        pass

#Hemos hecho poliformico el animal diciendo que si es perro dice guau y si es gato dice miau

#SUBCLASE
class Dog(Animal):  #para aplicar herencia ponemos la superclase en () luego de la subclase

    def sound (self): 
        print ("Guau!")
 
class Cat(Animal):

     def sound (self):  #Esto es poliformismo en tiempo de compilacion que es esa sobrecarga de funciones
        print ("Miau!")
  

def print_sound(animal: Animal):  #Esto recibe un animal / polimorfismo 
    animal.sound()    


my_animal = Animal("Animal")
print_sound(my_animal)

my_dog = Dog ("Perro")
print_sound(my_dog)

my_cat = Cat("Gato")
print_sound(my_cat)


"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""

#SUPERCLASE
class Employee:

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name    #ahora son propiedades de clase
        self.employees = []  #no solo sirve para guardar propiedades sino tambien para definir una nueva


    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)



#SUBCLASE
class Manager(Employee):  
    def coordinate_projects(self):  #operaciones propias
        print(f"{self.name} es coordinando todos los proyectos de la empresa")

        


class ProjectManager(Employee):
    def __init__(self, id: int, name: str, project:str): #estamos reutilizando el inicializado de la super clase y aparte le estamos añadiendo una propiedad propia de los project manager
        super().__init__(id,name)
        self.project= project

    def coordinate_project(self):  #operaciones propias
        print(f"{self.name} esta coordinando su proyecto")


class Programmer(Employee):
    def __init__(self, id: int, name: str, languaje:str):  #estamos reutilizando el inicializado de la super clase y aparte le estamos añadiendo una propiedad propia de los programadores
        super().__init__(id,name)
        self.languaje= languaje

    def code(self):
        print(f"{self.name} está programando en {self.languaje}")

    def add(self, employee:Employee):
        print(f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá")
        #pass tambien puede servir


#basandonos en una superclase empezamos modificar su comportamiento segun la clase especializada que vamos a crear , basandonos en herencia y polimorfismo

my_manager = Manager(1,"Franco")                     #creando diferentes empleados
my_project_manager = ProjectManager(2,"Emerson", "Proyecto 1")
my_project_manager2 = ProjectManager(3,"Max", "Proyecto 2")
my_programmer = Programmer(4,"Kontrol", "Swift")
my_programmer2 = Programmer(5,"Ross", "Cobol")
my_programmer3= Programmer(6,"Bushi", "Dart")
my_programmer4= Programmer(7,"Nasos", "Python")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer2)

my_programmer.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()

print ("Empleado de my_manager")
my_manager.print_employees()

print ("Empleado de my_project_manager")
my_project_manager.print_employees()

print ("Empleado de my_programmer")
my_programmer.print_employees()