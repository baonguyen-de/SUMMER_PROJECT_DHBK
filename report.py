"""
==================================================
MODULE: report.py
==================================================

Vai trò:
    Tổng hợp và hiển thị báo cáo phiên sử dụng xe.

Nội dung báo cáo:
    - Thông tin xe.
    - Tổng số chuyến đi.
    - Tổng quãng đường.
    - Năng lượng sử dụng.
    - Lịch sử bảo dưỡng.
    - Tổng chi phí.
    - Các vấn đề đang tồn tại.
    - Số lượng phụ kiện.

Chức năng chính:
    - Tổng hợp dữ liệu.
    - Tính toán các số liệu cần thiết.
    - Hiển thị báo cáo.

Ghi chú:
    - Chỉ đọc và tổng hợp dữ liệu.
    - Không thêm dữ liệu.
    - Không chỉnh sửa dữ liệu trong utils.py.
"""
import accessory
import car
import energy
import expense
import trip
import utils

def print_issue():
    print("\n\033[32m--- CÁC VẤN ĐỀ ĐANG TỒN TẠI ---\033[0m")
    if len(utils.issue_parts) == 0:
        print("Hiện không có vấn đề nào")
    for i in range(len(utils.issue_parts)):
        desc = utils.issue_parts[i]
        severity = utils.issue_errors[i]
        status = utils.issue_statuses[i]
        print(f"STT {i + 1}:")
        print(f"  Vấn đề   : {desc}")
        print(f"  Mức độ   : {severity}")
        print(f"  Trạng thái: {status}")

def print_maintenance():
    print("\n\033[32m--- LỊCH SỬ BẢO DƯỠNG XE ---\033[0m")
    
    if not utils.maint_items:
        print("Chưa có lịch sử bảo dưỡng nào.")
    
    for i in range(len(utils.maint_items)):
        print(f"Hạng mục   : {utils.maint_items[i]}")
        print(f"Ngày       : {utils.maint_dates[i]}")
        print(f"Số kilomet : {utils.maint_kms[i]:.0f} km")
        print(f"Chi phí    : {utils.maint_costs[i]:.0f} VND")
    
def report():
    if len(utils.car_info) == 0:
        print("\033[31mVui lòng nhập thông tin xe!\033[0m")
        input()
        return
    else:
        total_distance = 0.0
        initial_car_km = 0.0
        for km in utils.trips:
            total_distance += km[3] 
        utils.car_info[3] = total_distance + initial_car_km
        car.display_car_info()
        trip.view_trip()
        trip.total_distance()
        energy.view_energy_history()
        print_maintenance()
        expense.calculate_total_expenses()
        print_issue()
        accessory.view_accessory_list()
        input("\nNhấn ENTER để tiếp tục")
        return
    
    
        
