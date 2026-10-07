from itertools import product

expresion = input("Ingrese una expresión lógico: ")

variables = []

if "P" in expresion:
    variables.append("P")
    
if "Q" in expresion:
    variables.append("Q")
    
if "R" in expresion:
    variables.append("R")
    
cantidad_variables = len(variables)
combinaciones = 2** cantidad_variables

print("\nVariables detectadas: ", variables)
print("Cantidad de combinacions:", combinaciones)

filas = list(product([True, False], repeat=cantidad_variables))

#Encabezado
print("\nTabla de verdad:\n")

for variable in variables:
    print(variable, end="\t")
print("Resultado")

#Generacion de tabla
for fila in filas:
    
    valores_actuales = {}
    
    posicion = 0
    
    for variable in variables:
        valores_actuales[variable] = fila[posicion]
        posicion = posicion + 1
        
    resultado = eval (expresion, {}, valores_actuales)
    
    #Mostrar valores de las variables
    for valor in fila:
        
        if valor:
            print("V", end="\t")
        else:
            print("F", end="\t")
            
    #Mostrar el resultado
    if resultado:
        print("V")
    else:
        print("F")


