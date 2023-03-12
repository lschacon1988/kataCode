def migratoryBirds(arr:list):
    # Write your code here
    avistamientos= {key:arr.count(key) for key in arr  }
    
    typo_avistamientos = max(avistamientos.values())    
            
    return avistamientos[typo_avistamientos]

arry=[1, 2, 3, 4, 5, 4, 3 ,2 ,1 ,3 ,4,5]

print('estoy aqui',migratoryBirds(arry))