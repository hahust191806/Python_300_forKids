def tinh_tong(n: int = None) -> int: 
    num = 0 
    while n != 0: 
        num += n % 10
        n = n // 10 
    
    return num 

print(tinh_tong(123))