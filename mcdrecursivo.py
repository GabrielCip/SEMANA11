def mcd(a, b):
    # CASO BASE: Si el segundo número es 0, el MCD es el primer número
    if b == 0:
        return a
    # PASO RECURSIVO: Pasamos el segundo número y el residuo (a % b)
    else:
        return mcd(b, a % b)


def principal():
    print("--- Calculadora de Máximo Común Divisor (MCD) ---")
    
    # Pedimos los datos al usuario y los convertimos a números enteros (int)
    numero1 = int(input("Ingresa el primer número:\t"))
    numero2 = int(input("Ingresa el segundo número:\t"))
    
    # Calculamos el resultado usando nuestra función recursiva
    resultado = mcd(numero1, numero2)
    
    # Mostramos el resultado
    print(f"\nEl MCD de {numero1} y {numero2} es: {resultado}")


    principal()