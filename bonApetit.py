def bonAppetit(bill, k, b):
    # Write your code here
    total__anna = int((sum(bill) - bill[k]) / 2)
    
    if (total__anna == b): print('Bon Appetit')
    
    else: print(abs(total__anna - b))
    
    
bill = [3 ,10 ,2 ,9]
k=1
b=8

bonAppetit(k=k,b=b,bill=bill) 