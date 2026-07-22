"""
==================================================
MODULE: inspection.py
==================================================

Vai trò:
    Kiểm tra tình trạng các bộ phận chính của xe.

Các bộ phận kiểm tra:
    - Lốp xe.
    - Hệ thống phanh.
    - Đèn xe.
    - Điều hòa.
    - Pin hoặc hệ thống năng lượng.

Trạng thái:
    - OK.
    - WARNING.
    - ERROR.

Chức năng chính:
    - Thực hiện kiểm tra xe.
    - Cập nhật trạng thái bộ phận.
    - Xem kết quả kiểm tra.
    - Phát hiện bộ phận có vấn đề.

Luồng liên kết:
    INSPECTION
        ↓
    Phát hiện WARNING hoặc ERROR
        ↓
    ISSUE

Ghi chú:
    - Module này chỉ phát hiện vấn đề.
    - Không xử lý bảo dưỡng trực tiếp.
    - Không tự đóng vấn đề.
"""