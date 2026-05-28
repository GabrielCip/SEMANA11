#Dados dos numeros enteros hallar la suma, resta, multiplicacion y división
import operaciones.operacionesbasicas as oper
from operaciones.operacionesbasicas import restar
from operaciones.operacionesbasicas import dividir
#ENTRADA
nro1 = int(input("Ingrese el numero 1:\t"))
nro2 = int(input("Ingrese numero2:\t"))

#PROCESO
suma = oper.sumar(nro1, nro2)
diferencia = restar(nro1, nro2)
#Hallara la multiplicacion con import
producto = oper.multiplicar(nro1,nro2)
#Hallar la division con from
division = dividir(nro1,nro2)
#Implementar residuo en operaciones basicas y hallar el residuo
residuo = oper.residuo(nro1,nro2)
#SALIDA
print(f"{nro1} + {nro2} = {suma}")
print(f"{nro1} - {nro2} = {diferencia}")
print(f"{nro1} x {nro2} = {producto}")
print(f"{nro1} / {nro2} = {division}")
print(f"El residuo de {nro1} entre {nro2} = {residuo}")