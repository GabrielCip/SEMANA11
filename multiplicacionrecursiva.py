def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

def principal():
    numero1 = int(input("Ingrese el primer numero:\t"))
    numero2 = int(input("Ingrese el segundo numero:\t"))
    resultado = mcd(numero1, numero2)
    print(f"El MCD de los dos numeros es {resultado} ")

principal()