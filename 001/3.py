def find_max_number(a: int = None, b: int = None, c: int = None) -> int:
    if a >= b and a >= c: 
        return a 
    elif b >= a and b >= c: 
        return b
    else: 
        return c 

try: 
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    c = int(input("Nhập số nguyên c: "))
    max = find_max_number(a, b, c)
    print(f"Số lớn nhất là: {max}")
except ValueError: 
    print("Vui lòng nhập số hợp lệ!")