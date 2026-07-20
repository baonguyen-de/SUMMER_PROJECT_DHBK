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
from utils import car_info
def display_car_info():
    print("---THÔNG TIN XE---")
    print(f"Tên xe: {car_info[0]}")
    print(f"Loại xe: {car_info[1]}")
    print(f"Biển số: {car_info[2]}")
    print(f"Số kilomet: {car_info[3]}")
    print(f"Năm sản xuất: {car_info[4]}")

