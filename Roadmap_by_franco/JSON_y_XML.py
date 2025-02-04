# Reto 12 JSON Y XML

"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 """

#JSON Y XML son formatos de ficheros que nos sirven para guardar información de manera estructurada
import os                                           #Importamos la librería para trabajar con el sistema operativo
import xml.etree.ElementTree as xml                 #Importamos la librería para trabajar con XML
import json                                         #Importamos la librería para trabajar con JSON


data= {                                                   #creamos un diccionario para almacenar los datos 
    "name" : "Franco",
    "age" : 20,
    "birth_date" : "18/11/2000",
    "programming_languajes" : ["Python", "Java", "C++"]
}
xml_file= "franco.xml"                                    # Nombre del fichero XML
json_file= "franco.json"                                   # Nombre del fichero JSON

#XML

def create_xml():                                         # Función para crear archivos xml

    root = xml.Element("data")                            # Se crea un elemento tipo xml de nombre datos

    for key, value in data.items():                       # Se recorre los datos del diccionario creado data
        child = xml.SubElement(root, key)                 # Le asignamos a una variable un sub elemento  del elemento datos antes creado y le pasamos la llave del dicc
        if isinstance(value, list):                       # Preguntamos si el tipo de valor es una lista
            for item in value:                            # Si es una lista, la recorremos
                xml.SubElement(child, "item").text = item # y escribimos por cada subelemento el valor
        else:                                             # Si no es una lista
            child.text = str(value)                       # se escribe directamente el valor

    tree = xml.ElementTree(root)                          # Se crea un árbol de los elementos antes creados
    tree.write(xml_file)


create_xml()

with open(xml_file, "r") as xml_data:                        # Mostramos el contenido del archivo XML
    print(xml_data.read())
#os.remove(xml_file)                                          # Borramos el archivo XML



#JSON


def create_json():                                           # Función para guardar datos en un archivo JSON
    with open (json_file, "w") as json_data:                     # Creamos el archivo JSON
       json.dump(data, json_data)                     # Guardamos los datos en el archivo JSON
     #dump es la posibilidad de pasarle un objeto y que lo convierta en formato JSON(en esta caso el diccionario data)
create_json()


with open(json_file, "r") as json_data:                        # Ahora queremos leer en consola el archivo JSON
       print(json_data.read())

#os.remove(json_file)                                         # Borramos el archivo JSON


"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
"""
create_xml()
create_json()

class Data:                                                    # Creamos una clase llamada Data
    def __init__(self, name, age, birth_date, programming_languajes):  # Definimos el constructor de la clase con sus atributos/propiedades/parametros
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languajes = programming_languajes


with open(xml_file, "r") as xml_data:                      
    
    root= xml.fromstring(xml_data.read())              # Convertimos el archivo XML en un objeto de tipo XML             
    name= root.find("name").text                #recuperamos los datos ya q podemos acceder a ellos pq ahora es un objeto de tipo XML
    age= root.find("age").text
    birth_date= root.find("birth_date").text

    programming_languajes= []               #creamos una lista vacía para almacenar los lenguajes de programación
    for item in root.find("programming_languajes"): #recorremos la lista de lenguajes de programación
        programming_languajes.append(item.text)    #agregamos cada lenguaje a la lista


    xml_class=Data(name, age, birth_date, programming_languajes) #creamos un objeto de la clase Data con los datos recuperados del archivo XML 
    print(xml_class.__dict__) #mostramos los datos del objeto creado como un diccionario




    with open(json_file, "r") as json_data:  
        json_dict =json.load(json_data) #leemos el archivo JSON y el read lo convierte en un diccionario
        #name= json_dict ["name"]  #recuperamos los datos del diccionario
        #age= json_dict ["age"]
        #birth_date= json_dict ["birth_date"]
        #programming_languajes= json_dict ["programming_languajes"]
        json_class= Data(
            json_dict ["name"], 
            json_dict ["age"], 
            json_dict ["birth_date"], 
            json_dict ["programming_languajes"]) #creamos un objeto de la clase Data con los datos recuperados del archivo JSON
        print(json_class.__dict__)

os.remove(xml_file) #borramos el archivo XML
os.remove(json_file) #borramos el archivo JSON