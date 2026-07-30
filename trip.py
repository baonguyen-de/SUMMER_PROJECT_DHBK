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
from datetime import datetime
import utils


def add_trip():
    """Ghi nhận chuyến đi mới (Bao gồm giao diện nhập liệu chuẩn hóa)"""
    print("\n--- THÊM CHUYẾN ĐI MỚI ---")

    # 1. Nhập và kiểm tra định dạng Ngày (DD/MM/YYYY)
    while True:
        date_str = input("Nhập ngày (DD/MM/YYYY): ").strip()
        try:
            # Kiểm tra ngày hợp lệ (đúng định dạng và đúng ngày thực tế, ví dụ không có 31/02)
            valid_date = datetime.strptime(date_str, "%d/%m/%Y")
            formatted_date = valid_date.strftime("%d/%m/%Y")
            break
        except ValueError:
            print(
                "Lỗi: Định dạng ngày không hợp lệ! Vui lòng nhập đúng dạng DD/MM/YYYY (VD: 25/12/2026)."
            )

    # 2. Nhập Điểm đi (Không được để trống)
    while True:
        origin = input("Nhập điểm đi: ").strip()
        if origin:
            break
        print("Lỗi: Điểm đi không được để trống!")

    # 3. Nhập Điểm đến (Không được để trống và phải khác điểm đi)
    while True:
        destination = input("Nhập điểm đến: ").strip()
        if not destination:
            print("Lỗi: Điểm đến không được để trống!")
        elif destination.lower() == origin.lower():
            print("Lỗi: Điểm đến không được trùng với điểm đi!")
        else:
            break

    # 4. Nhập Quãng đường (Phải là số thực và lớn hơn 0)
    while True:
        try:
            distance = float(input("Nhập quãng đường (km): "))
            if distance > 0:
                break
            print("Lỗi: Quãng đường phải lớn hơn 0!")
        except ValueError:
            print("Lỗi: Quãng đường phải là số hợp lệ! Vui lòng nhập lại.")

    # 5. Nhập Chế độ lái (Không được để trống)
    while True:
        mode = input("Nhập chế độ lái (VD: Eco, Sport, Auto): ").strip()
        if mode:
            break
        print("Lỗi: Chế độ lái không được để trống!")

    # Lưu dữ liệu vào utils.trips
    if not hasattr(utils, "trips"):
        utils.trips = []

    new_trip = [formatted_date, origin, destination, distance, mode]
    utils.trips.append(new_trip)
    print("\n-> Đã thêm chuyến đi thành công!")


def view_trip():
    """Xem danh sách các chuyến đi"""
   

    print("\n\033[32m--- LỊCH SỬ CHUYỂN ĐI ---\033[0m")
    for i, trip in enumerate(utils.trips, start=1):
        date, origin, destination, distance, mode = trip
        print(
            f"{i}. Ngày: {date} | Từ: {origin} Đến: {destination} | "
            f"Khoảng cách: {distance} km | Chế độ lái: {mode}"
        )


def show_summary():
    if not utils.trips:
        print("Chưa có lịch sử chuyến đi nào.")
        return
    """Hiển thị tổng quãng đường và chuyến đi dài nhất"""
    # Tính tổng quãng đường
    total_dist = sum(trip[3] for trip in utils.trips)
    # Tìm chuyến đi dài nhất
    longest = max(utils.trips, key=lambda trip: trip[3])

    print(f"\n- Tổng quãng đường đã đi: {total_dist} km")
    print(
        f"- Chuyến đi dài nhất: {longest[1]} -> {longest[2]} ({longest[3]} km)"
    )


def delete_trip():
    """Xóa một chuyến đi khỏi danh sách"""
    view_trip()
    if not utils.trips:
        print("\nLịch sử chuyến đi trống.")
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


