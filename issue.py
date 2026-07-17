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