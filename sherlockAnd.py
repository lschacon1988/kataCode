'''A Watson le gusta desafiar la capacidad matemática de
Sherlock. Proporcionará un valor inicial y final que describe
un rango de números enteros, incluidos los puntos finales. 
Sherlock debe determinar el número de enteros cuadrados dentro
de ese rango.

Nota : Un número entero cuadrado es un número entero
que es el cuadrado de un número entero, por ejemplo.'''

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#
import math


def squares(a, b):
    # Write your code here
    rango = range(a,b+1)
    enteros_cuadrados = [entero for entero in rango if math.isqrt(entero) ** 2 == entero]    
    
    return len(enteros_cuadrados)    

a= 17
b= 24


print(squares(a=a,b=b))


def squares2(a, b):
    # Write your code here
    '''se usan dos while para recorrer
    cada entero dentrro de un rango "a" inicia el
    rango y "b" lo finaliza'''
    count = 0
    i = 1
    while i * i < a:
        i += 1
    while i * i <= b:
        count += 1
        i += 1
    return count

a= 50
b= 100000000


print(squares2(a=a,b=b))