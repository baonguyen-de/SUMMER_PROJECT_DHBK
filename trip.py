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

