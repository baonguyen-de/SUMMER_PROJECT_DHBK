"""
==================================================
MODULE: expense.py
==================================================

Vai trò:
    Quản lý các khoản chi phí liên quan đến xe.

Các nhóm chi phí:
    - Năng lượng.
    - Bảo dưỡng.
    - Bảo hiểm.
    - Phụ kiện.
    - Khác.

Chức năng chính:
    - Thêm chi phí.
    - Xem lịch sử chi phí.
    - Tính tổng chi phí.
    - Tính chi phí theo nhóm.
    - Xóa chi phí.

Ghi chú:
    - Dữ liệu được lưu trong utils.py.
    - Chi phí bảo dưỡng có thể được tạo từ maintenance.py.
    - Chi phí phụ kiện có thể được tạo từ accessory.py.
    - Không yêu cầu người dùng nhập lại chi phí đã được tự động ghi nhận.
"""
import utils
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

EXPENSE_CATEGORIES = ["Năng lượng", "Bảo dưỡng", "Bảo hiểm", "Phụ kiện", "Khác"]

# Đảm bảo utils.expenses luôn được khởi tạo
if not hasattr(utils, "expenses"):
    utils.expenses = []

# Hàm phụ trợ nhập số tổng quát
def input_num(prompt, is_int=False):
    while True:
        try:
            v = int(input(prompt)) if is_int else float(input(prompt))
            if v >= 0: 
                return v
            console.print("[bold red]Lỗi: Không được nhập số âm![/bold red]")
        except ValueError:
            console.print("[bold red]Lỗi: Phải nhập số hợp lệ![/bold red]")

# 1. Thêm chi phí
def add_expense():
    console.print("\n[bold cyan]--- THÊM CHI PHÍ MỚI ---[/bold cyan]")
    while True:
        desc = input("Nhập mô tả chi phí: ").strip()
        if desc: 
            break
        console.print("[bold red]Lỗi: Mô tả không được để trống![/bold red]")

    # Bảng danh mục nhóm chi phí
    cat_table = Table(show_header=False, box=None, padding=(0, 2))
    cat_table.add_column("STT", style="bold cyan", justify="center")
    cat_table.add_column("Tên nhóm", style="bold white", justify="center")
    for idx, cat in enumerate(EXPENSE_CATEGORIES, 1):
        cat_table.add_row(f"[{idx}]", cat)

    console.print(Panel(cat_table, title="[bold yellow]NHÓM CHI PHÍ[/bold yellow]", border_style="cyan"))

    cat_idx = int(input_num(f"Chọn nhóm (1-{len(EXPENSE_CATEGORIES)}): ", is_int=True)) - 1
    if not (0 <= cat_idx < len(EXPENSE_CATEGORIES)):
        console.print("[bold red]Lỗi: Lựa chọn không hợp lệ![/bold red]")
        return

    amount = input_num("Nhập số tiền (VND): ")

    utils.expenses.append([desc, EXPENSE_CATEGORIES[cat_idx], amount])
    console.print("\n[bold green]✔ Đã thêm chi phí thành công![/bold green]")

# 2. Xem lịch sử
def view_expense_history():
    expenses = getattr(utils, "expenses", [])
    if not expenses:
        console.print("\n[bold yellow] Chưa có khoản chi phí nào được ghi nhận.[/bold yellow]")
        return False

    table = Table(border_style="white", header_style="cyan")
    table.add_column("STT", justify="center", style="white")
    table.add_column("Mô tả", style="white", justify="center")
    table.add_column("Nhóm chi phí", justify="center", style="white")
    table.add_column("Số tiền", justify="center", style="white")

    for idx, item in enumerate(expenses, 1):
        table.add_row(
            str(idx),
            str(item[0]),
            str(item[1]),
            f"{item[2]:,.0f} VND"
        )

    panel = Panel(
        table,
        title="[bold yellow]💸 LỊCH SỬ CHI PHÍ 💸[/bold yellow]",
        border_style="green",
        padding=(0, 1)
    )
    console.print(panel)
    return True

# 3 & 4. Báo cáo tổng quan
def calculate_total_expenses():
    expenses = getattr(utils, "expenses", [])
    if not expenses:
        console.print("\n[bold yellow] Chưa có dữ liệu chi phí để tính toán.[/bold yellow]")
        return

    total = sum(item[2] for item in expenses)

    # Bảng chi tiết từng nhóm
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Nhóm", style="bold cyan", justify="center")
    table.add_column("Số tiền", style="white", justify="center")
    for cat in EXPENSE_CATEGORIES:
        cat_total = sum(item[2] for item in expenses if item[1] == cat)
        if cat_total > 0:
            table.add_row(
                f"{cat}:",
                f"[bold yellow]{cat_total:,.0f} VND[/bold yellow]"
                )
    table.add_row("", "")
    table.add_row("[bold white]TỔNG CHI PHÍ:[/bold white]", f"[bold red]{total:,.0f} VND[/bold red]")

    panel = Panel(
        table,
        title="[bold yellow]📊 BÁO CÁO TỔNG QUAN CHI PHÍ 📊[/bold yellow]",
        border_style="green",
        padding=(1, 2)
    )
    console.print(panel)

# 5. Xóa chi phí
def delete_expense():
    has_expenses = view_expense_history()
    if not has_expenses:
        return

    expenses = getattr(utils, "expenses", [])
    choice = int(input_num("\nNhập STT khoản chi phí muốn xóa (0 để hủy): ", is_int=True))
    
    if 0 < choice <= len(expenses):
        removed = expenses.pop(choice - 1)
        console.print(f"\n[bold green]✔ Đã xóa thành công:[/bold green] [dim]'{removed[0]}' ({removed[2]:,.0f} VND)[/dim]")
    elif choice != 0:
        console.print("[bold red]❌ Lỗi: STT không tồn tại![/bold red]")








