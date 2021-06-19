#Elaborar un algoritmo que lea el nombre de una persona y su estado civil. 
#El estado civil está codificado con un dígito con los siguientes significados:

#1: Soltero
#2: Casado
#3: Separado
#4: Viudo
#5: Unión libre
#El algoritmo debe imprimir el nombre leído y la descripción correspondiente al estado civil leído.

nombre = input("Entre nombre: ")
estadoCivil = int(input(f"{nombre} teclee su estado civil: "))
if estadoCivil == 1:
     print(nombre, "Soltero")
if estadoCivil == 2:
     print(nombre, "Casado")
if estadoCivil == 3:
     print(nombre, "Separado")
if estadoCivil == 4:
     print(nombre, "Viudo")
if estadoCivil == 5:
     print(nombre, "Unión libre")
if estadoCivil != 1 and estadoCivil != 2 and estadoCivil != 3 and estadoCivil != 4 and estadoCivil != 5:
     print("Estado civil inválido")