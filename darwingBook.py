'''Un maestro le pide a la clase que abra sus libros
en un número de página. Un estudiante puede comenzar
a pasar las páginas desde el frente del libro o desde
la parte posterior del libro. Siempre pasan las páginas
de una en una. Cuando abren el libro, páginasiempre está
del lado derecho:

imagen

Cuando pasan la página, ven páginasy. Cada página excepto la
última página siempre se imprimirá en ambos lados. La última
página sólo podrá imprimirse en el anverso, dada la extensión
del libro. si el libro espáginas de largo, y un estudiante
quiere pasar a la página, ¿cuál es el número mínimo de página
s para pasar? Pueden comenzar al principio o al final del libro.

Dadoy, busque e imprima el número mínimo de páginas que deben
pasarse para llegar a la página.'''

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    page_book = range(n // 2 + 1)
    book=[(page * 2, page * 2 + 1) for page in page_book]
    initial_pag = 0
    final_pag = 0
    
    for i in page_book:   
        
        if(book[i][1] == p or book[i][0] == p):
            break
            
        initial_pag+=1
    for i in page_book:   
        
        if(book[-1+i][1] == p or book[-1+i][0] == p):
            break
            
        final_pag+=1
    
    
    if(initial_pag < final_pag):
        print(initial_pag)
    else:
        print(final_pag)
    
    
    
    
    

n = 6
p = 5

pageCount(n=n,p=p)