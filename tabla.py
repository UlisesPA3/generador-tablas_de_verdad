from itertools import product

expresion = input("Ingresa una expresión lógica: ")

variables = []

if "P" in expresion:
    variables.append("P")

if "Q" in expresion:
    variables.append("Q")

if "R" in expresion:
    variables.append("R")

cantidad_variables = len(variables)
combinaciones = 2 ** cantidad_variables

print("\nVariables detectadas:", variables)
print("Cantidad de combinaciones:", combinaciones)

filas = list(product([True, False], repeat=cantidad_variables))

print("\nCombinaciones generadas:")

for fila in filas:
     print(fila)
          