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
#DS bộ phận xe
parts = [
    "Lốp xe",
    "Hệ thống phanh",
    "Đèn xe",
    "Điều hòa",
    "Pin hoặc hệ thống năng lượng"
]
statuses = ["OK", "WARNING", "ERROR"]
def inspection():
    print("KIỂM TRA TÌNH TRẠNG XE")
    while True:
        try:
            choice_part = int(input("Nhập số tương ứng với bộ phận: "))
            if 1 <= choice_part <= len(parts):
                selected_part = parts[choice_part - 1]
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 4.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\nChọn tình trạng của [{selected_part}]:")
    for i, status in enumerate(statuses, 1):
        print(f"{i}. {status}")
        
    while True:
        try:
            choice_status = int(input("Nhập số tương ứng với tình trạng: "))
            if 1 <= choice_status <= len(statuses):
                selected_status = statuses[choice_status - 1]
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 3.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" KẾT QUẢ KIỂM TRA XE ")
    print(f"- Bộ phận đã chọn:  {selected_part}")
    print(f"- Tình trạng:       {selected_status}")
    input("Nhấn ENTER để quay về:")

    



    


