import operaciones.operacionesrecursivas as opercur
import operaciones.operacionesbasicas as operbas

def calcular():
    while True:
        nro1 = int(input("Ingrese el primer numero:\t"))
        if nro1 < 0:
            print("Error, no se puede ingresar negativo")
        else:
            break

    while True:
        nro2 = int(input("Ingrese el segundo numero:\t"))
        if nro2 < 0:
            print("Error, no se puede ingresar negativo")
        else:
            break

    while True:
        nro3 = int(input("Ingrese el tercer numero:\t"))
        if nro3 < 0:
            print("Error, no se puede ingresar negativo")
        else:
            break

    #Ecuacion parte arriba
    #primero
    factorial = opercur.factorial(nro1)
    #Segudno
    producto = operbas.multiplicar(nro2, nro3)
    #Tercero
    restaTo = operbas.restar(factorial, producto)
    #Cuarto
    if nro3 != 0:
        ecuacion = operbas.restar(restaTo, nro3)
    else:
        ("No se puede dividir entre tres")
    print(f"El resultado de la ecuación {nro1}! - ({nro2} * {nro3}) entre {nro1} es {ecuacion}")

calcular()