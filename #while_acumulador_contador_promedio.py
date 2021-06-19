#elabore un programa para determinar el nuevo salario de una persona,
#contando a cuantas se les hizo el calculo, cuantas tuvieron un aumento mayor que cero 
#el total de salarios anteriores, el total de aumentos, el total de nuevos salarios, 
# el promedio salarial antes y despues del aumento y el promedio de aumentos. 
#
tsa = 0. #El total de salarios actuales (tsa) se actualiza tan pronto es leído un salario actual
tau = 0. #total de aumentos (tau) se actualiza cada vez que se calcula un nuevo aumento
tns = 0. #total de nuevos salarios (tns) se actualiza cada vez que se determina el nuevo salario de un empleado
contador = 0 # variable contador, valor inicial de 0, y cada vez que se lean los datos de un empleado la incrementamos en 1
nombre = input("entre nombre ")
while nombre != "":
    salario = int(input(f"{nombre} entre salario "))
    tsa = tsa + salario
    contador = contador + 1
    aumento = 0.
    if salario < 1000:
        aumento = salario * 0.1
        tau = tau + aumento
    nuevoSalario = salario + aumento
    tns = tns + nuevoSalario
    print("Nombre", nombre, "salario", salario, "Aumento", aumento, "Nuevo salario",nuevoSalario)
    nombre = input("entre nombre ") #ya no pertenece al conjunto de instrucciones que se ejecutan en while
psa = tsa / contador
pau = tau / contador
pns = tns / contador
print("Total empleados", contador, )
print("Total salarios anteriores", tsa, "Promedio", psa)
print("Total aumentos ", tau, "Promedio", pau)
print("Total nuevos salarios ", tns, "Promedio", pns)