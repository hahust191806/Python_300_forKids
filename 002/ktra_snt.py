def check_snt(n: int = None) -> bool:
    if n <= 1: 
        return False 
    flag = True
    i = 2
    while i < n: 
        if n % i == 0: 
            flag = False 
            break 
        i+=1 
    
    return flag 

print(check_snt(23))