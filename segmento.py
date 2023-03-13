def segmento(s,d,m):
    
    count=0
    len_segmento = len(s)
    range_segmento = range(m,len_segmento + 1)   
    
    for i in range_segmento:
        temp = sum(s[i-m:i])
        
        if(temp == d):
            count += 1
            
    return count

s = [1 ,2, 1, 3, 2]
d =  3
m =  2

print('seg',segmento(s=s,d=d,m=m))