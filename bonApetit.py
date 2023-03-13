def bonAppetit(bill, k, b):
    # Write your code here
    total__anna = (sum(bill) - bill[k]) / 2
    
    if (total__anna == b): print('Bon Appetit')
    
    else: print(abs(int(total__anna) - b))
    
    
bill = [3 ,10 ,2 ,9]
k=1
b=7

bonAppetit(k=k,b=b,bill=bill) 