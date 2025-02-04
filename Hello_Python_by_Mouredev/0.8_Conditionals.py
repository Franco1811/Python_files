### Conditionals ###

my_condition = False

if my_condition: #es lo mismo que if my condition==true:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")
    
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25 :  #una segunda condicional dentro de otra
    print("Es igual a 25")
else: #con el else aseguramos que se ejecutara una de las lineas
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continua")

"== true es redundante ya que esta implicito en el if ya que te tiene q cumplir la condicion"
"Si la condicion es falsa no se imprime la primera parte"



my_string = ""

if not my_string: #nos niega la condicion lo que para nosotros antes no se cumplia , ahora si
    print("Mi cadena de texto es vacia")

if my_string == "Mi cadena de textoooo":
    print("Mi cadenas de texto coinciden")
    



 