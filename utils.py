"""
==================================================
MODULE: utils.py
==================================================

Vai trò:
    Lưu trữ dữ liệu dùng chung của toàn bộ chương trình.

Dữ liệu có thể bao gồm:
    - Thông tin xe.
    - Danh sách chuyến đi.
    - Dữ liệu năng lượng.
    - Lịch sử bảo dưỡng.
    - Danh sách chi phí.
    - Kết quả kiểm tra xe.
    - Các vấn đề của xe.
    - Danh sách phụ kiện.

Ghi chú quan trọng:
    - Đây là nơi lưu trữ dữ liệu dùng chung.
    - Chỉ sử dụng List và các kiểu dữ liệu cơ bản.
    - Không sử dụng Dictionary.
    - Không sử dụng Set.
    - Không xử lý logic nghiệp vụ.
    - Không viết menu trong file này.

Định hướng nâng cấp:
    - Phiên bản đầu tiên: Lưu dữ liệu trong bộ nhớ bằng List.
    - Phiên bản sau: Nâng cấp sang SQLite.
"""
car_info = []
def get_car_info():
    global car_info
    CARNAME = input("Nhập tên xe: ")
    CARTYPE = input("Nhập loại xe: ")
    CARNUMBER = input("Nhập biển số: ")
    CARKM = float(input("Nhập số kilomet hiện tại: "))
    CARYEAR = int(input("Nhập năm sản xuất: "))
    car_info = [CARNAME, CARTYPE, CARNUMBER, CARKM, CARYEAR]
    return car_info
get_car_info()



    
