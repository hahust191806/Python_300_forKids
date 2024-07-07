def check_even_old(n : int = None) -> str:
    if n == 0: 
        return "Số bạn nhập không phải là chẵn cũng không phải là lẻ!"
    elif n % 2 == 0: 
        return "Số bạn nhập là số chẵn"
    else: 
        return "Số bạn nhập là số lẻ"

try: 
    num = int(input("Nhập số nguyên cần kiểm tra: "))
    results = check_even_old(num)
    print(results)
except ValueError:
    print("Nhập số nguyên hợp lệ!")