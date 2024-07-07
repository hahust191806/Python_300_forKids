def calculate_taxi_money(s: int = None) -> int:
    if s <= 1: 
        return s * 10000
    elif s <= 10: 
        return s * 8500
    else: return s * 7500

try: 
    s = int(input("Nhập số km mà khách đi!"))
except ValueError: 
    print("Vui lòng nhập số km đúng!")