def tinh_luy_thua(n: int = None, k: int = None) -> int: 
    rs = 1 
    i = 1
    while i <= k:
        rs *= n
        i += 1 
        
    return rs 

print(tinh_luy_thua(2, 3))