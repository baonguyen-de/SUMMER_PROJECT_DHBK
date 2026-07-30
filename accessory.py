"""
==================================================
MODULE: accessory.py
==================================================

Vai trò:
    Quản lý các phụ kiện của xe.

Chức năng chính:
    - Thêm phụ kiện.
    - Xem danh sách phụ kiện.
    - Xóa phụ kiện.
    - Tính tổng chi phí phụ kiện.

Dữ liệu liên quan:
    - Tên phụ kiện.
    - Chi phí phụ kiện.

Ghi chú:
    - Dữ liệu được lưu trong utils.py.
    - Chi phí phụ kiện cần được ghi nhận vào hệ thống chi phí.
    - Không xử lý thông tin xe hoặc bảo dưỡng trong module này.
"""

POPULAR_ACCESSORIES = [
    "Camera hành trình",
    "Phim cách nhiệt",
    "Lót sàn",
    "Camera 360",
    "Khác",
]
import utils

def add_accessory():
    """1. Thêm phụ kiện mới"""
    print("\n--- THÊM PHỤ KIỆN MỚI ---")

    # Chọn tên phụ kiện từ danh sách hoặc nhập mới
    print("Chọn loại phụ kiện:")
    for idx, acc in enumerate(POPULAR_ACCESSORIES, 1):
        print(f"{idx}. {acc}")

    while True:
        choice = input(
            f"Chọn loại (1-{len(POPULAR_ACCESSORIES)}): "
        ).strip()
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(POPULAR_ACCESSORIES):
                if POPULAR_ACCESSORIES[choice_idx] == "Khác":
                    while True:
                        name = input("Nhập tên phụ kiện khác: ").strip()
                        if name:
                            break
                        print("Lỗi: Tên phụ kiện không được để trống!")
                else:
                    name = POPULAR_ACCESSORIES[choice_idx]
                break
            else:
                print(
                    f"Lỗi: Vui lòng chọn số từ 1 đến {len(POPULAR_ACCESSORIES)}!"
                )
        except ValueError:
            print("Lỗi: Lựa chọn phải là số nguyên! Vui lòng nhập lại.")

    # Nhập chi phí
    while True:
        try:
            cost = float(input("Nhập chi phí phụ kiện (VND): "))
            if cost < 0:
                print("Lỗi: Chi phí không thể âm! Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Lỗi: Chi phí phải là số! Vui lòng nhập lại.")

    # Lưu thông tin phụ kiện dạng List: [Tên phụ kiện, Chi phí].
    accessory_item = [name, cost]
    utils.accessories.append(accessory_item)


    # Lưu chi phí phụ kiện dạng List: [Mô tả, Nhóm chi phí, Số tiền]
    expense_item = [f"Lắp đặt {name}", "Phụ kiện", cost]
    utils.expenses.append(expense_item)

    print("\n=> Đã thêm phụ kiện thành công")


def view_accessory_list():
    """2. Xem danh sách phụ kiện"""
    print("\n\033[32m--- DANH SÁCH PHỤ KIỆN ---\033[0m")
    if not utils.accessories:
        print("Chưa có phụ kiện nào được ghi nhận.")
        return
    print(f"{'STT':<5} | {'Tên phụ kiện':<30} | {'Chi phí (VND)':<18}")
    print("-" * 58)

    for idx, item in enumerate(utils.accessories, 1):
        print(f"{idx:<5} | {item[0]:<30} | {item[1]:>16,.0f}")


def calculate_total_accessory_cost():
    """3. Tính tổng chi phí phụ kiện"""
    print("\n--- TỔNG CHI PHÍ PHỤ KIỆN ---")
    if not utils.accessories:
        print("Chưa có dữ liệu phụ kiện để tính toán.")
        return

    total = sum(item[1] for item in utils.accessories)
    print(f">>> TỔNG CHI PHÍ PHỤ KIỆN: {total:,.0f} VND <<<\n")


def delete_accessory():
    """4. Xóa phụ kiện"""
    if not hasattr(utils, "accessories") or not utils.accessories:
        print("\nChưa có phụ kiện nào để xóa.")
        return

    view_accessory_list()
    try:
        index = int(input("\nNhập STT phụ kiện muốn xóa: ")) - 1
        if 0 <= index < len(utils.accessories):
            removed = utils.accessories.pop(index)
            print(
                f"=> Đã xóa thành công phụ kiện: '{removed[0]}' ({removed[1]:,.0f} VND)"
            )
        else:
            print("Lỗi: STT không tồn tại!")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên!")