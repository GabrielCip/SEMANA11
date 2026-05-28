# Dado un numero N hallar la suma de sus numeros impares
# Ejemplo:
# Si N = 7 suma = 7+5+3+1 = 16
# Si N = 8 suma = 7+5+3+1 = 16
def imparesrecursivo(x):
    if x == 0:
        return(0)
    elif x == 1:
        return 1
    else:
        if x % 2 != 0:
            return x + imparesrecursivo(x-2)
        else:
            return imparesrecursivo(x-1)

def principal():
    nro = int(input("Ingrese un numero:\t"))
    if nro%2==0:
        nro = nro - 1
    sumaImpar = imparesrecursivo(nro)
    print(f"La suma de los numeros impares es {sumaImpar}")

principal()