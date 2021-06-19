#Elabore un programa en Python que lea una longitud en metros y 
    # la convierta y escriba en centímetros, pies y pulgadas.

"""// 1 metro a a cm = 100
// 1 metro a pies = 3.28
// 1 metro a pulgadas: 39.37"""

opcion =  int(input(" MENU \n1. Metros convertidos a centímetros \n2. Metros convertidos a pies \n3. Metros convertidos a pulgadas \n "
"ingrese la opción que desea:") )
if opcion == 1: 
   metros=int(input("ingrese los metros"))
   centimetros = metros *100
   print (metros,"metros equivalen a", centimetros, "centimetros" )
elif opcion == 2:
   metros=int(input("ingrese los metros"))
   pies = metros *3.28
   print (metros,"metros equivalen a", pies, "pies")
elif opcion == 3:
   metros=int(input("ingrese los metros"))
   pulgadas = metros *39.37
   print (metros,"metros equivalen a", pulgadas, "pulgadas")