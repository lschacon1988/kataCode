'''Dada una serie de avistamientos de aves donde cada elemento
representa una identificación de tipo de ave, determine la identificación
del tipo avistado con más frecuencia. Si se ha detectado más de 1 tipo
de esa cantidad máxima, devuelva la identificación más pequeña.

Ejemplo
arr:[1,1,2,2,3]

Hay dos de cada uno de los tipos 1 y 2, y un avistamiento de tipo 3. Elija el menor de los dos tipos vistos dos veces: tipo 1.'''

def migratoryBirds(arr:list):
    # Write your code here
    avistamientos= {key:arr.count(key) for key in arr  }
    
    typo_avistamientos = max(avistamientos.values())    
            
    return avistamientos[typo_avistamientos]

arry=[1, 2, 3, 4, 5, 4, 3 ,2 ,1 ,3 ,4,5]

print('estoy aqui',migratoryBirds(arry))