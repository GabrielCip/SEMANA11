def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def principal():
    numero = int(input("Ingrese la posicion de Fibonacci que desea calcular:\t"))
    resultado = fibonacci(numero)
    print(f"El numero de Fibonacci en la posicion {numero} es {resultado} ")

principal()