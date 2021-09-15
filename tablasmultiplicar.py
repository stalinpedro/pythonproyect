print("¿Qué tabla quieres calcular?")
numero = int(input())

for numero2 in range(1,11):
    print("{} * {} = {}".format(numero, numero2, numero*numero2))