
####temas de herencia, getters, setters, definir classes

#h sabor y color
#si a aca estamos
# instanciar una clase de galleta son atributo

#programacion orientada a objetos permite reutilizar codigo
class Galleta:                              #una clase es como tener una plantilla 
        def __init__(self, sabor, color):   #inicializamos los atributos de la clase. Este es el constructor
                self.sabor = sabor          #inicializa atributo sabor. ESte es el atributo xxx...
                self.color = color          #quemar es pasarle algo definido, sin ingresar valor
        
sabor = input("ingrese sabor: ")
color = input("ingrese color: ")
galleta = Galleta(sabor, color)
                                    #llamamos la clase, no se le debe pasar valores. A la variable le pasamos el objeto


print(galleta.sabor)    #aca se muestra el atributo, osea el tipo de sabor 
print(galleta.color)
print(f"el sabor de la galleta es : {sabor} y el color es : {color}")


if galleta.sabor == "chocolate":
        print("el sabor de la galleta es chocolate")

else:
        print("el sabor de la galleta no es chocolate")


### ejercicio para clasificar utilizando herencia  
# clasificando animales

class Terrestre:
    def caminar(self):      #metodo constructor 
        print("el animal camina")
    
    def carnivoro(self):
        print("el animal es carnivoro")


class Acuatico:        #nuevos atributos
    def nadar(self):
        print("el animal nada")


class Pinguino(Terrestre, Acuatico):
    pass

class Perro(Terrestre):
    pass


perro = Perro()
perro.caminar()
pinguino = Pinguino()
pinguino.caminar()
pinguino.nadar()

### ejercicio para getters y setters
##getters---accede a un objetivo
##setters--- fijar el valor de un objetivo
#

class Persona:
    def __init__(self):
        self._edad = 0
    # Metodo Getter
    def get_edad(self):
        return self._edad
    
    # Metodo setter
    def set_edad(self, e):
        self._edad = e

edad_maria = int(input("ingrese edad"))
maria = Persona()
maria.set_edad(edad_maria)

print(maria.get_edad())

####clase del 5 de junio 
###tema listas 
##encontrar numeros pares
numeros = []
lista = []

for i in range(0,100):
    numeros.append(i)
    if i%2 != 0:
        lista.append(i)
print(lista)

###ejercicio
##dado un araid o arreglo  A = [20, 14, 12, 11, 8,4,1], encontrar el valor mas bajo 
##imprima el valor bajo 

A = [20, 14, 12, 11, 8,4,1]
maximo = 20 #para comparar desde el valor mas alto #variable que identifique el valor maximo
minimo = maximo # encontar variable minimo
for elemento in A:   ##
    if elemento < minimo:  #comienza con la condicion if#hacer una comparacion al valor minimo
       minimo = elemento  ## se le asigna el valor a minimo
    print (minimo)

###ejercicio
##almacene las asignaturas de un curso 
asignatura = ["matematicas", "ciencias", "quimica", "deportes"]
asignatura_elegida = (input("ingrese asignatura seleccionada: "))
for elemento in asignatura:
    if asignatura_elegida == elemento: #if es para comparar los elementos
        print("la asignatura elegida {asignatura_elegida} existe en la lista original: ")

###ejercicio
##dos arays del mismo tamaño.
#que los almacene los nombre e las personas
#y almacene la longitud o tamaño

a = int(input("tamaño: "))
personas = []       #arrays 1
tamanio_nombre = [] #arrays 2
for elemento in range(a):
    nombre_persona = input("ingrese su nombre: ")
    personas.append(nombre_persona)
    tamanio_nombre.append(len(personas[elemento]))
print(personas, tamanio_nombre)

###ejercicio
##hacer una funcion dado un numero lo multiplico por dos

def multiply(number):
    multiply_number = number * 2
    return multiply_number

print(multiply(2))


##tarea: Escribir una función que me sume los numeros que esten en una lista.
#ejemplo: [2,3,1]
#resultado = 6

