#Hallar la potencia de un nro a un exponente de forma recursiva
#nro 3 exponente 4 -----> 3*3*3*3 = potencia = 81
def potenciarecursiva(x, y):
    #CASO BASE
    if y == 0:
        return 1
    #Caso recursivo
    elif y == 1:
        return x
    else:
        return x * potenciarecursiva(x, y-1)
    
def principal():
    numero = int(input("Ingrese un numero:\t"))
    exponente = int(input("Ingrese el numero de potencia:\t"))

    potenciacion = potenciarecursiva(numero, exponente)
    print(f"La potencia de {numero} elevado a {exponente} es {potenciacion}")

principal()