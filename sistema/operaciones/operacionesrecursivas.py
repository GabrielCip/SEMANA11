def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
def multiplicacion(x,y):
    if x == 0 or y == 0:
        return 0
    else:
        if x == 1:
            return y
        else:
            return x + multiplicacion(x, y-1)
        

def potenciarecursiva(x, y):
    #CASO BASE
    if y == 0:
        return 1
    #Caso recursivo
    elif y == 1:
        return x
    else:
        return x * potenciarecursiva(x, y-1)
    