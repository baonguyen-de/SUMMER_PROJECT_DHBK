"""
==================================================
MODULE: issue.py
==================================================

Vai trò:
    Quản lý các vấn đề và cảnh báo của xe.

Chức năng chính:
    - Tạo vấn đề từ kết quả kiểm tra.
    - Xem các vấn đề đang tồn tại.
    - Hiển thị cảnh báo.
    - Theo dõi trạng thái vấn đề.

Trạng thái vấn đề:
    - OPEN.
    - IN_PROGRESS.
    - CLOSED.

Luồng xử lý:
    WARNING hoặc ERROR
        ↓
    OPEN
        ↓
    IN_PROGRESS
        ↓
    MAINTENANCE
        ↓
    CLOSED

Ghi chú:
    - Không cho phép đóng vấn đề tùy ý.
    - Vấn đề chỉ được CLOSED sau khi hoàn tất bảo dưỡng.
    - Dữ liệu được lưu trong utils.py.
"""
import os
import utils

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Hàm phụ trợ bẫy lỗi nhập số nguyên
def input_number(prompt, min_val=0, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if val < min_val or (max_val is not None and val > max_val):
                print(f"Lựa chọn không hợp lệ! Vui lòng nhập từ {min_val} đến {max_val}.")
                continue
            return val
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")

functions = [
    "Thêm vấn đề",
    "Xem các vấn đề đang tồn tại",
    "Đóng vấn đề",
    "Xóa vấn đề",
    "Thoát ra menu chính"
]

def create_issue(part_name, error_status):
    severity = "HIGH" if error_status == "ERROR" else "MEDIUM"
    utils.issue_parts.append(f"{part_name} bị lỗi")
    utils.issue_errors.append(severity)
    utils.issue_statuses.append("OPEN")

def add_issue():
    print("THÊM VẤN ĐỀ MỚI")
    desc = input("Mô tả vấn đề: ").strip()
    if not desc:
        print("Mô tả không được để trống!")
        input("\nNhấn ENTER để thử lại...")
        return

    muc_do = ["HIGH", "MEDIUM", "LOW"]
    print("\nMức độ nghiêm trọng:")
    for i, level in enumerate(muc_do, 1):
        print(f"{i}. {level}")

    choice_status = input_number("Nhập số tương ứng với tình trạng: ", min_val=1, max_val=len(muc_do))
    selected_status = muc_do[choice_status - 1]

    utils.issue_parts.append(desc)
    utils.issue_errors.append(selected_status)
    utils.issue_statuses.append("OPEN")
    
    print(f"\n✅ Đã thêm vấn đề: '{desc}' [Mức độ: {selected_status}] [Trạng thái: OPEN]")
    input("\nNhấn ENTER để tiếp tục")

def view_issue():
    print("CÁC VẤN ĐỀ ĐANG TỒN TẠI")
    if not utils.issue_parts:
        print("Hiện không có vấn đề nào")
    else:
        for i, (desc, severity, status) in enumerate(zip(utils.issue_parts, utils.issue_errors, utils.issue_statuses), 1):
            print(f"STT {i}:\n  Vấn đề   : {desc}\n  Mức độ   : {severity}\n  Trạng thái: {status}")
    
    input("\nNhấn ENTER để quay về")

def close_issue():
    print("ĐÓNG VẤN ĐỀ")
    open_issues = [i for i, status in enumerate(utils.issue_statuses) if status == "OPEN"]
    
    if not open_issues:
        print("Không có vấn đề nào để đóng")
        input("\nNhấn ENTER để tiếp tục")
        return

    for index, open_idx in enumerate(open_issues, 1):
        print(f"{index}. {utils.issue_parts[open_idx]}")

    choice = input_number("\nChọn STT vấn đề muốn đóng (0 để hủy): ", min_val=0, max_val=len(open_issues))
    if choice == 0:
        return

    target_i = open_issues[choice - 1]
    utils.issue_statuses[target_i] = "CLOSED"
    print("\n✅ Đã đóng vấn đề!")
    input("\nNhấn ENTER để tiếp tục")

def delete_issue():
    clear_screen()
    print("=== XÓA VẤN ĐỀ ===")

    if not utils.issue_parts:
        print("Không có vấn đề nào trong danh sách để xóa.")
        input("\nNhấn ENTER để quay về")
        return

    print("Danh sách tất cả các vấn đề:")
    for i, (p, e, s) in enumerate(zip(utils.issue_parts, utils.issue_errors, utils.issue_statuses), 1):
        print(f"{i}. {p} | {e} | {s}")

    choice = input_number("\nChọn STT vấn đề muốn xóa vĩnh viễn (0 để hủy): ", min_val=0, max_val=len(utils.issue_parts))
    if choice == 0:
        return

    idx = choice - 1
    removed_desc = utils.issue_parts[idx]
    
    # Xóa đồng thời trong cả 3 danh sách
    for lst in (utils.issue_parts, utils.issue_errors, utils.issue_statuses):
        lst.pop(idx)

    print(f"\n✅ Đã xóa thành công vấn đề: '{removed_desc}'")
    input("\nNhấn ENTER để tiếp tục")


    



