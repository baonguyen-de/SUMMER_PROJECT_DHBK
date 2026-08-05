"""
==================================================
MODULE: car.py
==================================================

Vai trò:
    Quản lý thông tin cơ bản của một chiếc xe.

Chức năng chính:
    - Xem thông tin xe.
    - Cập nhật thông tin xe.
    - Cập nhật số kilomet hiện tại.

Thông tin xe:
    - Tên xe.
    - Loại xe.
    - Biển số.
    - Số kilomet hiện tại.
    - Năm sản xuất.

Ghi chú:
    - Project chỉ quản lý một chiếc xe duy nhất.
    - Dữ liệu xe được lưu trong utils.py.
    - Không xử lý chuyến đi, bảo dưỡng hoặc chi phí.
"""
import utils

# Đảm bảo utils.car_info luôn được khởi tạo
if not hasattr(utils, "car_info"):
    utils.car_info = []

# --- HÀM HỖ TRỢ NHẬP DỮ LIỆU ---
def get_non_empty_input(prompt):
    """Đảm bảo không bỏ trống chuỗi"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("\033[31mCảnh báo: Thông tin này không được để trống!\033[0m")

def car_km():
    while True:
        try:
            val = float(input("Nhập số km: "))
            if val >= 0:
                return val
            print("\033[31mCảnh báo: Số km không được là số âm.\033[0m")
        except ValueError:
            print("\033[31mCảnh báo: Số km không hợp lệ. Vui lòng nhập lại.\033[0m")

def car_year():
    while True:
        try:
            val = int(input("Nhập năm sản xuất: "))
            if 1886 <= val <= 2026:
                return val
            print("\033[31mCảnh báo: Năm sản xuất phải từ 1886 đến 2026.\033[0m")
        except ValueError:
            print("\033[31mCảnh báo: Năm sản xuất không hợp lệ. Vui lòng nhập lại.\033[0m")

# --- HÀM XỬ LÝ CHÍNH ---
def display_car_info():
    """Hiển thị thông tin xe hiện tại"""
    if not utils.car_info or len(utils.car_info) < 5:
        print("\033[33mChưa có thông tin xe trong hệ thống.\033[0m")
        return False

    print("\033[32m--- THÔNG TIN XE HIỆN TẠI ---\033[0m")
    print(f"Tên xe       : {utils.car_info[0]}")
    print(f"Loại xe      : {utils.car_info[1]}")
    print(f"Biển số      : {utils.car_info[2]}")
    print(f"Số kilomet   : {utils.car_info[3]} km")
    print(f"Năm sản xuất : {utils.car_info[4]}")
    return True

def get_car_info():
    """Nhập thông tin xe mới (Ghi đè hoàn toàn thông tin cũ)"""
    print("\n--- NHẬP THÔNG TIN XE MỚI ---")
    car_name = get_non_empty_input("Nhập tên xe: ")
    car_type = get_non_empty_input("Nhập loại xe: ")
    car_number = get_non_empty_input("Nhập biển số: ")
    car_km_val = car_km()
    car_year_val = car_year()

    # Ghi đè toàn bộ danh sách car_info bằng dữ liệu mới
    utils.car_info = [car_name, car_type, car_number, car_km_val, car_year_val]
    print("\n\033[32m-> Đã cập nhật thông tin xe thành công!\033[0m")

def run():
    """Hàm chạy khi gọi từ Menu chính"""
    # 1. Nếu chưa có thông tin xe -> Yêu cầu nhập lần đầu
    if not utils.car_info:
        get_car_info()
        input("\nNhấn Enter để tiếp tục")
    else:
        # 2. Nếu đã có xe -> Hiện thông tin cũ và cho phép cập nhật đè
        display_car_info()
        print("\n[1] Nhập lại thông tin xe mới: ")
        print("[0] Bấm Enter để quay lại")
        
        choice = input("\nLựa chọn của bạn: ").strip()
        if choice == "1":
            get_car_info()
            input("\nNhấn Enter để tiếp tục...")
            




