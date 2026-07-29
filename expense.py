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

# Các nhóm chi phí cố định
EXPENSE_CATEGORIES = [
    "Năng lượng",
    "Bảo dưỡng",
    "Bảo hiểm",
    "Phụ kiện",
    "Khác",
]


# ==========================================
# CÁC HÀM CHỨC NĂNG CỐT LÕI
# ==========================================


def add_expense():
    """1. Thêm chi phí mới thủ công."""
    print("\n--- THÊM CHI PHÍ MỚI ---")
    description = input("Nhập mô tả chi phí: ").strip()
    if not description:
        print("Lỗi: Mô tả không được để trống!")
        return

    # Chọn nhóm chi phí bằng cách nhập số
    print("\nChọn nhóm chi phí:")
    for idx, cat in enumerate(EXPENSE_CATEGORIES, 1):
        print(f"{idx}. {cat}")

    while True:
        cat_choice = input(
            f"Chọn nhóm (1-{len(EXPENSE_CATEGORIES)}): "
        ).strip()
        try:
            cat_index = int(cat_choice) - 1
            if 0 <= cat_index < len(EXPENSE_CATEGORIES):
                category = EXPENSE_CATEGORIES[cat_index]
                break  
            else:
                print(f"Lỗi: Vui lòng nhập số từ 1 đến {len(EXPENSE_CATEGORIES)}!")
        except ValueError:
            print("Lỗi: Lựa chọn phải là số nguyên! Vui lòng nhập lại.")

    # Nhập số tiền
    while True:
        try:
            amount = float(input("Nhập số tiền (VND): "))
            if amount < 0:
                print("Lỗi: Số tiền không thể âm! Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Lỗi: Số tiền phải là số! Vui lòng nhập lại.")

    # Lưu dữ liệu vào utils
    if not hasattr(utils, "expenses"):
        utils.expenses = []

    expense_item = {
        "description": description,
        "category": category,
        "amount": amount,
    }
    utils.expenses.append(expense_item)

    print("\n=> Đã thêm chi phí thành công!")


def view_expense_history():
    """2. Xem lịch sử chi phí."""
    print("\n--- LỊCH SỬ CHI PHÍ ---")
    if not hasattr(utils, "expenses") or not utils.expenses:
        print("Chưa có khoản chi phí nào được ghi nhận.")
        return

    print(
        f"{'STT':<5} | {'Mô tả':<25} | {'Nhóm chi phí':<15} | {'Số tiền (VND)':<15}"
    )
    print("-" * 68)
    for idx, item in enumerate(utils.expenses, 1):
        print(
            f"{idx:<5} | {item['description']:<25} | {item['category']:<15} | {item['amount']:>13,.0f}"
        )


def calculate_total_expenses():
    """3 & 4. Tính tổng chi phí & tính chi phí theo nhóm."""
    print("\n--- BÁO CÁO TỔNG QUAN CHI PHÍ ---")
    if not hasattr(utils, "expenses") or not utils.expenses:
        print("Chưa có dữ liệu chi phí để tính toán.")
        return

    total = sum(item["amount"] for item in utils.expenses)
    print(f">>> TỔNG CHI PHÍ: {total:,.0f} VND <<<\n")

    print("Chi tiết theo từng nhóm:")
    for cat in EXPENSE_CATEGORIES:
        cat_total = sum(
            item["amount"]
            for item in utils.expenses
            if item["category"] == cat
        )
        if cat_total > 0:
            print(f" - {cat:<15}: {cat_total:>12,.0f} VND")


def delete_expense():
    """5. Xóa chi phí."""
    view_expense_history()
    if not hasattr(utils, "expenses") or not utils.expenses:
        return

    try:
        index = int(input("\nNhập STT khoản chi phí muốn xóa: ")) - 1
        if 0 <= index < len(utils.expenses):
            removed = utils.expenses.pop(index)
            print(
                f"=> Đã xóa thành công: '{removed['description']}' ({removed['amount']:,.0f} VND)"
            )
        else:
            print("Lỗi: STT không tồn tại!")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên!")


# ==========================================
# MENU ĐIỀU HƯỚNG ĐƠN GIẢN
# ==========================================


def expense_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== QUẢN LÝ CHI PHÍ ===")
        print("1. Xem lịch sử chi phí")
        print("2. Thêm chi phí")
        print("3. Tính tổng & chi phí theo nhóm")
        print("4. Xóa chi phí")
        print("0. Quay lại menu chính")

        choice = input("\nChọn chức năng (0-4): ").strip()

        if choice == "1":
            view_expense_history()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            calculate_total_expenses()
        elif choice == "4":
            delete_expense()
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!")

        input("\nẤn Enter để tiếp tục...")