"""
==================================================
MODULE: menu.py
==================================================

Vai trò:
    Quản lý giao diện menu và điều hướng chương trình.

Chức năng chính:
    - Hiển thị menu.
    - Điều hướng bằng phím mũi tên lên.
    - Điều hướng bằng phím mũi tên xuống.
    - Xác nhận lựa chọn bằng phím Enter.
    - Gọi module tương ứng.

Ghi chú:
    - menu.py chỉ xử lý điều hướng.
    - Không xử lý logic quản lý xe.
    - Không trực tiếp quản lý dữ liệu.
"""
import readchar
import os
import trip
options = [
    "Quản lý thông tin xe",
    "Quản lý chuyến đi",
    "Quản lý năng lượng",
    "Quản lý bảo dưỡng",
    "Quản lý chi phí",
    "Kiểm tra tình trạng xe",
    "Vấn đề và cảnh báo",
    "Quản lý phụ kiện",
    "Báo cáo phiên sử dụng",
    "Thoát"
]
def render_menu(selected_index):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---CARCARE MANAGER---")
    for i, option in enumerate(options):
        if i == selected_index:
            print(f"> \033[32m{option}\033[0m")
        else:
            print(f"    {option}")
def menu_choice():
    current_index = 0
    while True:
        render_menu(current_index)
        key = readchar.readkey()
        if key == readchar.key.UP:
            current_index = (current_index -1) % len(options)
        elif key == readchar.key.DOWN:
            current_index = (current_index + 1) % len(options)
        elif key == readchar.key.ENTER:
            return current_index

while True:
    selected_option = menu_choice()
    os.system('cls' if os.name == 'nt' else 'clear')
    import car
    if selected_option == 0:
        car.get_car_info()
        car.update_car_info()
    elif selected_option == 1:
        trip.trip_menu()
    elif selected_option == 9:
        break




        


   
    
  

    
    
    