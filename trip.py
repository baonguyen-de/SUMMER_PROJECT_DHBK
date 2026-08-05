"""
==================================================
MODULE: trip.py
==================================================

Vai trò:
    Quản lý lịch sử các chuyến đi của xe.

Chức năng chính:
    - Thêm chuyến đi.
    - Xem lịch sử chuyến đi.
    - Xóa chuyến đi.
    - Tính tổng quãng đường.
    - Tìm chuyến đi dài nhất.

Thông tin chuyến đi:
    - Ngày.
    - Điểm đi.
    - Điểm đến.
    - Quãng đường.
    - Chế độ lái.

Ghi chú:
    - Dữ liệu chuyến đi được lưu trong utils.py.
    - Chỉ quản lý lịch sử chuyến đi.
    - Không xử lý chi phí hoặc bảo dưỡng.
"""

from datetime import datetime
import utils
from rich.table import Table
from rich.panel import Panel
from rich.console import Console

console = Console()

# Khởi tạo thuộc tính trips trong utils nếu chưa có
if not hasattr(utils, "trips"):
    utils.trips = []


def add_trip():
    console.print("\n[bold cyan]--- THÊM CHUYẾN ĐI MỚI ---[/bold cyan]")

    # 1. Nhập Ngày (DD/MM/YYYY)
    while True:
        date_str = input("Nhập ngày (DD/MM/YYYY): ").strip()
        try:
            formatted_date = datetime.strptime(date_str, "%d/%m/%Y").strftime("%d/%m/%Y")
            break
        except ValueError:
            console.print("[bold red]Lỗi: Định dạng ngày không hợp lệ! VD: 25/12/2026.[/bold red]")

    # 2. Nhập Điểm đi
    while True:
        origin = input("Nhập điểm đi: ").strip()
        if origin: 
            break
        console.print("[bold red]Lỗi: Điểm đi không được để trống![/bold red]")

    # 3. Nhập Điểm đến
    while True:
        destination = input("Nhập điểm đến: ").strip()
        if not destination:
            console.print("[bold red]Lỗi: Điểm đến không được để trống![/bold red]")
        elif destination.lower() == origin.lower():
            console.print("[bold red]Lỗi: Điểm đến không được trùng với điểm đi![/bold red]")
        else:
            break

    # 4. Nhập Quãng đường
    while True:
        try:
            distance = float(input("Nhập quãng đường (km): "))
            if distance > 0: 
                break
            console.print("[bold red]Lỗi: Quãng đường phải lớn hơn 0![/bold red]")
        except ValueError:
            console.print("[bold red]Lỗi: Quãng đường phải là số hợp lệ![/bold red]")

    # 5. Nhập Chế độ lái
    while True:
        mode = input("Nhập chế độ lái (VD: Eco, Sport, Auto): ").strip()
        if mode: 
            break
        console.print("[bold red]Lỗi: Chế độ lái không được để trống![/bold red]")

    # Lưu dữ liệu
    utils.trips.append([formatted_date, origin, destination, distance, mode])
    console.print("\n[bold green]✔ Đã thêm chuyến đi thành công![/bold green]")


def view_trip():
    if not utils.trips:
        console.print("\n[bold yellow] Chưa có lịch sử chuyến đi nào.[/bold yellow]")
        return False

    # Tạo bảng hiển thị danh sách các chuyến đi
    table = Table(border_style="white", header_style="bold cyan")
    table.add_column("STT", justify="center", style="white")
    table.add_column("Ngày", justify="center", style="white")
    table.add_column("Điểm đi", style="bold white", justify="center")
    table.add_column("Điểm đến", style="bold white", justify="center")
    table.add_column("Quãng đường", justify="center", style="white")
    table.add_column("Chế độ lái", justify="center", style="white")

    for i, trip in enumerate(utils.trips, start=1):
        date, origin, destination, distance, mode = trip
        table.add_row(
            str(i),
            date,
            origin,
            destination,
            f"{distance:,.1f} km",
            mode
        )

    # Đóng gói Bảng vào Panel
    panel = Panel(
        table,
        title="[bold yellow]🗺️ LỊCH SỬ CHUYẾN ĐI 🗺️[/bold yellow]",
        border_style="green",
        padding=(0, 1)
    )

    console.print(panel)
    return True


def show_summary():
    if not utils.trips:
        console.print("\n[bold yellow] Chưa có lịch sử chuyến đi nào.[/bold yellow]")
        return

    total_dist = sum(trip[3] for trip in utils.trips)
    longest = max(utils.trips, key=lambda trip: trip[3])

    # Tạo bảng thống kê nhỏ
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Tiêu chí", style="bold cyan", justify="right")
    table.add_column("Giá trị", style="bold white")

    table.add_row("Tổng số chuyến đi:", f"[bold white]{len(utils.trips)} chuyến[/bold white]")
    table.add_row("Tổng quãng đường:", f"[bold white]{total_dist:,.1f} km[/bold white]")
    table.add_row(
        "Chuyến dài nhất:", 
        f"[green]{longest[1]}[/green] ➔ [green]{longest[2]}[/green] ([bold white]{longest[3]:,.1f} km[/bold white])"
    )

    panel = Panel(
        table,
        title="[bold yellow]📊 THỐNG KÊ QUÃNG ĐƯỜNG 📊[/bold yellow]",
        border_style="green",
        padding=(1, 2)
    )

    console.print(panel)


def delete_trip():
    has_trips = view_trip()
    if not has_trips:
        return

    try:
        index = int(input("\nNhập STT muốn xóa (nhập 0 để hủy): "))
        if index == 0:
            console.print("[bold yellow]-> Đã hủy xóa.[/bold yellow]")
            return

        if 1 <= index <= len(utils.trips):
            removed = utils.trips.pop(index - 1)
            console.print(f"[bold green]✔ Đã xóa chuyến đi:[/bold green] [dim]{removed[1]} ➔ {removed[2]}[/dim]")
        else:
            console.print("[bold red]❌ Lỗi: Số thứ tự không nằm trong danh sách.[/bold red]")
    except ValueError:
        console.print("[bold red]❌ Lỗi: Vui lòng nhập số nguyên hợp lệ![/bold red]")

