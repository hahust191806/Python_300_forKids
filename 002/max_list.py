def find_max(list_number: list = None) -> int: 
    max_num = 0 
    for idx, num in enumerate(list_number):
        if num > max_num: 
            max_num = num 
    
    return max_num

list_num = [3, 4, 5, 23, 9, 22, 20, 11]
print(find_max(list_num))
print(max(list_num))