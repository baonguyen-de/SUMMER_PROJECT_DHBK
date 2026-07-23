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
def electric_energy(init_bat, final_bat, distance):
    used_bat = init_bat - final_bat
    record = ["electric", init_bat, final_bat, 0, distance]
    utils.energy.append(record)
    print(f"Đã ghi nhận ! Pin đã sử dụng : {used_bat}")

def gas_energy(fuel_used, distance):
    consumption = (fuel_used/distance)*100 if distance > 0 else 0
    record = ["gas", 0, 0, fuel_used, distance]
    utils.energy.append(record)
    print(f"Đã ghi nhận ! Mức tiêu thụ : {consumption}")

def view_energy_history():
    if not utils.energy:
        print("Lịch sử trống")
        return None
    print("\n=== LỊCH SỬ TIÊU THỤ NĂNG LƯỢNG ===")
    for i, rec in enumerate(utils.energy, start = 1):
        loai_xe = rec[0]
        if loai_xe == "electric":
            pin_da_dung = rec[1] - rec[2]
            print(f"{i}. [Xe Điện] Quãng đường: {rec[4]} km | Pin dùng: {pin_da_dung}%")
        elif loai_xe == "gas":
            tieu_thu = (rec[3] / rec[4]) * 100 if rec[4] > 0 else 0
            print(f"{i}. [Xe sử dụng nguyên liệu] Quãng đường: {rec[4]} km | Nhiên liệu: {rec[3]} L | Mức tiêu thụ: {tieu_thu:.2f}")
