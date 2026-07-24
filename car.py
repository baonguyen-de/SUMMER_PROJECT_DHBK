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
import os
import utils
#Hàm nhập tên xe
def car_name():
    CARNAME = str(input("Nhập tên xe: "))
    return CARNAME 

#Hàm nhập loại xe
def car_type():
    CARTYPE = str(input("Nhập loại xe: "))
    return CARTYPE 

#Hàm nhập biển số xe
def car_num():
    CARNUMBER = str(input("Nhập biển số: "))
    return CARNUMBER

#Hàm nhập số km
def car_km():
    valid = False
    while valid is False: 
        CARKM_str = input("Nhập số km: ")
        if CARKM_str.replace('.', '', 1).isdigit():
            CARKM = float(CARKM_str)
            valid = True
        else:
            print("\033[31mCảnh báo: Số km không hợp lệ. Vui lòng nhập lại.\033[0m")
    return CARKM

#Hàm nhập năm sản xuất
def car_year():
    valid = False
    while valid is False: 
        CARYEAR_str = input("Nhập năm sản xuất: ")
        if CARYEAR_str.replace('.', '', 1).isdigit():
            CARYEAR = int(CARYEAR_str)
            if 1886 <= CARYEAR <= 2026:
                valid = True
            else:
                print("\033[31mCảnh báo: Năm sản xuất không hợp lệ. Vui lòng nhập lại.\033[0m")
        else:
            print("\033[31mCảnh báo: Năm sản xuất không hợp lệ. Vui lòng nhập lại.\033[0m")
    return CARYEAR

#Hàm hiện thông tin xe
def display_car_info():
    print("\033[32m---THÔNG TIN XE---\033[0m")
    print(f"Tên xe: {utils.car_info[0]}")
    print(f"Loại xe: {utils.car_info[1]}")
    print(f"Biển số: {utils.car_info[2]}")
    print(f"Số kilomet: {utils.car_info[3]}")
    print(f"Năm sản xuất: {utils.car_info[4]}")

#Hàm chạy thông tin được nhập vào
def get_car_info():
    CARNAME = car_name()
    CARTYPE = car_type()
    CARNUMBER = car_num()
    CARKM = car_km()
    CARYEAR = car_year()    
    utils.car_info.clear()
    utils.car_info.extend([CARNAME, CARTYPE, CARNUMBER, CARKM, CARYEAR])
    display_car_info()
    return utils.car_info

#Hàm chạy thông tin mới update
def update_car_info():
    print("Bạn có muốn cập nhật thông tin xe? (y/n)")
    choice = input().lower()
    if choice == 'n':
        return 
    while choice == 'y':
        CARNAME = car_name()
        CARTYPE = car_type()
        CARNUMBER = car_num()
        CARKM = car_km()
        CARYEAR = car_year()    
        utils.car_info.clear()
        utils.car_info.extend([CARNAME, CARTYPE, CARNUMBER, CARKM, CARYEAR])
        display_car_info()
        update_car_info()
        return
            




