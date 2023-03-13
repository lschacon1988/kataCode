
'''Marie inventó una máquina del tiempo
y quiere probarla viajando en el tiempo
para visitar Rusia en el Día del Programador (el día 256 del año)
durante un año en el rango inclusivo de 1700 a 2700.

Desde 1700 hasta 1917, el calendario oficial de Rusia
fue el calendario juliano ; desde 1919 utilizaron
el sistema de calendario gregoriano . La transición del
sistema de calendario juliano al gregoriano ocurrió en 1918,
cuando el día siguiente al 31 de enero era el 14 de febrero. 
Esto significa que en 1918, el 14 de febrero era el día 32 del año en Rusia.'''

def day_of_programmer(year):
    # Write your code here 
    if year == 1918: return '26.09'+str(year)   
    if( year <= 1917 and year % 4 == 0 ):
        return '12.09.'+str(year)
    elif(year % 4 == 0 and (year % 100 != 0  or year % 400 == 0)):
        return '12.09.'+str(year)
    return '13.09.'+ str(year)


print(day_of_programmer(1988)) 
