"""
==================================================
MODULE: car.py
==================================================

Vai trò:
    Quản lý thông tin cơ bản của một chiếc xe.

Chức năng chính:
    - Xem thông tin xe.
    - Cập nhật thông tin xe.
    - Cập nhật số kilomet hiện tại.

Thông tin xe:
    - Tên xe.
    - Loại xe.
    - Biển số.
    - Số kilomet hiện tại.
    - Năm sản xuất.

Ghi chú:
    - Project chỉ quản lý một chiếc xe duy nhất.
    - Dữ liệu xe được lưu trong utils.py.
    - Không xử lý chuyến đi, bảo dưỡng hoặc chi phí.
"""
import utils
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console() # Khởi tạo máy in màu

# Đảm bảo utils.car_info luôn được khởi tạo
if not hasattr(utils, "car_info"):
    utils.car_info = []

# --- HÀM HỖ TRỢ NHẬP DỮ LIỆU ---
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        console.print("[bold red]Cảnh báo: Thông tin này không được để trống![/bold red]")

def car_km():
    while True:
        try:
            val = float(input("Nhập số km: "))
            if val >= 0:
                return val
            console.print("[bold red]Cảnh báo: Số km không được là số âm.[/bold red]")
        except ValueError:
            console.print("[bold red]Cảnh báo: Số km không hợp lệ. Vui lòng nhập lại.[/bold red]")

def car_year():
    while True:
        try:
            val = int(input("Nhập năm sản xuất: "))
            if 1886 <= val <= 2026:
                return val
            console.print("[bold red]Cảnh báo: Năm sản xuất phải từ 1886 đến 2026.[/bold red]")
        except ValueError:
            console.print("[bold red]Cảnh báo: Năm sản xuất không hợp lệ. Vui lòng nhập lại.[/bold red]")

# --- HÀM XỬ LÝ CHÍNH (ĐÃ LÀM ĐẸP GIAO DIỆN) ---
def display_car_info():
    if not utils.car_info or len(utils.car_info) < 5:
        console.print("[bold yellow]⚠️ Chưa có thông tin xe trong hệ thống.[/bold yellow]")
        return False

    # 1. Tạo bảng 2 cột chứa chi tiết thông tin
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Thuộc tính", style="bold cyan", justify="right")
    table.add_column("Giá trị", style="bold white")

    # 2. Thêm từng dòng dữ liệu vào bảng
    table.add_row("Tên xe:", str(utils.car_info[0]))
    table.add_row("Loại xe:", str(utils.car_info[1]))
    table.add_row("Biển số:", f"{utils.car_info[2]}")
    table.add_row("Số kilomet:", f"{utils.car_info[3]:,.1f} km")
    table.add_row("Năm sản xuất:", str(utils.car_info[4]))

    # 3. Đóng gói bảng vào Panel
    panel = Panel(
        table,
        title="[bold yellow]🚘 THÔNG TÍN XE HIỆN TẠI 🚘[/bold yellow]",
        border_style="green",
        padding=(1, 2)
    )

    console.print(panel)
    return True

def get_car_info():
    console.print("\n[bold cyan]--- NHẬP THÔNG TIN XE MỚI ---[/bold cyan]")
    car_name = get_non_empty_input("Nhập tên xe: ")
    car_type = get_non_empty_input("Nhập loại xe: ")
    car_number = get_non_empty_input("Nhập biển số: ")
    car_km_val = car_km()
    car_year_val = car_year()

    # Ghi đè toàn bộ danh sách car_info bằng dữ liệu mới
    utils.car_info = [car_name, car_type, car_number, car_km_val, car_year_val]
    console.print("\n[bold green]✔ Đã cập nhật thông tin xe thành công![/bold green]")

def run():
    if not utils.car_info:
        get_car_info()
        input("\nNhấn Enter để tiếp tục...")
    else:
        display_car_info()
        console.print("\n[bold green][1][/bold green] Nhập lại thông tin xe mới")
        console.print("[bold red][0][/bold red] Bấm Enter để quay lại")
        
        choice = input("\nLựa chọn của bạn: ").strip()
        if choice == "1":
            get_car_info()
            input("\nNhấn Enter để tiếp tục...")
            




