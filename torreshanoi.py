def torres_hanoi(n, x, y, z):
    if n == 1:
        print(f"Mueve el disco 1 de {x} a {y}")
    else:
        torres_hanoi(n - 1, x, z, y)
        print(f"Mueve el disco {n} de {x} a {y}")
        torres_hanoi(n - 1, z, y, x)

def principal():
    discos = int(input("Ingrese la cantidad de discos:\t"))
    print("Los pasos para resolverlo son:")
    torres_hanoi(discos, "Poste A", "Poste C", "Poste B")

principal()