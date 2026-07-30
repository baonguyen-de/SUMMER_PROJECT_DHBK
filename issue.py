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
import readchar
import utils

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

functions = [
    "Thêm vấn đề",
    "Xem các vấn đề đang tồn tại",
    "Đóng vấn đề",
    "Xóa vấn đề",
    "Thoát ra menu chính"
]

def render_menu(selected_index):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---VẤN ĐỀ VÀ CẢNH BÁO---")
    for i, function in enumerate(functions):
        if i == selected_index:
            print(f"> \033[32m{function}\033[0m")
        else:
            print(f"    {function}")

def menu_choice():
    current_index = 0
    while True:
        render_menu(current_index)
        key = readchar.readkey()
        if key == readchar.key.UP:
            current_index = (current_index -1) % len(functions)
        elif key == readchar.key.DOWN:
            current_index = (current_index + 1) % len(functions)
        elif key == readchar.key.ENTER:
            return current_index
def create_issue(part_name, error_status):
    description = (f"{part_name} bị lỗi")
    if error_status == "ERROR":
        severity = "HIGH"
    else:
        severity = "MEDIUM"
    utils.issue_parts.append(description)
    utils.issue_errors.append(severity)
    utils.issue_statuses.append("OPEN")

def add_issue():
    print("THÊM VẤN ĐỀ MỚI")
    desc = input("Mô tả vấn đề:").strip()
    if not desc:
        print("Mô tả không được để trống!")
        input("\nNhấn ENTER để thử lại...")
        return
    Muc_do = [
        "HIGH",
        "MEDIUM",
        "LOW"
    ]
    print("\nMức độ nghiêm trọng:")
    for i, level in enumerate(Muc_do, 1):
        print(f"{i}. {level}")

    # Vòng lặp kiểm tra nhập liệu hợp lệ
    while True:
        try:
            choice_status = int(input("Nhập số tương ứng với tình trạng: "))
            if 1 <= choice_status <= len(Muc_do):
                selected_status = Muc_do[choice_status - 1]
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 3.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")

    utils.issue_parts.append(desc)
    utils.issue_errors.append(selected_status)
    utils.issue_statuses.append("OPEN")
    
    print(f"\n✅ Đã thêm vấn đề: '{desc}' [Mức độ: {selected_status}] [Trạng thái: OPEN]")
    input("\nNhấn ENTER để tiếp tục")

def view_issue():
    print("\n\033[32m--- CÁC VẤN ĐỀ ĐANG TỒN TẠI ---\033[0m")
    if len(utils.issue_parts) == 0:
        print("Hiện không có vấn đề nào")
        input("Nhấn ENTER để tiếp tục")
        return
    for i in range(len(utils.issue_parts)):
        desc = utils.issue_parts[i]
        severity = utils.issue_errors[i]
        status = utils.issue_statuses[i]
        print(f"STT {i + 1}:")
        print(f"  Vấn đề   : {desc}")
        print(f"  Mức độ   : {severity}")
        print(f"  Trạng thái: {status}")
        input("Nhấn ENTER để quay về")

def close_issue():
    print("ĐÓNG VẤN ĐỀ")
    open_issues = []
    for i in range(len(utils.issue_statuses)):
        if utils.issue_statuses[i] == "OPEN":
            open_issues.append(i)
    if len(open_issues) == 0:
        print("Không có vấn đề nào để đóng")
        input("Nhấn ENTER để tiếp tục")
        return
    for index, open in enumerate(open_issues, 1):
        print(f"{index}. {utils.issue_parts[open]}")
    try:
        choice = int(input("\nChọn STT vấn đề muốn đóng (0 để hủy): "))
        if choice == 0:
            return
        if 1 <= choice <= len(open_issues):
            target_i = open_issues[choice - 1]
            utils.issue_statuses[target_i] = "CLOSED"
            print(f"\nĐã đóng vấn đề!")
        else:
            print("Lựa chọn không hợp lệ!")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")
    
    input("\nNhấn ENTER để tiếp tục")

def delete_issue():
    """Chức năng: Xóa vấn đề"""
    clear_screen()
    print("\033[32m--- XÓA VẤN ĐỀ ---\033[0m")

    if not utils.issue_parts:
        print("Không có vấn đề nào trong danh sách để xóa.")
        input("\nNhấn ENTER để quay về")
        return

    print("Danh sách tất cả các vấn đề:")
    for i in range(len(utils.issue_parts)):
        print(f"{i + 1}. {utils.issue_parts[i]} | {utils.issue_errors[i]} | {utils.issue_statuses[i]}")

    try:
        choice = int(input("\nChọn STT vấn đề muốn xóa vĩnh viễn (0 để hủy): "))
        if choice == 0:
            return
        if 1 <= choice <= len(utils.issue_parts):
            idx = choice - 1
            removed_desc = utils.issue_parts.pop(idx)
            utils.issue_errors.pop(idx)
            utils.issue_statuses.pop(idx)
            print(f"\nĐã xóa thành công vấn đề: '{removed_desc}'")
        else:
            print("Lựa chọn không hợp lệ!")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

    input("\nNhấn ENTER để tiếp tục")

def run():
    while True:
        selected_option = menu_choice()
        os.system('cls' if os.name == 'nt' else 'clear')
        if selected_option == 0:
            add_issue()
        elif selected_option == 1:
            view_issue()
        elif selected_option == 2:
            close_issue()
        elif selected_option == 3:
            delete_issue()
        elif selected_option == 4:
            break
    



