"""
==================================================
MODULE: expense.py
==================================================

Vai trò:
    Quản lý các khoản chi phí liên quan đến xe.

Các nhóm chi phí:
    - Năng lượng.
    - Bảo dưỡng.
    - Bảo hiểm.
    - Phụ kiện.
    - Khác.

Chức năng chính:
    - Thêm chi phí.
    - Xem lịch sử chi phí.
    - Tính tổng chi phí.
    - Tính chi phí theo nhóm.
    - Xóa chi phí.

Ghi chú:
    - Dữ liệu được lưu trong utils.py.
    - Chi phí bảo dưỡng có thể được tạo từ maintenance.py.
    - Chi phí phụ kiện có thể được tạo từ accessory.py.
    - Không yêu cầu người dùng nhập lại chi phí đã được tự động ghi nhận.
"""

import os
import utils

EXPENSE_CATEGORIES = ["Năng lượng", "Bảo dưỡng", "Bảo hiểm", "Phụ kiện", "Khác"]

# Hàm phụ trợ nhập số tổng quát
def input_num(prompt, is_int=False):
    while True:
        try:
            v = int(input(prompt)) if is_int else float(input(prompt))
            if v >= 0: return v
            print("Lỗi: Không được nhập số âm!")
        except ValueError:
            print("Lỗi: Phải nhập số hợp lệ!")

# 1. Thêm chi phí
def add_expense():
    print("\n--- THÊM CHI PHÍ MỚI ---")
    while True:
        desc = input("Nhập mô tả chi phí: ").strip()
        if desc: break
        print("Lỗi: Mô tả không được để trống!")

    print("\nChọn nhóm chi phí:")
    for idx, cat in enumerate(EXPENSE_CATEGORIES, 1):
        print(f"{idx}. {cat}")

    cat_idx = int(input_num(f"Chọn nhóm (1-{len(EXPENSE_CATEGORIES)}): ", is_int=True)) - 1
    if not (0 <= cat_idx < len(EXPENSE_CATEGORIES)):
        return print("Lỗi: Lựa chọn không hợp lệ!")

    amount = input_num("Nhập số tiền (VND): ")

    if not hasattr(utils, "expenses"): utils.expenses = []
    utils.expenses.append([desc, EXPENSE_CATEGORIES[cat_idx], amount])
    print("\n=> Đã thêm chi phí thành công!")

# 2. Xem lịch sử
def view_expense_history():
    print("\n--- LỊCH SỬ CHI PHÍ ---")
    expenses = getattr(utils, "expenses", [])
    if not expenses:
        return print("Chưa có khoản chi phí nào được ghi nhận.")

    print(f"{'STT':<5} | {'Mô tả':<25} | {'Nhóm chi phí':<15} | {'Số tiền (VND)':<15}\n" + "-" * 68)
    for idx, item in enumerate(expenses, 1):
        print(f"{idx:<5} | {item[0]:<25} | {item[1]:<15} | {item[2]:>13,.0f}")

# 3 & 4. Báo cáo tổng quan
def calculate_total_expenses():
    print("\n\033[32m--- BÁO CÁO TỔNG QUAN CHI PHÍ ---\033[0m")
    expenses = getattr(utils, "expenses", [])
    if not expenses:
        return print("Chưa có dữ liệu chi phí để tính toán.")

    total = sum(item[2] for item in expenses)
    print(f">>> TỔNG CHI PHÍ: {total:,.0f} VND <<<\n\nChi tiết theo từng nhóm:")
    
    for cat in EXPENSE_CATEGORIES:
        cat_total = sum(item[2] for item in expenses if item[1] == cat)
        if cat_total > 0:
            print(f" - {cat:<15}: {cat_total:>12,.0f} VND")

# 5. Xóa chi phí
def delete_expense():
    expenses = getattr(utils, "expenses", [])
    if not expenses:
        return print("Chưa có chi phí nào để xóa.")
        
    view_expense_history()
    choice = int(input_num("\nNhập STT khoản chi phí muốn xóa (0 để hủy): ", is_int=True))
    
    if 0 < choice <= len(expenses):
        removed = expenses.pop(choice - 1)
        print(f"=> Đã xóa thành công: '{removed[0]}' ({removed[2]:,.0f} VND)")
    elif choice != 0:
        print("Lỗi: STT không tồn tại!")








