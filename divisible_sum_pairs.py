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