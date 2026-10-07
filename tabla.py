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
print("Cantidad de variables:", cantidad_variables)
print("Cantidad de combinaciones:", combinaciones)

valores = [True, False]

print("\nP\tQ\tR\tResultado")

for p in valores:
    for q in valores:
        for r in valores:

            resultado = eval(
                expresion,
                {},
                {
                    "P": p,
                    "Q": q,
                    "R": r
                }
            )

            if p:
                valor_p = "V"
            else:
                valor_p = "F"

            if q:
                valor_q = "V"
            else:
                valor_q = "F"

            if r:
                valor_r = "V"
            else:
                valor_r = "F"

            if resultado:
                valor_resultado = "V"
            else:
                valor_resultado = "F"

            print(
                valor_p,
                "\t",
                valor_q,
                "\t",
                valor_r,
                "\t",
                valor_resultado
            )