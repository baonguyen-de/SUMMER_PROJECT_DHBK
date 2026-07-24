"""
==================================================
MODULE: trip.py
==================================================

Vai trò:
    Quản lý lịch sử các chuyến đi của xe.

Chức năng chính:
    - Thêm chuyến đi.
    - Xem lịch sử chuyến đi.
    - Xóa chuyến đi.
    - Tính tổng quãng đường.
    - Tìm chuyến đi dài nhất.

Thông tin chuyến đi:
    - Ngày.
    - Điểm đi.
    - Điểm đến.
    - Quãng đường.
    - Chế độ lái.

Ghi chú:
    - Dữ liệu chuyến đi được lưu trong utils.py.
    - Chỉ quản lý lịch sử chuyến đi.
    - Không xử lý chi phí hoặc bảo dưỡng.
"""

import utils

def add_trip(date: str, origin: str, destination: str, distance: float, mode: str):
    new_trip = [date, origin, destination, float(distance), mode]
    utils.trips.append(new_trip)
    print("-> Đã thêm chuyến đi thành công!")

def view_trip():
    if not utils.trips:
        print("\nLịch sử chuyến đi trống.")
        return None
    else:
        print("\n--- LỊCH SỬ CHUYẾN ĐI ---")  
        for i, trip in enumerate(utils.trips, start=1):
            date, origin, destination, distance, mode = trip
            print(f"{i}.Ngày: {date} | Từ: {origin} Đến: {destination} | Khoảng cách: {distance} km | Chế độ lái: {mode}")

def total_distance():
    ans = 0
    for i in utils.trips:
        ans += i[3]
    return ans

def find_longest_distance():
    if not utils.trips:
        return None
    else:
        longest = max(utils.trips, key=lambda trip: trip[3])
        return longest

def delete_trip():
    view_trip()
    if not utils.trips:
        return
    try:
        index = int(input("\nNhập STT muốn xóa (nhập 0 để hủy): "))
        if index == 0:
            print("Đã hủy xóa.")
            return

        if 1 <= index <= len(utils.trips):
            removed = utils.trips.pop(index - 1)
            print(f"-> Đã xóa chuyến đi: {removed[1]} --> {removed[2]}")
        else:
            print("-> Số thứ tự không hợp lệ.")
    except ValueError:
        print("Lỗi: Phải nhập số nguyên!")

def trip_menu():
    while True:
        print("\n=== QUẢN LÝ CHUYẾN ĐI ===")
        print("1. Xem danh sách chuyến đi")
        print("2. Thêm chuyến đi mới")
        print("3. Xóa chuyến đi")
        print("4. Xem tổng quãng đường & tìm chuyến đi dài nhất")
        print("0. Quay lại menu chính")
        
        choice = input("Chọn chức năng (0-4): ").strip()
        
        if choice == '1':
            view_trip()
            
        elif choice == '2':
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
                    print("Lỗi: Quãng đường phải là số! Vui lòng nhập lại.")
                
            mode = input("Nhập chế độ lái: ")
            add_trip(date, origin, destination, distance, mode)
            
        elif choice == '3':
            delete_trip()
            
        elif choice == '4':
            print(f"\n- Tổng quãng đường đã đi: {total_distance()} km")
            longest = find_longest_distance()
            if longest:
                print(f"- Chuyến đi dài nhất: {longest[1]} -> {longest[2]} ({longest[3]} km)")
            else:
                print("- Chưa có dữ liệu chuyến đi để tìm.")
                
        elif choice == '0':
            break
            
        else:
            print("Lựa chọn không hợp lệ!")
        
        input("\nẤn Enter để tiếp tục...")