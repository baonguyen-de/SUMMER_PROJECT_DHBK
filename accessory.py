"""
==================================================
MODULE: accessory.py
==================================================

Vai trò:
    Quản lý các phụ kiện của xe.

Chức năng chính:
    - Thêm phụ kiện.
    - Xem danh sách phụ kiện.
    - Xóa phụ kiện.
    - Tính tổng chi phí phụ kiện.

Dữ liệu liên quan:
    - Tên phụ kiện.
    - Chi phí phụ kiện.

Ghi chú:
    - Dữ liệu được lưu trong utils.py.
    - Chi phí phụ kiện cần được ghi nhận vào hệ thống chi phí.
    - Không xử lý thông tin xe hoặc bảo dưỡng trong module này.
"""

POPULAR_ACCESSORIES = [
    "Camera hành trình",
    "Phim cách nhiệt",
    "Lót sàn",
    "Camera 360",
    "Khác",
]
import os
import utils
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Danh sách phụ kiện phổ biến
POPULAR_ACCESSORIES = [
    "Thảm lót sàn",
    "Fim cách nhiệt",
    "Camera hành trình",
    "Cảm biến áp suất lốp",
    "Bọc vô năng",
    "Khác"
]

# Đảm bảo các thuộc tính lưu trữ trong utils luôn sẵn sàng
if not hasattr(utils, "accessories"):
    utils.accessories = []
if not hasattr(utils, "expenses"):
    utils.expenses = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. Thêm phụ kiện mới
def add_accessory():
    clear_screen()
    console.print("[bold cyan]--- THÊM PHỤ KIỆN MỚI ---[/bold cyan]\n")

    # Bảng hiển thị danh sách phụ kiện gợi ý
    menu_table = Table(show_header=False, box=None, padding=(0, 2))
    menu_table.add_column("STT", style="bold cyan", justify="center")
    menu_table.add_column("Tên phụ kiện", style="white", justify="center")

    for idx, acc in enumerate(POPULAR_ACCESSORIES, 1):
        menu_table.add_row(f"[{idx}]", acc)

    console.print(Panel(
        menu_table,
        title="[bold yellow]DANH SÁCH PHỤ KIỆN GỢI Ý[/bold yellow]",
        border_style="cyan",
        padding=(0, 1)
    ))

    while True:
        choice = input(f"\nChọn loại (1-{len(POPULAR_ACCESSORIES)}): ").strip()
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(POPULAR_ACCESSORIES):
                if POPULAR_ACCESSORIES[choice_idx] == "Khác":
                    while True:
                        name = input("Nhập tên phụ kiện khác: ").strip()
                        if name:
                            break
                        console.print("[bold red]Lỗi: Tên phụ kiện không được để trống![/bold red]")
                else:
                    name = POPULAR_ACCESSORIES[choice_idx]
                break
            else:
                console.print(f"[bold red]Lỗi: Vui lòng chọn số từ 1 đến {len(POPULAR_ACCESSORIES)}![/bold red]")
        except ValueError:
            console.print("[bold red]Lỗi: Lựa chọn phải là số nguyên! Vui lòng nhập lại.[/bold red]")

    # Nhập chi phí
    while True:
        try:
            cost = float(input("Nhập chi phí phụ kiện (VND): "))
            if cost < 0:
                console.print("[bold red]Lỗi: Chi phí không thể âm! Vui lòng nhập lại.[/bold red]")
                continue
            break
        except ValueError:
            console.print("[bold red]Lỗi: Chi phí phải là số! Vui lòng nhập lại.[/bold red]")

    # Lưu thông tin phụ kiện
    utils.accessories.append([name, cost])

    # Đồng bộ lưu vào danh sách chi phí chung
    utils.expenses.append([f"Lắp đặt {name}", "Phụ kiện", cost])

    console.print(f"\n[bold green]✔ Đã thêm phụ kiện thành công![/bold green] '{name}' ({cost:,.0f} VND)")
    input("\nNhấn ENTER để tiếp tục...")

# 2. Xem danh sách phụ kiện
def view_accessory_list():
    if not hasattr(utils, "accessories") or not utils.accessories:
        console.print("\n[bold yellow] Chưa có phụ kiện nào được ghi nhận.[/bold yellow]")
        return False

    table = Table(border_style="white", header_style="cyan")
    table.add_column("STT", justify="center", style="white")
    table.add_column("Tên phụ kiện", style="white", justify="center")
    table.add_column("Chi phí", justify="center", style="white")

    for idx, item in enumerate(utils.accessories, 1):
        table.add_row(
            str(idx),
            str(item[0]),
            f"{item[1]:,.0f} VND"
        )

    panel = Panel(
        table,
        title="[bold yellow]🛞 DANH SÁCH PHỤ KIỆN ĐÃ LẮP ĐẶT 🛞[/bold yellow]",
        border_style="green",
        padding=(0, 1)
    )
    console.print(panel)
    return True

# 3. Tính tổng chi phí phụ kiện
def calculate_total_accessory_cost():
    clear_screen()
    if not hasattr(utils, "accessories") or not utils.accessories:
        console.print("[bold yellow]⚠️ Chưa có dữ liệu phụ kiện để tính toán.[/bold yellow]")
        input("\nNhấn ENTER để tiếp tục...")
        return

    total = sum(item[1] for item in utils.accessories)

    info_table = Table(show_header=False, box=None, padding=(0, 2))
    info_table.add_column("Tiêu chí", style="white", justify="center")
    info_table.add_column("Giá trị", style="white")
    info_table.add_row("Số lượng phụ kiện:", f"[bold white]{len(utils.accessories)} items[/bold white]")
    info_table.add_row("Tổng chi phí lắp đặt:", f"[bold red]{total:,.0f} VND[/bold red]")

    console.print(Panel(
        info_table,
        title="[bold yellow]💰 TỔNG CHI PHÍ PHỤ KIỆN 💰[/bold yellow]",
        border_style="green",
        padding=(1, 2)
    ))
    input("\nNhấn ENTER để tiếp tục...")

# 4. Xóa phụ kiện
def delete_accessory():
    clear_screen()
    has_items = view_accessory_list()
    if not has_items:
        input("\nNhấn ENTER để tiếp tục...")
        return

    try:
        choice = int(input("\nNhập STT phụ kiện muốn xóa (0 để hủy): "))
        if choice == 0:
            return
        
        index = choice - 1
        if 0 <= index < len(utils.accessories):
            removed = utils.accessories.pop(index)
            
            # Đồng bộ xóa khỏi danh sách chi phí chung (Expense)
            if hasattr(utils, "expenses"):
                utils.expenses = [
                    e for e in utils.expenses 
                    if not (e[0] == f"Lắp đặt {removed[0]}" and e[2] == removed[1])
                ]
            
            console.print(f"\n[bold green]✔ Đã xóa thành công phụ kiện:[/bold green] [dim]'{removed[0]}' ({removed[1]:,.0f} VND)[/dim]")
        else:
            console.print("[bold red]❌ Lỗi: STT không tồn tại![/bold red]")
    except ValueError:
        console.print("[bold red]❌ Lỗi: Vui lòng nhập một số nguyên![/bold red]")
    
    input("\nNhấn ENTER để tiếp tục...")