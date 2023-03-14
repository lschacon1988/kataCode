def bonAppetit(bill, k, b):
    # Write your code here
    total__anna = int((sum(bill) - bill[k]) / 2)
    
    if (total__anna == b): print('Bon Appetit')
    
    else: print(abs(total__anna - b))
    
    
bill = [3 ,10 ,2 ,9]
k=1
b=8

bonAppetit(k=k,b=b,bill=bill) 

def fix(l:list):
    if(len(l)%2==0):
        new_list=[]
        for itm in l:
            for ele in itm:
                new_list.append(ele)
    else:
        new_list = [ele for ele in l for ele in ele]
    def my_fun(x):
        return x        
    new_list.sort(reverse=True, key = my_fun)
        
    return new_list 

l=[[3,4],[2,6]]
print(fix(l))