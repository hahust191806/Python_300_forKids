def is_leap_year(year: int = None):
    if year % 4 == 0: 
        return True
    else: return False
    
try: 
    year = int(input("Nhập năm muốn kiểm tra: "))
    print(is_leap_year(year))
except ValueError: 
    print("Nhập một số nguyên hợp lệ!")