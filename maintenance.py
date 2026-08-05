"""
==================================================
MODULE: maintenance.py
==================================================

Vai trò:
    Quản lý quá trình bảo dưỡng và xử lý vấn đề của xe.

Chức năng chính:
    - Xem các vấn đề cần xử lý.
    - Bắt đầu xử lý vấn đề.
    - Thêm lịch sử bảo dưỡng.
    - Ghi nhận chi phí bảo dưỡng.
    - Hoàn tất bảo dưỡng.
    - Đóng vấn đề sau khi bảo dưỡng hoàn tất.

Luồng xử lý:
    ISSUE
        ↓
    MAINTENANCE
        ↓
    EXPENSE
        ↓
    ISSUE CLOSED

Ghi chú quan trọng:
    - Không được đóng vấn đề nếu chưa hoàn tất bảo dưỡng.
    - Khi bảo dưỡng phát sinh chi phí, chi phí phải được ghi nhận.
    - Sau khi bảo dưỡng hoàn tất, vấn đề phải được cập nhật trạng thái.
    - Dữ liệu được lưu trong utils.py.
"""
import os
import utils
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

maintenance_option = [
    "Thêm lịch bảo dưỡng",
    "Xem danh sách bảo dưỡng",
    "Xóa lịch bảo dưỡng",
    "Kiểm tra cảnh báo bảo dưỡng",
    "Quay lại"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Hàm nhập số dùng chung ngắn gọn
def input_num(prompt, is_int=False):
    while True:
        try:
            v = int(input(prompt)) if is_int else float(input(prompt))
            if v >= 0: 
                return v
            console.print("[bold red]Lỗi: Không được nhập số âm![/bold red]")
        except ValueError:
            console.print("[bold red]Lỗi: Phải nhập số hợp lệ![/bold red]")

# 1. Bảo dưỡng vấn đề
def add_maintenance():
    clear_screen()
    console.print("[bold cyan]=== THỰC HIỆN BẢO DƯỠNG ===[/bold cyan]\n")
    
    open_idx = [i for i, s in enumerate(utils.issue_statuses) if s == "OPEN"]
    if not open_idx:
        console.print("[bold yellow] Không có vấn đề OPEN cần bảo dưỡng![/bold yellow]")
        input("\nNhấn ENTER...")
        return

    # Tạo bảng danh sách các sự cố OPEN
    table = Table(border_style="white", header_style="cyan")
    table.add_column("STT", justify="center", style="white")
    table.add_column("Bộ phận", style="bold white", justify="center")
    table.add_column("Mức độ lỗi", justify="center", style="bold red")

    for idx, i in enumerate(open_idx, 1):
        table.add_row(
            str(idx),
            str(utils.issue_parts[i]),
            str(utils.issue_errors[i])
        )

    panel = Panel(
        table,
        title="[bold yellow]🛠️ DANH SÁCH VẤN ĐỀ CẦN BẢO DƯỠNG 🛠️[/bold yellow]",
        border_style="green",
        padding=(0, 1)
    )
    console.print(panel)

    choice = int(input_num("\nChọn STT bảo dưỡng (0 để hủy): ", is_int=True))
    if choice == 0 or choice > len(open_idx): 
        return

    target_idx = open_idx[choice - 1]
    name = utils.issue_parts[target_idx]

    date = input("Nhập ngày (dd/mm/yyyy): ").strip() or "N/A"
    km = input_num("Nhập số km: ")
    cost = input_num("Nhập chi phí (VND): ")

    # Lưu dữ liệu vào 4 danh sách song song
    utils.maint_items.append(f"Bảo dưỡng: {name}")
    utils.maint_dates.append(date)
    utils.maint_kms.append(km)
    utils.maint_costs.append(cost)

    # Đồng bộ Expense & đóng Issue
    if not hasattr(utils, "expenses"): 
        utils.expenses = []
    utils.expenses.append([f"Bảo dưỡng: {name}", "Bảo dưỡng", cost])
    utils.issue_statuses[target_idx] = "CLOSED"

    console.print(f"\n[bold green]✔ Đã bảo dưỡng & đóng vấn đề '{name}' thành công![/bold green]")
    input("\nNhấn ENTER để tiếp tục...")

# 2. Xem lịch sử
def view_maintenance():
    clear_screen()
    if not utils.maint_items:
        console.print("[bold yellow] Chưa có lịch sử bảo dưỡng.[/bold yellow]")
    else:
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

        panel = Panel(
            table,
            title="[bold yellow]🔧 LỊCH SỬ BẢO DƯỠNG 🔧[/bold yellow]",
            border_style="green",
            padding=(0, 1)
        )
        console.print(panel)

    input("\nNhấn ENTER để quay về...")

# 3. Xóa lịch sử
def delete_maintenance():
    clear_screen()
    if not utils.maint_items:
        console.print("[bold yellow] Chưa có lịch sử để xóa.[/bold yellow]")
        input("\nNhấn ENTER...")
        return

    # Tái sử dụng bảng danh sách để chọn xóa cho trực quan
    table = Table(border_style="white", header_style="cyan")
    table.add_column("STT", justify="center", style="white")
    table.add_column("Hạng mục", style="white", justify="center")
    table.add_column("Ngày", justify="center", style="white")

    for i in range(len(utils.maint_items)):
        table.add_row(str(i + 1), str(utils.maint_items[i]), str(utils.maint_dates[i]))

    panel = Panel(table, title="[bold yellow]🗑️ XÓA LỊCH SỬ BẢO DƯỠNG 🗑️[/bold yellow]", border_style="red")
    console.print(panel)

    choice = int(input_num("\nChọn STT xóa (0 để hủy): ", is_int=True))
    if 0 < choice <= len(utils.maint_items):
        idx = choice - 1
        item_name, cost_to_remove = utils.maint_items[idx], utils.maint_costs[idx]

        # Xóa đồng thời trên cả 4 danh sách song song
        for lst in (utils.maint_items, utils.maint_dates, utils.maint_kms, utils.maint_costs):
            lst.pop(idx)

        # Đồng bộ xóa Expense
        if hasattr(utils, "expenses"):
            utils.expenses = [e for e in utils.expenses if not (e[0] == item_name and e[2] == cost_to_remove)]
        
        console.print("\n[bold green]✔ Đã xóa lịch sử thành công![/bold green]")
    else:
        console.print("\n[bold yellow]-> Đã hủy xóa.[/bold yellow]")
    input("\nNhấn ENTER để tiếp tục...")

# 4. Kiểm tra cảnh báo
def check_maintenance_warning():
    clear_screen()
    if not utils.maint_kms:
        console.print("[bold yellow] Chưa có dữ liệu bảo dưỡng.[/bold yellow]")
        input("\nNhấn ENTER...")
        return

    last_km = max(utils.maint_kms)
    
    # Bảng hiển thị thông số kiểm tra
    info_table = Table(show_header=False, box=None, padding=(0, 2))
    info_table.add_column("Tiêu chí", style="bold cyan", justify="center")
    info_table.add_column("Giá trị", style="bold white",justify="center")
    info_table.add_row("Km bảo dưỡng gần nhất:", f"[bold yellow]{last_km:,.0f} km[/bold yellow]")

    console.print(Panel(info_table, title="[bold yellow]🔍 KIỂM TRA CẢNH BÁO 🔍[/bold yellow]", border_style="cyan"))

    current_km = input_num("\nNhập số km hiện tại: ")
    diff = current_km - last_km

    # Hiển thị kết quả bằng Panel riêng biệt
    result_text = f"Quãng đường đã đi thêm: [bold yellow]{diff:,.0f} km[/bold yellow]\n\n"
    if diff >= 5000:
        result_text += "[bold red]⚠️ NÊN BẢO DƯỠNG XE NGAY (Đã vượt mốc 5,000 km)![/bold red]"
        border = "red"
    else:
        result_text += "[bold green]✔ Xe hoạt động an toàn (Chưa đến mốc 5,000 km).[/bold green]"
        border = "green"

    console.print("\n", Panel(result_text, title="[bold white]KẾT QUẢ KIỂM TRA[/bold white]", border_style=border))
    input("\nNhấn ENTER để tiếp tục...")


  