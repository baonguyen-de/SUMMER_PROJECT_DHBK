"""
==================================================
MODULE: energy.py
==================================================

Vai trò:
    Theo dõi và quản lý mức tiêu thụ năng lượng của xe.

Chức năng chính:
    - Ghi nhận thông tin sử dụng năng lượng.
    - Tính lượng năng lượng đã sử dụng.
    - Xem lịch sử sử dụng năng lượng.

Hỗ trợ:
    - Xe điện.
    - Xe sử dụng nhiên liệu.

Ghi chú:
    - Dữ liệu được lưu trong utils.py.
    - Chỉ sử dụng List.
    - Không sử dụng Dictionary hoặc Set.
"""

import utils


def electric_energy():
    """Ghi nhận tiêu thụ Xe Điện (Bao gồm giao diện nhập liệu)"""
    print("\n--- GHI NHẬN NĂNG LƯỢNG XE ĐIỆN ---")

    # Nhập pin ban đầu
    while True:
        try:
            init_bat = float(input("Nhập Mức pin ban đầu (%): "))
            if 0 <= init_bat <= 100:
                break
            print("Lỗi: Pin phải nằm trong khoảng từ 0 đến 100%!")
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ!")

    # Nhập pin còn lại
    while True:
        try:
            final_bat = float(input("Nhập Mức pin còn lại (%): "))
            if 0 <= final_bat <= init_bat:
                break
            print("Lỗi: Pin còn lại phải từ 0% và không thể lớn hơn pin ban đầu!")
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ!")

    # Nhập quãng đường
    while True:
        try:
            distance = float(input("Nhập Quãng đường đã đi (km): "))
            if distance >= 0:
                break
            print("Lỗi: Quãng đường không thể âm!")
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ!")

    # Lưu vào utils.energy
    if not hasattr(utils, "energy"):
        utils.energy = []

    used_bat = init_bat - final_bat
    record = ["electric", init_bat, final_bat, 0, distance]
    utils.energy.append(record)
    print(f"\n=> Đã ghi nhận thành công! Pin đã sử dụng: {used_bat}%")


def gas_energy():
    """Ghi nhận tiêu thụ Xe Xăng (Bao gồm giao diện nhập liệu)"""
    print("\n\033[32m--- GHI NHẬN NĂNG LƯỢNG XE XĂNG ---\033[0m")

    # Nhập nhiên liệu đã dùng
    while True:
        try:
            fuel_used = float(input("Nhập Số lít nhiên liệu đã dùng (L): "))
            if fuel_used >= 0:
                break
            print("Lỗi: Số lít nhiên liệu không thể âm!")
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ!")

    # Nhập quãng đường
    while True:
        try:
            distance = float(input("Nhập Quãng đường đã đi (km): "))
            if distance >= 0:
                break
            print("Lỗi: Quãng đường không thể âm!")
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ!")

    # Lưu vào utils.energy
    if not hasattr(utils, "energy"):
        utils.energy = []

    consumption = (fuel_used / distance) * 100 if distance > 0 else 0
    record = ["gas", 0, 0, fuel_used, distance]
    utils.energy.append(record)
    print(f"\n=> Đã ghi nhận thành công! Mức tiêu thụ: {consumption:.2f} L/100km")


def view_energy_history():
    """Xem lịch sử tiêu thụ năng lượng"""
    print("\n\033[32m--- LỊCH SỬ TIÊU THỤ NĂNG LƯỢNG ---\033[0m")
    if not hasattr(utils, "energy") or not utils.energy:
        print("Lịch sử trống.")
        return

    for i, rec in enumerate(utils.energy, start=1):
        loai_xe = rec[0]
        if loai_xe == "electric":
            pin_da_dung = rec[1] - rec[2]
            print(f"{i}. [Xe Điện] Quãng đường: {rec[4]} km | Pin dùng: {pin_da_dung}%")
        elif loai_xe == "gas":
            tieu_thu = (rec[3] / rec[4]) * 100 if rec[4] > 0 else 0
            print(f"{i}. [Xe Xăng] Quãng đường: {rec[4]} km | Nhiên liệu: {rec[3]} L | Mức tiêu thụ: {tieu_thu:.2f} L/100km")