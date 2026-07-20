"""
==================================================
MODULE: main.py
==================================================

Vai trò:
    File khởi chạy chính của chương trình.

Chức năng chính:
    - Khởi động chương trình.
    - Khởi tạo phiên quản lý xe.
    - Gọi menu chính.
    - Điều phối luồng hoạt động.
    - Xử lý chức năng thoát chương trình.

Ghi chú:
    - Không viết toàn bộ logic chức năng trong main.py.
    - Mỗi chức năng phải được xử lý trong module tương ứng.
    - main.py chỉ có nhiệm vụ điều phối chương trình.
"""
from utils import get_car_info
from menu import render_menu, menu_choice