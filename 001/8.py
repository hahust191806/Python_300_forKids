def count_old_even(list_num: list = None) -> list[int, int]:
    count_old = 0 
    for idx in range(len(list_num)):
        if list_num[idx] % 2 == 0: 
            count_old += 1
    return count_old, len(list_num) - count_old

# Nhập danh sách các số nguyên từ người dùng
try:
    input_list = input("Nhập các số nguyên, cách nhau bằng dấu cách: ")
    numbers = [int(num) for num in input_list.split()]
    even_count, odd_count = count_old_even(numbers)
    print(f"Số lượng số chẵn: {even_count}")
    print(f"Số lượng số lẻ: {odd_count}")
except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ.")