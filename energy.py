"""
==================================================
MODULE: energy.py
==================================================

Vai trò:
    Theo dõi và quản lý mức tiêu thụ năng lượng của xe.

Chức năng chính:
    - Ghi nhận thông tin sử dụng năng lượng.
    - Tính lượng năng lượng đã sử dụng.
    - Xem lịch sử sử dụng năng lượng.

Hỗ trợ:
    - Xe điện.
    - Xe sử dụng nhiên liệu.

Ghi chú:
    - Dữ liệu được lưu trong utils.py.
    - Chỉ sử dụng List.
    - Không sử dụng Dictionary hoặc Set.
"""

import utils
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Đảm bảo utils.energy luôn được khởi tạo
if not hasattr(utils, "energy"):
    utils.energy = []


def electric_energy():
    console.print("\n[bold cyan]⚡ GHI NHẬN NĂNG LƯỢNG XE ĐIỆN ⚡[/bold cyan]")

    # Nhập pin ban đầu
    while True:
        try:
            init_bat = float(input("Nhập Mức pin ban đầu (%): "))
            if 0 <= init_bat <= 100:
                break
            console.print("[bold red]Lỗi: Pin phải nằm trong khoảng từ 0 đến 100%![/bold red]")
        except ValueError:
            console.print("[bold red]Lỗi: Vui lòng nhập số hợp lệ![/bold red]")

    # Nhập pin còn lại
    while True:
        try:
            final_bat = float(input("Nhập Mức pin còn lại (%): "))
            if 0 <= final_bat <= init_bat:
                break
            console.print("[bold red]Lỗi: Pin còn lại phải từ 0% và không thể lớn hơn pin ban đầu![/bold red]")
        except ValueError:
            console.print("[bold red]Lỗi: Vui lòng nhập số hợp lệ![/bold red]")

    # Nhập quãng đường
    while True:
        try:
            distance = float(input("Nhập Quãng đường đã đi (km): "))
            if distance >= 0:
                break
            console.print("[bold red]Lỗi: Quãng đường không thể âm![/bold red]")
        except ValueError:
            console.print("[bold red]Lỗi: Vui lòng nhập số hợp lệ![/bold red]")

    used_bat = init_bat - final_bat
    record = ["electric", init_bat, final_bat, 0, distance]
    utils.energy.append(record)
    
    console.print(f"\n[bold green]✔ Đã ghi nhận thành công![/bold green] Pin đã sử dụng: [bold yellow]{used_bat:.1f}%[/bold yellow]")


def gas_energy():
    console.print("\n[bold cyan]⛽ GHI NHẬN NĂNG LƯỢNG XE XĂNG ⛽[/bold cyan]")

    # Nhập nhiên liệu đã dùng
    while True:
        try:
            fuel_used = float(input("Nhập Số lít nhiên liệu đã dùng (L): "))
            if fuel_used >= 0:
                break
            console.print("[bold red]Lỗi: Số lít nhiên liệu không thể âm![/bold red]")
        except ValueError:
            console.print("[bold red]Lỗi: Vui lòng nhập số hợp lệ![/bold red]")

    # Nhập quãng đường
    while True:
        try:
            distance = float(input("Nhập Quãng đường đã đi (km): "))
            if distance >= 0:
                break
            console.print("[bold red]Lỗi: Quãng đường không thể âm![/bold red]")
        except ValueError:
            console.print("[bold red]Lỗi: Vui lòng nhập số hợp lệ![/bold red]")

    consumption = (fuel_used / distance) * 100 if distance > 0 else 0
    record = ["gas", 0, 0, fuel_used, distance]
    utils.energy.append(record)
    
    console.print(f"\n[bold green]✔ Đã ghi nhận thành công![/bold green] Mức tiêu thụ: [bold yellow]{consumption:.2f} L/100km[/bold yellow]")


def view_energy_history():
    if not hasattr(utils, "energy") or not utils.energy:
        console.print("\n[bold yellow] Lịch sử tiêu thụ năng lượng trống.[/bold yellow]")
        return False

    # Định nghĩa Bảng hiển thị lịch sử
    table = Table(border_style="white", header_style="cyan")
    table.add_column("STT", justify="center", style="white")
    table.add_column("Loại xe", justify="center", style="white")
    table.add_column("Quãng đường", justify="center", style="white")
    table.add_column("Năng lượng đã dùng", justify="center", style="white")
    table.add_column("Mức tiêu thụ trung bình", justify="center", style="white")

    for i, rec in enumerate(utils.energy, start=1):
        loai_xe = rec[0]
        distance = rec[4]
        
        if loai_xe == "electric":
            tag_xe = "[cyan]⚡ Xe Điện[/cyan]"
            pin_da_dung = rec[1] - rec[2]
            nang_luong = f"{pin_da_dung:.1f}% Pin"
            tieu_thu = f"{(pin_da_dung / distance):.2f}% / km" if distance > 0 else "N/A"
        else: # gas
            tag_xe = "[yellow]⛽ Xe Xăng[/yellow]"
            fuel_used = rec[3]
            nang_luong = f"{fuel_used:.1f} L"
            tieu_thu = f"{((fuel_used / distance) * 100):.2f} L / 100km" if distance > 0 else "N/A"

        table.add_row(
            str(i),
            tag_xe,
            f"{distance:,.1f} km",
            nang_luong,
            tieu_thu
        )

    # Đóng gói Bảng vào Panel
    panel = Panel(
        table,
        title="[bold yellow]🔋 LỊCH SỬ TIÊU THỤ NĂNG LƯỢNG 🔋[/bold yellow]",
        border_style="green",
        padding=(0, 1)
    )

    console.print(panel)
    return True