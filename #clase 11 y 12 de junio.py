#clase 11 y 12 de junio
"""
ejercicio 1
import random
class vector:
    __nombre="Fredy"
    def __init__(self,n):
        self.n=n
        self.V=[0]*(n+1)
    
    def __str__(self):
        return "El vector es: "+str(self.V)
    
    
    def construyeVector(self,m,r):
        self.V[0]=m
        for i in range(1,m+1):
            self.V[i]=random.randint(1,r)
    
    def getNombre(self):
        print(self.__nombre)
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre
    
v=vector(4)
print(v.V)

v.getNombre()
v.setNombre("Jhon")
v.getNombre()
_______________________________________________
"""
"""
#ejercicio de matriz 
#suma de matrices
def crear_matriz_2(cantidad_filas, cantidad_columnas):
    return [[0 for _c in range(cantidad_columnas)] for _f in range(cantidad_filas)]

def sumamatrix(mat1,mat2):                                      #función suma
    cantidad_filas = len(mat1)                                  #define longitud de fila
    cantidad_columnas = len(mat2[0])                            #define longitud columna
    matriz_resultante = crear_matriz_2(cantidad_filas,cantidad_columnas) #matriz resultado de la suma
    for i in range(cantidad_filas):                             #recorrer filas
        for j in range(cantidad_columnas):                      #recorrer columnas
            matriz_resultante[i][j] = mat1[i][j] + mat2[i][j]   #suma de matrices
    #for _ in matriz_resultante:
    print(matriz_resultante)

# 3x3 matrix
matriz_a = [[4,12,7,3],
    [4,6,5,6],
    [7,6,8,9]]

# 3x4 matrix
matriz_b = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

sumamatrix(matriz_a,matriz_b)
"""
"""
##ejercicio
##otra forma de sumar matrices

import random

def crear_matriz_2(cantidad_filas, cantidad_columnas):
    m = [[0 for _c in range(cantidad_columnas)] for _f in range(cantidad_filas)]
    for i in range(cantidad_filas):
        for j in range(cantidad_columnas):
            m[i][j] = random.randint(1,9)
    return m

def sumamatriz(fil,col):
    matriz_a = crear_matriz_2(fil,col)
    matriz_b = crear_matriz_2(fil,col)
    for i in range(fil):
        print("\n")
        for j in range(col):
            print(matriz_a[i][j], end="   ")
    print("\n")
    print("\n")
    for i in range(fil):
        print("\n")
        for j in range(col):
            print(matriz_b[i][j], end="   ")
    print("\n")
    print("\n")
    matriz_res = crear_matriz_2(fil,col)
    for i in range(fil):
        for j in range(col):
            matriz_res[i][j] = matriz_a[i][j] + matriz_b[i][j]
    return matriz_res

f = int(input("Ingrese cantidad de filas: "))
c = int(input("Ingrese cantidad de columnas: "))
matriz = sumamatriz(f,c)

for i in range(f):
    print("\n")
    for j in range(c):
        print(matriz[i][j], end="   ")
"""

#ejercicio 
#leer una matriz de determoinado tamaño y haga la transpuesta.

def transpuesta(matriz):#Funcion para hacer la transpuesta de una matriz
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]#Se compacta la lectura y se hace la transpuesta de la matriz en una sola línea
mat_1= [[1,2,3],[4,5,6]]#matriz original

print("Esta es la matriz original",mat_1)#imprime la matriz orgiinal
matriz_resultado=transpuesta(mat_1)#Llama la función transpuesta
print("Esta es la transpuesta",matriz_resultado)#imprime la matriz transpuesta
