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

def create_issue(part_name, error_status):
    utils.issue_parts.append(part_name)
    utils.issue_statuses.append("OPEN") 
    utils.issue_errors.append(error_status)

def view_issues():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== DANH SÁCH VẤN ĐỀ VÀ CẢNH BÁO CỦA XE ===")
    
    if not utils.issue_parts:
        print("Hiện tại không có vấn đề nào được ghi nhận.")
        input("\nNhấn ENTER để quay về...")
        return


    for i in range(len(utils.issue_parts)):
        part = utils.issue_parts[i]
        status = utils.issue_statuses[i]
        error = utils.issue_errors[i]
        i += 1
        print(f"Bộ phận: {part} | Lỗi: {error} | Trạng thái: {status}")
    
    print("\n[Lưu ý: Không thể tự ý đóng vấn đề ở đây. Vui lòng qua bảo dưỡng (maintenance) để xử lý.]")
    input("\nNhấn ENTER để quay về...")

def run():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- QUẢN LÝ VẤN ĐỀ (ISSUE) ---")
        print("1. Xem danh sách vấn đề")
        print("2. Quay về menu chính") 
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == '1':
            view_issues()
        elif choice == '2':
            break
        else:
            print("Lựa chọn không hợp lệ!")
            input("Nhấn ENTER để thử lại...")
