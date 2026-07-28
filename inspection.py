"""
==================================================
MODULE: inspection.py
==================================================

Vai trò:
    Kiểm tra tình trạng các bộ phận chính của xe.

Các bộ phận kiểm tra:
    - Lốp xe.
    - Hệ thống phanh.
    - Đèn xe.
    - Điều hòa.
    - Pin hoặc hệ thống năng lượng.

Trạng thái:
    - OK.
    - WARNING.
    - ERROR.

Chức năng chính:
    - Thực hiện kiểm tra xe.
    - Cập nhật trạng thái bộ phận.
    - Xem kết quả kiểm tra.
    - Phát hiện bộ phận có vấn đề.

Luồng liên kết:
    INSPECTION
        ↓
    Phát hiện WARNING hoặc ERROR
        ↓
    ISSUE

Ghi chú:
    - Module này chỉ phát hiện vấn đề.
    - Không xử lý bảo dưỡng trực tiếp.
    - Không tự đóng vấn đề.
"""
import os
import issue
import utils  

#DS bộ phận xe
parts = [
    "Lốp xe",
    "Hệ thống phanh",
    "Đèn xe",
    "Điều hòa",
    "Pin hoặc hệ thống năng lượng"
]

#DS trạng thái
statuses = ["OK", "WARNING", "ERROR"]

#Hàm kiểm tra bộ phận xe
def status():
    for part_name in parts:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nChọn tình trạng của \033[34m{part_name}\033[0m:")
        for i, status in enumerate(statuses, 1):
            print(f"{i}. {status}")

        #vòng lặp để kiểm tra xem người dùng có nhập đúng yêu cầu không
        while True:
            try: #Lệnh try - except để kiểm tra giá trị lỗi (ValueError)
                choice_status = int(input("Nhập số tương ứng với tình trạng: "))
                if 1 <= choice_status <= len(statuses):
                    selected_status = statuses[choice_status - 1]
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 3.")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ!")
        #thêm trạng thái vào list
        utils.inspection_results.append(selected_status)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== KẾT QUẢ KIỂM TRA TẤT CẢ BỘ PHẬN ===")
    for part_name, status in zip(parts, utils.inspection_results): #hàm zip ghép các trạng thái tương ứng với các bộ phận
        print(f"- \033[34m{part_name}\033[0m: {status}")
        if selected_status == "WARNING" or selected_status == "ERROR":
                issue.create_issue(part_name, status)
    input("\nNhấn ENTER để quay về menu chính:") #quay về menu chính



   

    



    


