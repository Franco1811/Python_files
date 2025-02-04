### Clases ###
"Nos sirve para que todo pueda responder ante cierta lógica"
 
class MyEmptyPerson: 
    pass      


print(MyEmptyPerson)      #las clases pueden tener constructores para q reciba parametros y haga algo #
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias= "sin alias"):                               #nos sirve para crear un constructor de clase
        self.full_name = f"{name} {surname} ({alias})"                         #ahora tengo la capacidad de que "Person" reciba parametros
                                                                     #Al darle un valor por defecto no me da error ejemplo ="sin alias"
    def walk(self):                                                  #si yo pongo self puedo acceder a todo lo gaurdado dentro de self
        print (f"{self.full_name} Esta caminando")

my_person = Person("franco","gonzalez")
print(my_person.full_name)
my_person.walk()


my_other_person = Person("Franco", "Poma", "Chato")    #Puedo agregar caracteres 
my_other_person.walk()


my_other_person.full_name = "Max Feo (El que no se baña)"   #Una vez ya tengo el constructor creado , puedo hacer lo q quiera
print(my_other_person.full_name)



my_other_person.full_name = 666  #EL tipado es debil asi que lo podemos variar
print(my_other_person.full_name)