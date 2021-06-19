#clase 29 de mayo
"""
# Elaborar un programa para calcular y mostrar el factorial de un entero
# entrado por teclado.

numero = int(input("ingrese numero: "))
fact = 1
for i in range(1,numero+1):
    fact = fact * i
    print("el factorial es: ", numero, fact)
"""
##
"""
menu = int(input("ingrese opcion del menu: "))
a = int(input("ingrese numero a operar: "))
b = int(input("ingrese numero a operar: "))
if menu == 1:
    suma = a+b
    print(suma)
elif menu == 2:
    if b > a:
        resta = b - a
    else:
        resta = a - b
    print(resta)
elif menu == 3:
    if a > b:
        division = b / a
    else:
        division = a / b
    print(division)
elif menu == 4:
    multiplicacion = a * b
    print(multiplicacion)
else:
    print("no ingreso numero valido")
"""
##
"""
#calcular edad
edad = 18
sexo = "masculino"
if edad >= 18:
    if sexo == "masculino":
        print("hombre  mayor de edad")
    else:
        print("mujer mayor de edad")
else:
        print("no soy mayor de edad")
"""
###
"""
a = 1024
s = str(a)
for i in s:
    print(i)
"""
##
"""
###calcular salario de empleados
total_lista_empleados = 10
empleados = 1
salario_base = 908311
while empleados <= total_lista_empleados:
    comision = salario_base*0.05
    salario = salario_base + comision
    print("nuevo salario", salario, empleados)
    empleados +=1

##

##imprimir los numeros del 1 al 10
x = range (6)
for i in range(10):  #el i itera el rango, el for cuenta pociciones y no 
    print (i +0)

# otra forma 
x = range (3,6)

for i in x:  
    print (i)
 """
 """

 #calcular numeros si es primo o no
 #condiciones para unnumero primo: 
 ##que se divida por si mismo y que se divide por 1
 #4/4 = 0 #divisible por si mismo
 #4/1 = 0 #divisible por  1
 #4/2 = 0
 #si el numero es divisible por otro numero no primo
num = int(input("ingrese el numero: "))
if num < 2:  #
    return False
for i in range(2, num): 
    if num % i == 0:
    return true
        print("no es primo")
    """
    

