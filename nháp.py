import os
import utils

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_issue(part_name, error_status):
    """
    Hàm này được gọi tự động từ module inspection hoặc gọi thủ công
    """
    description = f"{part_name} bị lỗi"
    
    # Quy đổi mức độ nghiêm trọng từ trạng thái kiểm tra
    severity = "HIGH" if error_status == "ERROR" else "MEDIUM"
    
    # Kiểm tra xem vấn đề này đã tồn tại ở trạng thái OPEN/IN_PROGRESS chưa để tránh trùng lặp
    for i in range(len(utils.issue_parts)):
        if utils.issue_parts[i] == description and utils.issue_statuses[i] != "CLOSED":
            return  # Đã có issue chưa đóng rồi thì không tạo mới nữa

    utils.issue_parts.append(description)
    utils.issue_errors.append(severity)     # Lưu mức độ nghiêm trọng (HIGH/MEDIUM)
    utils.issue_statuses.append("OPEN")       # Trạng thái ban đầu luôn là OPEN

def add_issue_manual():
    """Chức năng: Thêm vấn đề thủ công"""
    clear_screen()
    print("=== THÊM VẤN ĐỀ MỚI ===")
    
    desc = input("Nhập mô tả vấn đề (ví dụ: Đèn xe bị lỗi): ").strip()
    if not desc:
        print("Mô tả không được để trống!")
        input("\nNhấn ENTER để thử lại...")
        return

    print("\nChọn mức độ nghiêm trọng:")
    print("1. HIGH")
    print("2. MEDIUM")
    print("3. LOW")
    
    choice = input("Nhập lựa chọn (1-3): ").strip()
    severity_map = {"1": "HIGH", "2": "MEDIUM", "3": "LOW"}
    severity = severity_map.get(choice, "MEDIUM")

    utils.issue_parts.append(desc)
    utils.issue_errors.append(severity)
    utils.issue_statuses.append("OPEN")

    print(f"\n✅ Đã thêm vấn đề: '{desc}' [Mức độ: {severity}] [Trạng thái: OPEN]")
    input("\nNhấn ENTER để tiếp tục...")

def view_issues():
    """Chức năng: Xem các vấn đề đang tồn tại"""
    clear_screen()
    print("⚠️  CÁC VẤN ĐỀ ĐANG TỒN TẠI\n")
    print("=" * 45)

    if not utils.issue_parts:
        print("Hiện tại không có vấn đề nào được ghi nhận.")
        input("\nNhấn ENTER để quay về...")
        return

    for i in range(len(utils.issue_parts)):
        desc = utils.issue_parts[i]
        severity = utils.issue_errors[i]
        status = utils.issue_statuses[i]
        
        print(f"STT {i + 1}:")
        print(f"  Vấn đề   : {desc}")
        print(f"  Mức độ   : {severity}")
        print(f"  Trạng thái: {status}")
        print("-" * 45)

    input("\nNhấn ENTER để quay về...")

def close_issue():
    """Chức năng: Đóng vấn đề"""
    clear_screen()
    print("=== ĐÓNG VẤN ĐỀ ===")

    # Lọc ra danh sách các vấn đề chưa đóng
    open_indices = [i for i in range(len(utils.issue_parts)) if utils.issue_statuses[i] != "CLOSED"]

    if not open_indices:
        print("Không có vấn đề nào đang mở để đóng.")
        input("\nNhấn ENTER để quay về...")
        return

    print("Danh sách các vấn đề đang mở:")
    for idx, original_i in enumerate(open_indices, 1):
        print(f"{idx}. {utils.issue_parts[original_i]} [{utils.issue_statuses[original_i]}]")

    try:
        choice = int(input("\nChọn STT vấn đề muốn đóng (0 để hủy): "))
        if choice == 0:
            return
        if 1 <= choice <= len(open_indices):
            target_i = open_indices[choice - 1]
            utils.issue_statuses[target_i] = "CLOSED"
            print(f"\n✅ Đã chuyển trạng thái vấn đề '{utils.issue_parts[target_i]}' sang CLOSED!")
        else:
            print("Lựa chọn không hợp lệ!")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

    input("\nNhấn ENTER để tiếp tục...")



def run():
    while True:
        clear_screen()
        print("--- QUẢN LÝ VẤN ĐỀ VÀ CẢNH BÁO ---")
        print("1. Xem các vấn đề đang tồn tại")
        print("2. Thêm vấn đề mới")
        print("3. Đóng vấn đề")
        print("4. Xóa vấn đề")
        print("5. Quay về menu chính")
        
        choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
        if choice == '1':
            view_issues()
        elif choice == '2':
            add_issue_manual()
        elif choice == '3':
            close_issue()
        elif choice == '4':
            delete_issue()
        elif choice == '5':
            break
        else:
            print("Lựa chọn không hợp lệ!")
            input("Nhấn ENTER để thử lại...")