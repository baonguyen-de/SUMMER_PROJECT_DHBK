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

maintenance_option = [
    "Thêm lịch bảo dưỡng",
    "Xem danh sách bảo dưỡng",
    "Xóa lịch bảo dưỡng",
    "Kiểm tra cảnh báo bảo dưỡng",
    "Quay lại"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Hàm nhập số dùng chung ngắn gọn
def input_num(prompt, is_int=False):
    while True:
        try:
            v = int(input(prompt)) if is_int else float(input(prompt))
            if v >= 0: return v
            print("Lỗi: Không được nhập số âm!")
        except ValueError:
            print("Lỗi: Phải nhập số hợp lệ!")

# 1. Bảo dưỡng vấn đề
def add_maintenance():
    clear_screen()
    print("=== THỰC HIỆN BẢO DƯỠNG ===")
    
    open_idx = [i for i, s in enumerate(utils.issue_statuses) if s == "OPEN"]
    if not open_idx:
        return print("Không có vấn đề OPEN cần bảo dưỡng!"), input("\nNhấn ENTER...")

    for idx, i in enumerate(open_idx, 1):
        print(f"{idx}. {utils.issue_parts[i]} (Mức độ: {utils.issue_errors[i]})")

    choice = int(input_num("\nChọn STT bảo dưỡng (0 để hủy): ", is_int=True))
    if choice == 0 or choice > len(open_idx): return

    target_idx = open_idx[choice - 1]
    name = utils.issue_parts[target_idx]

    date = input("Nhập ngày (dd/mm/yyyy): ").strip() or "N/A"
    km = input_num("Nhập số km: ")
    cost = input_num("Nhập chi phí (VND): ")

    # Lưu dữ liệu vào 4 danh sách song song
    utils.maint_items.append(f"Bảo dưỡng: {name}")
    utils.maint_dates.append(date)
    utils.maint_kms.append(km)
    utils.maint_costs.append(cost)

    # Đồng bộ Expense & đóng Issue
    if not hasattr(utils, "expenses"): utils.expenses = []
    utils.expenses.append([f"Bảo dưỡng: {name}", "Bảo dưỡng", cost])
    utils.issue_statuses[target_idx] = "CLOSED"

    print(f"\n✅ Đã bảo dưỡng & đóng vấn đề '{name}'!")
    input("\nNhấn ENTER để tiếp tục...")

# 2. Xem lịch sử
def view_maintenance():
    clear_screen()
    print("--- LỊCH SỬ BẢO DƯỠNG ---")
    if not utils.maint_items:
        print("Chưa có lịch sử bảo dưỡng.")
    else:
        for i in range(len(utils.maint_items)):
            print(f"Hạng mục: {utils.maint_items[i]} | Ngày: {utils.maint_dates[i]} | {utils.maint_kms[i]:.0f} km | {utils.maint_costs[i]:,.0f} VND")
    input("\nNhấn ENTER để quay về...")

# 3. Xóa lịch sử
def delete_maintenance():
    clear_screen()
    if not utils.maint_items:
        return print("Chưa có lịch sử để xóa."), input("\nNhấn ENTER...")

    for i in range(len(utils.maint_items)):
        print(f"{i + 1}. {utils.maint_items[i]} - {utils.maint_dates[i]}")

    choice = int(input_num("\nChọn STT xóa (0 để hủy): ", is_int=True))
    if 0 < choice <= len(utils.maint_items):
        idx = choice - 1
        item_name, cost_to_remove = utils.maint_items[idx], utils.maint_costs[idx]

        # Xóa đồng thời trên cả 4 danh sách song song
        for lst in (utils.maint_items, utils.maint_dates, utils.maint_kms, utils.maint_costs):
            lst.pop(idx)

        # Đồng bộ xóa Expense
        if hasattr(utils, "expenses"):
            utils.expenses = [e for e in utils.expenses if not (e[0] == item_name and e[2] == cost_to_remove)]
        
        print("\n✅ Đã xóa lịch sử thành công!")
    input("\nNhấn ENTER để tiếp tục...")

# 4. Kiểm tra cảnh báo
def check_maintenance_warning():
    clear_screen()
    if not utils.maint_kms:
        return print("Chưa có dữ liệu bảo dưỡng."), input("\nNhấn ENTER...")

    last_km = max(utils.maint_kms)
    print(f"Km lần bảo dưỡng gần nhất: {last_km:.0f} km")
    current_km = input_num("Nhập số km hiện tại: ")

    diff = current_km - last_km
    print(f"Quãng đường đã đi thêm: {diff:.0f} km")
    print("\n⚠️ NÊN BẢO DƯỠNG XE!" if diff >= 5000 else "\n✅ Xe hoạt động an toàn.")
    input("\nNhấn ENTER để tiếp tục...")


  