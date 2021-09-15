print("Sabores:")
print("Vainilla\nChocolate\nFresa\nChicle")
print("¿De que sabor quieres tu Helado?: ")
sabor = input()




if sabor == "Vainilla":
	precio = 19
elif sabor == "Chocolate":
	precio = 25
elif sabor == "Fresa":
	precio = 22
elif sabor  == "Chicle":
	precio = 28
else:
    print("producto no disponible")
    precio = 0

print("El precio es ${}".format(precio))