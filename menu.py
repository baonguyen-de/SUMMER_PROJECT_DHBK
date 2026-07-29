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
import os
import readchar
import trip
import expense
import accessory
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
        # Render sub-menu
        os.system("cls" if os.name == "nt" else "clear")
        print("=== QUẢN LÝ CHUYẾN ĐI ===")
        for i, option in enumerate(trip_options):
            if i == current_index:
                print(f"> \033[32m{option}\033[0m")
            else:
                print(f"    {option}")

        # Bắt phím
        key = readchar.readkey()
        if key == readchar.key.UP:
            current_index = (current_index - 1) % len(trip_options)
        elif key == readchar.key.DOWN:
            current_index = (current_index + 1) % len(trip_options)
        elif key == readchar.key.ENTER:
            # Xử lý theo tính năng đã chọn
            if current_index == 0:
                trip.view_trip()

            elif current_index == 1:
                print("\n--- THÊM CHUYẾN ĐI MỚI ---")
                date = input("Nhập ngày (DD/MM/YYYY): ")
                origin = input("Nhập điểm đi: ")
                destination = input("Nhập điểm đến: ")

                # Lặp cho đến khi người dùng nhập đúng số quãng đường mới thôi
                while True:
                    try:
                        distance = float(input("Nhập quãng đường (km): "))
                        break  # Nhập đúng số -> Thoát khỏi vòng lặp nhập quãng đường
                    except ValueError:
                        print(
                            "Lỗi: Quãng đường phải là số! Vui lòng nhập lại."
                        )

                mode = input("Nhập chế độ lái: ")
                trip.add_trip(date, origin, destination, distance, mode)

            elif current_index == 2:
                trip.delete_trip()

            elif current_index == 3:
                print(f"\n- Tổng quãng đường đã đi: {trip.total_distance()} km")
                longest = trip.find_longest_distance()
                if longest:
                    print(
                        f"- Chuyến đi dài nhất: {longest[1]} -> {longest[2]} ({longest[3]} km)"
                    )
                else:
                    print("- Chưa có dữ liệu chuyến đi để tìm.")

            elif current_index == 4:
                break  # Quay lại menu chính

            input("\nẤn Enter để tiếp tục...")
#Menu expense
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
    import accessory  # Import chính module để dùng tiền tố accessory.

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
    elif selected_option == 4:
        expense_menu()
    elif selected_option == 5:
        inspection.status()
    elif selected_option == 6:
        issue.run()
    elif selected_option == 7:
        accessory_menu()
    elif selected_option == 9:
        break




        


   
    
  

    
    
    