valores = [True, False]

print("P\tQ\tNOT P\tNOT Q\tP and Q\tP or Q")

for p in valores:
    for q in valores:
        
        resultado_not_p = not p
        resultado_not_q = not q
        resultado_and = p and q
        resultado_or = p or q
        
        if p: 
            valor_p = "V"
        else:
            valor_p = "F"

        if q:
            valor_q = "V"
        else:
            valor_q = "F"
        
        if resultado_not_p:
            valor_not_p = "V"
        else:
            valor_not_p = "F"
            
        if resultado_not_q:
            valor_not_q = "V"
        else:
            valor_not_q = "F"
            
        if resultado_and: 
            valor_and = "V"
        else:
            valor_and = "F"
            
        if resultado_or: 
            valor_or = "V"
        else:
            valor_or = "F"
                    
        print(valor_p, "\t", valor_q, "\t", valor_not_p, "\t", valor_not_q, "\t", valor_and, "\t", valor_or)
        
