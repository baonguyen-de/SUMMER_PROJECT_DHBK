"""
==================================================
MODULE: maintenance.py
==================================================

Vai trò:
    Quản lý quá trình bảo dưỡng và xử lý vấn đề của xe.

Chức năng chính:
    - Xem các vấn đề cần xử lý.
    - Bắt đầu xử lý vấn đề.
    - Thêm lịch sử bảo dưỡng.
    - Ghi nhận chi phí bảo dưỡng.
    - Hoàn tất bảo dưỡng.
    - Đóng vấn đề sau khi bảo dưỡng hoàn tất.

Luồng xử lý:
    ISSUE
        ↓
    MAINTENANCE
        ↓
    EXPENSE
        ↓
    ISSUE CLOSED

Ghi chú quan trọng:
    - Không được đóng vấn đề nếu chưa hoàn tất bảo dưỡng.
    - Khi bảo dưỡng phát sinh chi phí, chi phí phải được ghi nhận.
    - Sau khi bảo dưỡng hoàn tất, vấn đề phải được cập nhật trạng thái.
    - Dữ liệu được lưu trong utils.py.
"""
import os
import utils

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. Bảo dưỡng vấn đề và ĐÓNG VẤN ĐỀ (OPEN -> CLOSED)
def add_maintenance():
    clear_screen()
    print("=== THỰC HIỆN BẢO DƯỠNG ===")

    # Lọc các vấn đề đang OPEN
    open_indices = [i for i in range(len(utils.issue_parts)) if utils.issue_statuses[i] == "OPEN"]

    if not open_indices:
        print("Không có vấn đề nào đang OPEN cần bảo dưỡng!")
        input("\nNhấn ENTER để quay về")
        return

    print("Danh sách các vấn đề cần xử lý bảo dưỡng:")
    for idx, orig_i in enumerate(open_indices, 1):
        print(f"{idx}. {utils.issue_parts[orig_i]} (Mức độ: {utils.issue_errors[orig_i]})")

    try:
        choice = int(input("\nChọn STT vấn đề cần bảo dưỡng (0 để hủy): "))
        if choice == 0:
            return
        if not (1 <= choice <= len(open_indices)):
            print("Lựa chọn không hợp lệ!")
            input("\nNhấn ENTER để thử lại")
            return
    except ValueError:
        print("Vui lòng nhập số!")
        input("\nNhấn ENTER để thử lại")
        return

    # Lấy vị trí thực tế của vấn đề trong utils
    target_idx = open_indices[choice - 1]
    issue_name = utils.issue_parts[target_idx]

    print(f"\n---> Bắt đầu bảo dưỡng cho: {issue_name}")
    date = input("Nhập ngày thực hiện (dd/mm/yyyy): ")
    km = float(input("Nhập số kilomet hiện tại (km): "))
    cost = float(input("Nhập chi phí bảo dưỡng (VND): "))

    # 1. Lưu vào danh sách lịch sử bảo dưỡng
    utils.maint_items.append(f"Bảo dưỡng: {issue_name}")
    utils.maint_dates.append(date)
    utils.maint_kms.append(km)
    utils.maint_costs.append(cost)

    # 2. CHÍNH THỨC CHUYỂN TRẠNG THÁI ISSUE THÀNH CLOSED
    utils.issue_statuses[target_idx] = "CLOSED"

    print("\n✅ Đã ghi nhận lịch sử bảo dưỡng thành công!")
    print(f"✅ Trạng thái của '{issue_name}' đã được chuyển sang CLOSED!")
    input("\nNhấn ENTER để tiếp tục")

# 2. Xem lịch sử bảo dưỡng
def view_maintenance():
    clear_screen()
    print("=== LỊCH SỬ BẢO DƯỠNG XE ===\n")

    if not utils.maint_items:
        print("Chưa có lịch sử bảo dưỡng nào.")
        input("\nNhấn ENTER để quay về")
        return

    for i in range(len(utils.maint_items)):
        print(f"Hạng mục   : {utils.maint_items[i]}")
        print(f"Ngày       : {utils.maint_dates[i]}")
        print(f"Số kilomet : {utils.maint_kms[i]:.0f} km")
        print(f"Chi phí    : {utils.maint_costs[i]:.0f} VND")

    input("\nNhấn ENTER để quay về")

# 3. Xóa lịch sử bảo dưỡng
def delete_maintenance():
    clear_screen()
    print("=== XÓA LỊCH SỬ BẢO DƯỠNG ===")
    if not utils.maint_items:
        print("Chưa có lịch sử bảo dưỡng nào để xóa.")
        input("\nNhấn ENTER để quay về")
        return

    for i in range(len(utils.maint_items)):
        print(f"{i + 1}. {utils.maint_items[i]} - {utils.maint_dates[i]}")

    try:
        choice = int(input("\nChọn STT muốn xóa (0 để hủy): "))
        if 1 <= choice <= len(utils.maint_items):
            idx = choice - 1
            utils.maint_items.pop(idx)
            utils.maint_dates.pop(idx)
            utils.maint_kms.pop(idx)
            utils.maint_costs.pop(idx)
            print("\nĐã xóa lịch sử thành công!")
    except ValueError:
        pass

    input("\nNhấn ENTER để tiếp tục...")

# 4. Kiểm tra cảnh báo bảo dưỡng
def check_maintenance_warning():
    clear_screen()
    print("=== KIỂM TRA CẢNH BÁO BẢO DƯỠNG ===")
    if not utils.maint_kms:
        print("Chưa có dữ liệu bảo dưỡng nào để kiểm tra.")
        input("\nNhấn ENTER để quay về")
        return

    last_km = max(utils.maint_kms)
    print(f"Số km ở lần bảo dưỡng gần nhất: {last_km:.0f} km")
    
    try:
        current_km = float(input("Nhập số kilomet hiện tại của xe: "))
        km_diff = current_km - last_km
        
        print("\n" + "=" * 40)
        if km_diff >= 5000:
            print(f"Quãng đường đã đi thêm: {km_diff:.0f} km")
            print("\nXE CÓ THỂ CẦN ĐƯỢC BẢO DƯỠNG")
        else:
            print(f"Quãng đường đã đi thêm: {km_diff:.0f} km")
            print("\nXe vẫn hoạt động an toàn (Chưa vượt quá 5000 km).")
    except ValueError:
        print("Số km không hợp lệ!")

    input("\nNhấn ENTER để tiếp tục")

maintenance_option = [
    "Bảo dưỡng vấn đề",
    "Xem lịch sử bảo dưỡng",
    "Xóa lịch sử bảo dưỡng",
    "Kiểm tra cảnh báo bảo dưỡng",
    "Quay về menu chính"
]


  