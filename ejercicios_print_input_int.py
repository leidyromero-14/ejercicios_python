# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:48:49 2021

@author: LENOVO
"""
##los mensajes deben ir en doble comilla ""
##la instruccion para mostrar datos es print
print ("Hola")
print ('mundo')
print ("Hola mundo")
print ("Hola", "mundo")
print ("Hola", end=" ")
print ("mundo") ## el resultado hola mundo
print ("Hola","jóvenes","cómo","amanecen")
print ("Hola jóvenes cómo amanecen")
print ("Hola","jóvenes" , "cómo","amanecen"
, sep=",")
print ("Hola","jóvenes"
,
"\ncómo"
,"amanecen", sep=", ")
a = 7 + 5
print(a)
print(7 + 5)
print(f"7 + 5 {a}") 


## la instruccion para entrar datos (leer) es input
nombre = input("Teclee su nombre ")
apellido = input( "Teclee su apellido")
apellido2 = input(f"ahora {nombre} {apellido} teclee su segundo apellido ")
print("Nombre ", nombre, end=" ")
print(apellido)
edad = int(input(f"Muy bien {nombre} {apellido} {apellido2} ahora teclee su edad"))
qq = edad + 2
print(qq)
a = input( "Entre número entero")
b = input("Entre otro número entero ")
print(a+b)

a = int(input("Entre número entero"))
b = int(input("Entre otro número entero"))
print(a+b)