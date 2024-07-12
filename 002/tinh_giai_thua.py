def tinh_giai_thua(n: int = None):
    if n == 1: 
        return 1 
    return n * tinh_giai_thua(n-1)

print(tinh_giai_thua(5))