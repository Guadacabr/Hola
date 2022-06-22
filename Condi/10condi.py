print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input ("Ingresa el número correspondiente al tipo de pizza que quieres: ")

if tipo == "1":
    print("Ingredientes de pizza vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input ("Ingresa el ingrediente que deseas: ")
    pint("Pizza vegetariana con mozzarella, tomate y ", end="")

    if ingrediente == "1":
        print("pimiento")

    else:
        print("Tofu")

else:
    print("Ingredientes de pizza no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input ("Ingresa el ingrediente que deseas: ")
    print("Pizza no vegetariana con mozarrella, tomate y ", end="")
    if ingrediente =="1":
        print("peperoni")

    elif ingrediente == "2":
        print("Jamón")

    else:
        print("Salmón")
