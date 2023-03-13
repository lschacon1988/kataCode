'''Dada una matriz de enteros y un entero positivo k, determinar el número de (i,j) pares donde (i < j) y arr[i] + arr[j] es divisible por k.

Ejemplo
arr = [1,2,3,4,5,6]
k = 5


Tres pares cumplen los criterios: [1,4], [2,3], y [4,6].'''

def divisible_sum_pairs(n,k,ar):
    contador = 0
    rango = range(1,n)
    for i in rango:
        for j in range(i,n):
            temp = ar[i-1] + ar[j]
                        
            if(temp % k == 0):
                contador += 1
                
    return contador

ar = [1 ,3 ,2 ,6 ,1 ,2]
n=6
k=3

print('suma', divisible_sum_pairs(n=n,k=k,ar=ar))