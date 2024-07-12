def tinh_tong(n: int = None) -> int:
    if n == 1: 
        return 1 
    return tinh_tong(n-1) + n 

print(tinh_tong(10))