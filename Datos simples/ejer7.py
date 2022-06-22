peso = input ("¿Cuál es tu peso (kg)? ")
estatura = input ("¿Cuál es tu estaura (metros)? ")
imc = round (float(peso) / float(estatura) **2,2)
print ("Tu indice de masa corporal es " + str(imc))
