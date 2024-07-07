def check_number(n : int = None) -> str:
    if n > 0: 
        return "Số nhập là số dương"
    elif n < 0: 
        return "Số nhập là số âm"
    else: 
        return "Số nhập là số 0"
    
try: 
    number = int(input("Nhập số nguyên: "))
    results = check_number(number)
    print(results)
except ValueError: 
    print("Vui lòng nhập số hợp lệ!")