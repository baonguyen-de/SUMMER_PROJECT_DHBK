"""
==================================================
MODULE: menu.py
==================================================

Vai trò:
    Quản lý giao diện menu và điều hướng chương trình.

Chức năng chính:
    - Hiển thị menu.
    - Điều hướng bằng phím mũi tên lên.
    - Điều hướng bằng phím mũi tên xuống.
    - Xác nhận lựa chọn bằng phím Enter.
    - Gọi module tương ứng.

Ghi chú:
    - menu.py chỉ xử lý điều hướng.
    - Không xử lý logic quản lý xe.
    - Không trực tiếp quản lý dữ liệu.
"""
import os
import readchar
from rich.console import Console  
from rich.panel import Panel      
from rich.text import Text        
console = Console()            
import car, inspection, issue, trip, expense, accessory, energy, maintenance, report

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Hàm chung điều khiển menu bằng bàn phím 
def run_menu(title, options):
    current = 0
    while True:
        clear_screen()
        
        # 1. Tạo danh sách các tùy chọn
        menu_text = Text()
        for i, opt in enumerate(options):
            if i == current:
                # Dòng đang chọn: Nền màu xanh lá, chữ trắng đậm
                menu_text.append(f" ▶ {opt}\n", style="bold white on green")
            else:
                # Các dòng còn lại: Chữ màu xám
                menu_text.append(f"   {opt}\n", style="gray")

        # 2. Tạo khung đóng gói menu (Panel)
        panel = Panel(
            menu_text,
            title=f"[bold yellow]🔧 {title} 🚗[/bold yellow]",
            subtitle="[green]Dùng phím ↑ / ↓ để di chuyển | ENTER để chọn[/green]",
            border_style= "cyan",
        )
        
        # 3. In khung menu ra màn hình
        console.print(panel)

        # 4. Nhận phím bấm từ bàn phím
        key = readchar.readkey()
        if key in (readchar.key.UP, 'w', 'W'):
            current = (current - 1) % len(options)
        elif key in (readchar.key.DOWN, 's', 'S'):
            current = (current + 1) % len(options)
        elif key in (readchar.key.ENTER, '\r', '\n'):
            return current

# 1. Menu Bảo dưỡng
def maintenance_run():
    while True:
        choice = run_menu("QUẢN LÝ BẢO DƯỠNG", maintenance.maintenance_option)
        clear_screen()
        if choice == 0: maintenance.add_maintenance()
        elif choice == 1: maintenance.view_maintenance()
        elif choice == 2: maintenance.delete_maintenance()
        elif choice == 3: maintenance.check_maintenance_warning()
        elif choice == 4: break

# 2. Menu Issue
def issue_run():
    while True:
        choice = run_menu("VẤN ĐỀ VÀ CẢNH BÁO", issue.functions)
        clear_screen()
        if choice == 0: issue.add_issue()
        elif choice == 1: issue.view_issue()
        elif choice == 2: issue.close_issue()
        elif choice == 3: issue.delete_issue()
        elif choice == 4: break

# 3. Menu Trip
def trip_menu():
    options = ["Xem danh sách chuyến đi", "Thêm chuyến đi mới", "Xóa chuyến đi", "Xem tổng quãng đường & dài nhất", "Quay lại"]
    while True:
        choice = run_menu("QUẢN LÝ CHUYẾN ĐI", options)
        clear_screen()
        if choice == 0: trip.view_trip()
        elif choice == 1: trip.add_trip()
        elif choice == 2: trip.delete_trip()
        elif choice == 3: trip.show_summary()
        elif choice == 4: break
        input("\nẤn Enter để tiếp tục...")

# 4. Menu Energy
def energy_menu():
    options = ["Xem lịch sử tiêu thụ", "Ghi nhận XE ĐIỆN", "Ghi nhận XE XĂNG", "Quay lại"]
    while True:
        choice = run_menu("QUẢN LÝ TIÊU THỤ NĂNG LƯỢNG", options)
        clear_screen()
        if choice == 0: energy.view_energy_history()
        elif choice == 1: energy.electric_energy()
        elif choice == 2: energy.gas_energy()
        elif choice == 3: break
        input("\nẤn Enter để tiếp tục...")

# 5. Menu Expense
def expense_menu():
    options = ["Xem lịch sử chi phí", "Thêm chi phí mới", "Tính tổng & theo nhóm", "Xóa chi phí", "Quay lại"]
    while True:
        choice = run_menu("QUẢN LÝ CHI PHÍ", options)
        clear_screen()
        if choice == 0: expense.view_expense_history()
        elif choice == 1: expense.add_expense()
        elif choice == 2: expense.calculate_total_expenses()
        elif choice == 3: expense.delete_expense()
        elif choice == 4: break
        input("\nẤn Enter để tiếp tục...")

# 6. Menu Accessory
def accessory_menu():
    options = ["Xem danh sách phụ kiện", "Thêm phụ kiện mới", "Tính tổng chi phí", "Xóa phụ kiện", "Quay lại"]
    while True:
        choice = run_menu("QUẢN LÝ PHỤ KIỆN", options)
        clear_screen()
        if choice == 0: accessory.view_accessory_list()
        elif choice == 1: accessory.add_accessory()
        elif choice == 2: accessory.calculate_total_accessory_cost()
        elif choice == 3: accessory.delete_accessory()
        elif choice == 4: break

# 7. Menu chính
main_options = [
    "Quản lý thông tin xe", "Quản lý chuyến đi", "Quản lý năng lượng",
    "Quản lý bảo dưỡng", "Quản lý chi phí", "Kiểm tra tình trạng xe",
    "Vấn đề và cảnh báo", "Quản lý phụ kiện", "Báo cáo phiên sử dụng", "Thoát"
]

while True:
    choice = run_menu("CARCARE MANAGER", main_options)
    clear_screen()
    if choice == 0: car.run()
    elif choice == 1: trip_menu()
    elif choice == 2: energy_menu()
    elif choice == 3: maintenance_run()
    elif choice == 4: expense_menu()
    elif choice == 5: inspection.status()
    elif choice == 6: issue_run()
    elif choice == 7: accessory_menu()
    elif choice == 8: report.report()
    elif choice == 9: break




        


   
    
  

    
    
    