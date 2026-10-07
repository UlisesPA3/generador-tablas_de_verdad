expresion = input("Ingresa una expresión lógica: ")

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