### Functions ###

#funcion simple
def my_function ():
    print("Esto es una función") #nos sirve para llamarla y que ejecute codigo
                                 #tambien puede devolver y recibir codigo

my_function()
my_function()
my_function()

#funcion que recibe parametros
def sum_two_values (first_number,second_number):    #dentro del parentesis puedo poner parametros
    print(first_number+second_number)               #nos sirven para hacer operaciones mas complejas

sum_two_values(5,7)
sum_two_values(557,755)
sum_two_values(1.4,5.2)

#funcion con return
def sum_two_values_with_return (first_number,second_number):    
   my_sum = first_number + second_number
   return my_sum

my_result = sum_two_values_with_return(10,5)
print(my_result)



def print_name(name,surname):
    print(f"{name} {surname}")   #la f nos permite acceder a los valores

print_name(surname="Gonzalez", name="Franco")  #Se ha reordenado el orden q nos intentaba imponer el print



def print_name_with_default(name,surname,alias="Sin alias"):  #Le di un valor por defecto al alias
    print(f"{name} {surname} {alias}") 

print_name_with_default("Franco","Gonzalez","Chato")
print_name_with_default("Franco","Gonzalez")



def print_upper_texts(*texts):   #el asterisco me da la posibilidad de pasar muchos parametros
    print(type(texts))
    for text in texts:           #el for me ayuda a mofificar los parametros segun lo que necesito
        print(text.upper())
    

print_upper_texts("Hola","Python","Chato")
print_upper_texts("Hola")   



