#Hallar el factorial de un numero de forma recursiva
# Funcion recursiva de factorial
def factorialrecursiva(N):
    #CASO BASE
    if N == 1:
        return 1
    #Caso recursivo
    else:
        return N * factorialrecursiva(N-1)

def principal():
    numero = int(input("Ingrese un numero:\t"))

    factorial = factorialrecursiva(numero)
    print(f"El factorial de {numero} es {factorial}")

principal()