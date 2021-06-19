"""
#h sabor y color
#si a aca estamos
# instanciar una clase de galleta son atributo
"""
"""
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
"""
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




