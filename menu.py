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
import car
import inspection
import issue
import trip
import expense
import accessory
import energy
import issue
import maintenance
import report

# Menu maintenance
def render_maintenance_menu(selected_maintenance_choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---VẤN ĐỀ VÀ CẢNH BÁO---")
    for i, option in enumerate(maintenance.maintenance_option):
        if i == selected_maintenance_choice:
            print(f"> \033[32m{option}\033[0m")
        else:
            print(f"    {option}")
def maintenance_choice():
    current_index = 0
    while True:
        render_maintenance_menu(current_index)
        key = readchar.readkey()
        if key == readchar.key.UP:
            current_index = (current_index -1) % len(maintenance.maintenance_option)
        elif key == readchar.key.DOWN:
            current_index = (current_index + 1) % len(maintenance.maintenance_option)
        elif key == readchar.key.ENTER:
            return current_index
def maintenance_run():
    while True:
        selected_option = maintenance_choice()
        os.system('cls' if os.name == 'nt' else 'clear')
        if selected_option == 0:
            maintenance.add_maintenance()
        elif selected_option == 1:
            maintenance.view_maintenance()
        elif selected_option == 2:
            maintenance.delete_maintenance()
        elif selected_option == 3:
            maintenance.check_maintenance_warning()
        elif selected_option == 4:
            break

#Menu issue
def render_issue_menu(selected_issue_choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---VẤN ĐỀ VÀ CẢNH BÁO---")
    for i, function in enumerate(issue.functions):
        if i == selected_issue_choice:
            print(f"> \033[32m{function}\033[0m")
        else:
            print(f"    {function}")

def issue_menu_choice():
    current_index = 0
    while True:
        render_issue_menu(current_index)
        key = readchar.readkey()
        if key == readchar.key.UP:
            current_index = (current_index -1) % len(issue.functions)
        elif key == readchar.key.DOWN:
            current_index = (current_index + 1) % len(issue.functions)
        elif key == readchar.key.ENTER:
            return current_index
def issue_run():
    while True:
        selected_issue = issue_menu_choice()
        os.system('cls' if os.name == 'nt' else 'clear')
        if selected_issue == 0:
            issue.add_issue()
        elif selected_issue == 1:
            issue.view_issue()
        elif selected_issue == 2:
            issue.close_issue()
        elif selected_issue == 3:
            issue.delete_issue()
        elif selected_issue == 4:
            break
#Menu Trip.
def trip_menu():
    trip_options = [
        "Xem danh sách chuyến đi",
        "Thêm chuyến đi mới",
        "Xóa chuyến đi",
        "Xem tổng quãng đường & tìm chuyến đi dài nhất",
        "Quay lại menu chính",
    ]
    current_index = 0
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== QUẢN LÝ CHUYẾN ĐI ===")
        for i, option in enumerate(trip_options):
            if i == current_index:
                print(f"> \033[32m{option}\033[0m")
            else:
                print(f"    {option}")

        key = readchar.readkey()
        if key == readchar.key.UP:
            current_index = (current_index - 1) % len(trip_options)
        elif key == readchar.key.DOWN:
            current_index = (current_index + 1) % len(trip_options)
        elif key == readchar.key.ENTER:
            os.system("cls" if os.name == "nt" else "clear")

            # 1. Xem danh sách
            if current_index == 0:
                trip.view_trip()

            # 2. Thêm chuyến đi mới
            elif current_index == 1:
                trip.add_trip()

            # 3. Xóa chuyến đi
            elif current_index == 2:
                trip.delete_trip()

            # 4. Xem thống kê (Tổng & Dài nhất)
            elif current_index == 3:
                trip.show_summary()

            # 5. Quay lại menu chính
            elif current_index == 4:
                break

            input("\nẤn Enter để tiếp tục...")
#Menu energy
def energy_menu():
    options = [
        "Xem lịch sử tiêu thụ năng lượng",
        "Ghi nhận tiêu thụ XE ĐIỆN",
        "Ghi nhận tiêu thụ XE XĂNG",
        "Quay lại menu chính",
    ]

    current_index = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== QUẢN LÝ TIÊU THỤ NĂNG LƯỢNG ===")
        for i, option in enumerate(options):
            if i == current_index:
                print(f"> \033[32m{option}\033[0m")
            else:
                print(f"    {option}")

        key = readchar.readkey()
        if key == readchar.key.UP:
            current_index = (current_index - 1) % len(options)
        elif key == readchar.key.DOWN:
            current_index = (current_index + 1) % len(options)
        elif key == readchar.key.ENTER:
            os.system("cls" if os.name == "nt" else "clear")
            # 1. Xem lịch sử
            if current_index == 0:
                energy.view_energy_history()
            # 2. Ghi nhận Xe Điện 
            elif current_index == 1:
                energy.electric_energy()
            # 3. Ghi nhận Xe Xăng 
            elif current_index == 2:
                energy.gas_energy()
            # 4. Quay lại menu chính
            elif current_index == 3:
                break

            input("\nẤn Enter để tiếp tục...")
# Menu expense
def expense_menu():
    options = [
        "Xem lịch sử chi phí",
        "Thêm chi phí mới",
        "Tính tổng & chi phí theo nhóm",
        "Xóa chi phí",
        "Quay lại menu chính",
    ]

    current_index = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== QUẢN LÝ CHI PHÍ ===")
        for i, option in enumerate(options):
            if i == current_index:
                print(f"> \033[32m{option}\033[0m")
            else:
                print(f"    {option}")

        key = readchar.readkey()
        if key == readchar.key.UP:
            current_index = (current_index - 1) % len(options)
        elif key == readchar.key.DOWN:
            current_index = (current_index + 1) % len(options)
        elif key == readchar.key.ENTER:
            os.system("cls" if os.name == "nt" else "clear")

            if current_index == 0:
                expense.view_expense_history()
            elif current_index == 1:
                expense.add_expense()
            elif current_index == 2:
                expense.calculate_total_expenses()
            elif current_index == 3:
                expense.delete_expense()
            elif current_index == 4:
                break  # Quay lại menu chính

            input("\nẤn Enter để tiếp tục...")

#Menu accessory
def accessory_menu():

    options = [
        "Xem danh sách phụ kiện",
        "Thêm phụ kiện mới",
        "Tính tổng chi phí phụ kiện",
        "Xóa phụ kiện",
        "Quay lại menu chính",
    ]

    current_index = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== QUẢN LÝ PHỤ KIỆN ===")
        for i, option in enumerate(options):
            if i == current_index:
                print(f"> \033[32m{option}\033[0m")
            else:
                print(f"    {option}")

        key = readchar.readkey()
        if key == readchar.key.UP:
            current_index = (current_index - 1) % len(options)
        elif key == readchar.key.DOWN:
            current_index = (current_index + 1) % len(options)
        elif key == readchar.key.ENTER:
            os.system("cls" if os.name == "nt" else "clear")

            if current_index == 0:
                accessory.view_accessory_list()
            elif current_index == 1:
                accessory.add_accessory()
            elif current_index == 2:
                accessory.calculate_total_accessory_cost()
            elif current_index == 3:
                accessory.delete_accessory()
            elif current_index == 4:
                break  # Quay lại menu chính

            input("\nẤn Enter để tiếp tục...")
#Menu chính 


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
    import inspection
    import issue
    import maintenance
    import trip
    if selected_option == 0:
        car.run()
    elif selected_option == 1:
        trip_menu()
    elif selected_option == 2:
        energy_menu()
    elif selected_option == 3:
        maintenance_run()
    elif selected_option == 4:
        expense_menu()
    elif selected_option == 5:
        inspection.status()
    elif selected_option == 6:
        issue_run()
    elif selected_option == 7:
        accessory_menu()
    elif selected_option == 8:
        report.report()
    elif selected_option == 9:
        break




        


   
    
  

    
    
    