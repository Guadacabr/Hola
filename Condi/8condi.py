bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input ("Ingrese tu puntuación: "))

if puntos == inaceptable:
    nivel = "Inaceptable"

elif puntos == aceptable:
    nivel = "Aceptable"

elif puntos >= 0.6:
    nivel = "Meritorio"

else:
    nivel = ""

if nivel == "":
    print("Esta puntuación NO es válida")

else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))
    
