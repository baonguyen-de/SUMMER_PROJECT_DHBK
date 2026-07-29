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

import readchar
import os
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

