'''¡Su biblioteca local necesita su ayuda! Dadas las
fechas de devolución esperadas y reales de un libro de
la biblioteca, cree un programa que calcule la multa
(si corresponde). La estructura de tarifas es la
siguiente:

Si el libro se devuelve en la fecha de devolución 
prevista o antes, no se cobrará ninguna multa 
(es decir: fine = 0).
Si el libro se devuelve después del día de devolución
previsto , pero aún dentro del mismo mes y año 
calendario que la fecha de devolución prevista,
fine = 15 Hanckos x(the number of days late).
Si el libro se devuelve después del mes de devolución
esperado pero aún dentro del mismo año calendario que la
fecha de devolución esperada, el fine = 500 Hackos x (the number of months late).
Si el libro se devuelve después del año natural en que
se esperaba, se impone una multa fija de 10000 Hackos.
Los cargos se basan únicamente en la medida menos 
precisa de retraso. Por ejemplo, si un libro vence el 1
de enero de 2017 o el 31 de diciembre de 2017, si se
devuelve el 1 de enero de 2018, es un año de retraso y
la multa sería. 10000 Hackos'''

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#
import datetime
import math


def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    day = datetime.date(day=d1, month=m1, year=y1)
    day2 = datetime.date(day=d2, month=m2, year=y2)

    
    if (day <= day2):
        return 0   

    if (day.year != day2.year):
        return 10000

    if ((day2 != day)):
        diferencia = abs(day2 - day)

        if (diferencia.days > 30 and (day2.month!=2)):
            
            return 500 * (round(diferencia.days / 30))
        elif day2.month == 2:
            return  500 * (round(diferencia.days / 28))

        return 15 * diferencia.days
    pass


d1 = 9
m1 = 6
y1 = 2015
d2 = 6
m2 = 6
y2 = 2015

print(libraryFine(d1=d1, m1=m1, y1=y1, y2=y2, d2=d2, m2=m2))
