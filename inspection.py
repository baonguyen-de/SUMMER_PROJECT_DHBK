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
import utils
import issue  # Import module issue để tự động tạo vấn đề khi phát hiện lỗi

# Danh sách bộ phận xe
parts = [
    "Lốp xe",
    "Hệ thống phanh",
    "Đèn xe",
    "Điều hòa",
    "Pin hoặc hệ thống năng lượng"
]

# Danh sách trạng thái
statuses = ["OK", "WARNING", "ERROR"]

def status():
    # Xóa dữ liệu kiểm tra cũ
    utils.inspection_results.clear()

    # Vòng lặp cho người dùng nhập tình trạng từng bộ phận
    for part_name in parts:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nChọn tình trạng của \033[34m{part_name}\033[0m:")
        for i, st in enumerate(statuses, 1):
            print(f"{i}. {st}")

        # Vòng lặp kiểm tra nhập liệu hợp lệ
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
        
        # Thêm trạng thái vào danh sách kết quả
        utils.inspection_results.append(selected_status)

    # Hiển thị bảng kết quả kiểm tra xe
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========== KIỂM TRA XE ==========\n")
    
    has_error = False
    
    # Ghép từng bộ phận với kết quả tương ứng
    for part_name, st in zip(parts, utils.inspection_results):
        print(f"{part_name:<30} [{st}]")
        
        # Nếu gặp WARNING hoặc ERROR thì tự động tạo Issue
        if st in ["WARNING", "ERROR"]:
            issue.create_issue(part_name, st)
        
        # Đánh dấu nếu phát hiện lỗi ERROR để hiển thị cảnh báo tổng thể
        if st == "ERROR":
            has_error = True

    print("\n" + "=" * 33)
    
    # Hiển thị cảnh báo nếu phát hiện trạng thái ERROR
    if has_error:
        print("\033[31m[CẢNH BÁO]: Phát hiện bộ phận ở trạng thái ERROR! Vui lòng kiểm tra và bảo dưỡng ngay.\033[0m")
    else:
        print("\033[32m[THÔNG BÁO]: Tất cả bộ phận đều hoạt động tốt hoặc ở mức chấp nhận được.\033[0m")

    input("\nNhấn ENTER để quay về menu chính...")



   

    



    


