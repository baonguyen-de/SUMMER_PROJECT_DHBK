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