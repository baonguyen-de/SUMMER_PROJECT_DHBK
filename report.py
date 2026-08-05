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
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def print_issue():
    if not hasattr(utils, "issue_parts") or not utils.issue_parts:
        console.print("\n[bold yellow] Hiện không có vấn đề nào trong hệ thống.[/bold yellow]")
        return

    table = Table(border_style="white", header_style="cyan")
    table.add_column("STT", justify="center", style="white")
    table.add_column("Mô tả vấn đề", style="white", justify="center")
    table.add_column("Mức độ", justify="center", style="white")
    table.add_column("Trạng thái", justify="center", style="white")

    for i in range(len(utils.issue_parts)):
        desc = utils.issue_parts[i]
        severity = utils.issue_errors[i]
        status = utils.issue_statuses[i]

        # Định dạng màu Mức độ
        if severity == "HIGH":
            sev_text = "[bold red]HIGH[/bold red]"
        elif severity == "MEDIUM":
            sev_text = "[bold yellow]MEDIUM[/bold yellow]"
        else:
            sev_text = "[bold green]LOW[/bold green]"

        # Định dạng màu Trạng thái
        st_text = "[bold red]OPEN[/bold red]" if status == "OPEN" else "[bold green]CLOSED[/bold green]"

        table.add_row(str(i + 1), str(desc), sev_text, st_text)

    console.print(Panel(
        table,
        title="[bold yellow]⚠️ CÁC VẤN ĐỀ ĐANG TỒN TẠI ⚠️[/bold yellow]",
        border_style="green",
        padding=(0, 1)
    ))

def print_maintenance():
    if not hasattr(utils, "maint_items") or not utils.maint_items:
        console.print("\n[bold yellow] Chưa có lịch sử bảo dưỡng nào.[/bold yellow]")
        return

    table = Table(border_style="white", header_style="cyan")
    table.add_column("STT", justify="center", style="white")
    table.add_column("Hạng mục", style="white", justify="center")
    table.add_column("Ngày", justify="center", style="white")
    table.add_column("Số km", justify="right", style="white")
    table.add_column("Chi phí", justify="right", style="white")

    for i in range(len(utils.maint_items)):
        table.add_row(
            str(i + 1),
            str(utils.maint_items[i]),
            str(utils.maint_dates[i]),
            f"{utils.maint_kms[i]:,.0f} km",
            f"{utils.maint_costs[i]:,.0f} VND"
        )

    console.print(Panel(
        table,
        title="[bold yellow]🔧 LỊCH SỬ BẢO DƯỠNG XE 🔧[/bold yellow]",
        border_style="green",
        padding=(0, 1)
    ))

def report():
    if not hasattr(utils, "car_info") or len(utils.car_info) == 0:
        console.print("\n[bold red]🚨 Lỗi: Vui lòng nhập thông tin xe trước khi xem báo cáo![/bold red]")
        input("\nNhấn ENTER để quay lại...")
        return

    # Tiêu đề báo cáo tổng quan
    console.print(Panel(
        "[bold white]TỔNG HỢP BÁO CÁO HOẠT ĐỘNG VÀ BẢO TRÌ XE[/bold white]",
        title="[bold yellow]📊 BAO CAO PHIEN SU DUNG 📊[/bold yellow]",
        border_style="magenta",
        padding=(0, 2)
    ))

    # Cập nhật tổng ODO dựa trên danh sách chuyến đi
    total_distance = sum(km[3] for km in getattr(utils, "trips", []))
    
    # Kiểm tra ODO ban đầu nếu có, mặc định là 0.0
    initial_car_km = utils.car_info[3] if len(utils.car_info) > 3 else 0.0
    utils.car_info[3] = total_distance + initial_car_km

    # Gọi các hàm báo cáo thành phần từ các module (đã giao diện Rich)
    car.display_car_info()
    trip.view_trip()
    trip.show_summary()
    energy.view_energy_history()
    print_maintenance()
    expense.calculate_total_expenses()
    print_issue()
    accessory.view_accessory_list()

    input("\nNhấn ENTER để tiếp tục...")
    
    
        
