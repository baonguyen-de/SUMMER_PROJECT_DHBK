"""
==================================================
MODULE: issue.py
==================================================

Vai trò:
    Quản lý các vấn đề và cảnh báo của xe.

Chức năng chính:
    - Tạo vấn đề từ kết quả kiểm tra.
    - Xem các vấn đề đang tồn tại.
    - Hiển thị cảnh báo.
    - Theo dõi trạng thái vấn đề.

Trạng thái vấn đề:
    - OPEN.
    - IN_PROGRESS.
    - CLOSED.

Luồng xử lý:
    WARNING hoặc ERROR
        ↓
    OPEN
        ↓
    IN_PROGRESS
        ↓
    MAINTENANCE
        ↓
    CLOSED

Ghi chú:
    - Không cho phép đóng vấn đề tùy ý.
    - Vấn đề chỉ được CLOSED sau khi hoàn tất bảo dưỡng.
    - Dữ liệu được lưu trong utils.py.
"""
import os
import utils
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Đảm bảo các danh sách song song trong utils luôn tồn tại
for attr in ["issue_parts", "issue_errors", "issue_statuses"]:
    if not hasattr(utils, attr):
        setattr(utils, attr, [])

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Hàm phụ trợ bẫy lỗi nhập số nguyên
def input_number(prompt, min_val=0, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if val < min_val or (max_val is not None and val > max_val):
                console.print(f"[bold red]Lỗi: Vui lòng nhập từ {min_val} đến {max_val}![/bold red]")
                continue
            return val
        except ValueError:
            console.print("[bold red]Lỗi: Vui lòng nhập một số nguyên hợp lệ![/bold red]")

functions = [
    "Thêm vấn đề",
    "Xem các vấn đề đang tồn tại",
    "Đóng vấn đề",
    "Xóa vấn đề",
    "Thoát ra menu chính"
]

def create_issue(part_name, error_status):
    """Được gọi tự động từ module inspection khi phát hiện WARNING / ERROR"""
    severity = "HIGH" if error_status == "ERROR" else "MEDIUM"
    utils.issue_parts.append(f"{part_name} bị lỗi")
    utils.issue_errors.append(severity)
    utils.issue_statuses.append("OPEN")

def add_issue():
    clear_screen()
    console.print("[bold cyan]--- THÊM VẤN ĐỀ MỚI ---[/bold cyan]\n")
    
    desc = input("Nhập mô tả vấn đề: ").strip()
    if not desc:
        console.print("[bold red]Lỗi: Mô tả không được để trống![/bold red]")
        input("\nNhấn ENTER để thử lại...")
        return

    muc_do = ["HIGH", "MEDIUM", "LOW"]
    
    # Bảng chọn mức độ nghiêm trọng
    level_table = Table(show_header=False, box=None, padding=(0, 2))
    level_table.add_column("STT", style="bold cyan")
    level_table.add_column("Mức độ", style="bold white")
    level_table.add_row("[1]", "[bold red]HIGH[/bold red]")
    level_table.add_row("[2]", "[bold yellow]MEDIUM[/bold yellow]")
    level_table.add_row("[3]", "[bold green]LOW[/bold green]")

    console.print(Panel(
        level_table,
        title="[bold yellow]MỨC ĐỘ NGHIÊM TRỌNG[/bold yellow]",
        border_style="cyan",
        padding=(0, 1)
    ))

    choice_status = input_number("\nNhập số tương ứng với mức độ (1-3): ", min_val=1, max_val=len(muc_do))
    selected_status = muc_do[choice_status - 1]

    utils.issue_parts.append(desc)
    utils.issue_errors.append(selected_status)
    utils.issue_statuses.append("OPEN")
    
    console.print(f"\n[bold green]✔ Đã thêm vấn đề thành công![/bold green] [dim]'{desc}'[/dim]")
    input("\nNhấn ENTER để tiếp tục...")

def view_issue():
    clear_screen()
    if not utils.issue_parts:
        console.print("[bold yellow]⚠️ Hiện không có vấn đề nào trong hệ thống.[/bold yellow]")
    else:
        table = Table(border_style="white", header_style="cyan")
        table.add_column("STT", justify="center", style="dim white")
        table.add_column("Mô tả vấn đề", style="bold white")
        table.add_column("Mức độ", justify="center")
        table.add_column("Trạng thái", justify="center")

        for idx, (desc, severity, status) in enumerate(zip(utils.issue_parts, utils.issue_errors, utils.issue_statuses), 1):
            # Định dạng màu Mức độ
            if severity == "HIGH":
                sev_text = "[bold red]HIGH[/bold red]"
            elif severity == "MEDIUM":
                sev_text = "[bold yellow]MEDIUM[/bold yellow]"
            else:
                sev_text = "[bold green]LOW[/bold green]"

            # Định dạng màu Trạng thái
            st_text = "[bold red]OPEN[/bold red]" if status == "OPEN" else "[bold green]CLOSED[/bold green]"

            table.add_row(str(idx), str(desc), sev_text, st_text)

        panel = Panel(
            table,
            title="[bold yellow]⚠️ DANH SÁCH VẤN ĐỀ TỒN TẠI ⚠️[/bold yellow]",
            border_style="green",
            padding=(0, 1)
        )
        console.print(panel)
    
    input("\nNhấn ENTER để quay về...")

def close_issue():
    clear_screen()
    open_issues = [i for i, status in enumerate(utils.issue_statuses) if status == "OPEN"]
    
    if not open_issues:
        console.print("[bold yellow]⚠️ Không có vấn đề OPEN nào để đóng.[/bold yellow]")
        input("\nNhấn ENTER để tiếp tục...")
        return

    # Bảng danh sách vấn đề đang OPEN
    table = Table(border_style="white", header_style="cyan")
    table.add_column("STT", justify="center", style="white")
    table.add_column("Vấn đề cần đóng", style="white", justify="center")
    table.add_column("Mức độ", justify="center", style="white")

    for index, open_idx in enumerate(open_issues, 1):
        table.add_row(
            str(index),
            str(utils.issue_parts[open_idx]),
            str(utils.issue_errors[open_idx])
        )

    console.print(Panel(
        table,
        title="[bold yellow]🔒 ĐÓNG VẤN ĐỀ (OPEN ➔ CLOSED) 🔒[/bold yellow]",
        border_style="cyan",
        padding=(0, 1)
    ))

    choice = input_number("\nChọn STT vấn đề muốn đóng (0 để hủy): ", min_val=0, max_val=len(open_issues))
    if choice == 0:
        return

    target_i = open_issues[choice - 1]
    utils.issue_statuses[target_i] = "CLOSED"
    console.print(f"\n[bold green]✔ Đã đóng vấn đề thành công![/bold green]")
    input("\nNhấn ENTER để tiếp tục...")

def delete_issue():
    clear_screen()

    if not utils.issue_parts:
        console.print("[bold yellow] Không có vấn đề nào trong danh sách để xóa.[/bold yellow]")
        input("\nNhấn ENTER để quay về...")
        return

    table = Table(border_style="white", header_style="cyan")
    table.add_column("STT", justify="center", style="white")
    table.add_column("Mô tả vấn đề", style="white", justify="center")
    table.add_column("Trạng thái", justify="center", style="white")

    for i, (p, e, s) in enumerate(zip(utils.issue_parts, utils.issue_errors, utils.issue_statuses), 1):
        table.add_row(str(i), str(p), str(s))

    console.print(Panel(
        table,
        title="[bold red]🗑️ XÓA VẤN ĐỀ VĨNH VIỄN 🗑️[/bold red]",
        border_style="red",
        padding=(0, 1)
    ))

    choice = input_number("\nChọn STT muốn xóa (0 để hủy): ", min_val=0, max_val=len(utils.issue_parts))
    if choice == 0:
        return

    idx = choice - 1
    removed_desc = utils.issue_parts[idx]
    
    # Xóa đồng thời trong cả 3 danh sách song song
    for lst in (utils.issue_parts, utils.issue_errors, utils.issue_statuses):
        lst.pop(idx)

    console.print(f"\n[bold green]✔ Đã xóa thành công vấn đề:[/bold green] [dim]'{removed_desc}'[/dim]")
    input("\nNhấn ENTER để tiếp tục...")


    



