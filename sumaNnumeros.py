# Hallar la suma de N números
# N = 5  suma = 5+4+3+2+1 = 15
#Hallarlo recursivamente
def sumarecursiva(N):
    #CASO BASE
    if N == 1:
        return 1
    #Caso recursivo
    else:
        return N + sumarecursiva(N-1)

def principal():
    numero = int(input("Ingrese un numero:\t"))

    suma = sumarecursiva(numero)
    print(f"La suma recursiva de {numero} es {suma}")

principal()