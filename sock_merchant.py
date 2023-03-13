'''Hay una gran pila de calcetines que deben
emparejarse por color. Dada una serie de números
enteros que representan el color de cada calcetín,
determine cuántos pares de calcetines con colores iguales hay.'''
#Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sock_merchant(n: int, ar: list):
    # Write your code here
    pares_color = {key: ar.count(key) for key in ar}
    count = 0
    for value in pares_color.values():
        count += value // 2  
    
    return count

n = 9
ar = [10 ,20 ,20 ,10 ,10 ,30 ,50 ,10 ,20]
print(sock_merchant(n=n, ar=ar))  

print(5 // 2)