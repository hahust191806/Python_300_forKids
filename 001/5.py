def calculate_average(list_score: list = None) -> float: 
    return sum(list_score) / len(list_score)

def classify_student(average_score: float = None) -> str: 
    if average_score >= 8.5: return "Xuất sắc"
    elif average_score >= 7.0: return "Giỏi"
    elif average_score >= 5.5: return "Khá"
    elif average_score >= 4.0: return "Trung bình"
    else: return "Yếu"
    
try: 
    scores = []
    num_subjects = int(input("Nhập số lượng môn học"))
    if num_subjects <= 0: 
        print("Số lượng môn học phải lớn hơn 0!")
    else: 
        for _ in range(num_subjects):
            score = float(input("Nhập điểm môn học: "))
            if score < 0 or score > 10: 
                print("Điểm số phải từ 0 đến 10. Vui lòng nhập lại")
                break
            scores.append(score)
            
        average_score = calculate_average(scores)
        classification = classify_student(average_score)
        print(f"Hạng của học sinh là: {classify_student}")
except ValueError: 
    print("Vui lòng nhập một số hợp lệ!")