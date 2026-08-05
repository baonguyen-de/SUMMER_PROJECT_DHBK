"""
==================================================
MODULE: inspection.py
==================================================

Vai trò:
    Kiểm tra tình trạng các bộ phận chính của xe.

Các bộ phận kiểm tra:
    - Lốp xe.
    - Hệ thống phanh.
    - Đèn xe.
    - Điều hòa.
    - Pin hoặc hệ thống năng lượng.

Trạng thái:
    - OK.
    - WARNING.
    - ERROR.

Chức năng chính:
    - Thực hiện kiểm tra xe.
    - Cập nhật trạng thái bộ phận.
    - Xem kết quả kiểm tra.
    - Phát hiện bộ phận có vấn đề.

Luồng liên kết:
    INSPECTION
        ↓
    Phát hiện WARNING hoặc ERROR
        ↓
    ISSUE

Ghi chú:
    - Module này chỉ phát hiện vấn đề.
    - Không xử lý bảo dưỡng trực tiếp.
    - Không tự đóng vấn đề.
"""
import os
import utils
import issue  # Import module issue để tự động tạo vấn đề khi phát hiện lỗi
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Đảm bảo utils.inspection_results luôn được khởi tạo
if not hasattr(utils, "inspection_results"):
    utils.inspection_results = []

# Danh sách bộ phận xe
parts = [
    "Lốp xe",
    "Hệ thống phanh",
    "Đèn xe",
    "Điều hòa",
    "Pin hoặc hệ thống năng lượng"
]

# Danh sách trạng thái
statuses = ["OK", "WARNING", "ERROR"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def status():
    # Xóa dữ liệu kiểm tra cũ
    utils.inspection_results.clear()

    # Vòng lặp cho người dùng nhập tình trạng từng bộ phận
    for part_name in parts:
        clear_screen()
        
        # Tạo bảng chọn trạng thái cho bộ phận hiện tại
        menu_table = Table(show_header=False, box=None, padding=(0, 2))
        menu_table.add_column("STT", style="bold cyan")
        menu_table.add_column("Trạng thái", style="bold white")
        
        menu_table.add_row("[1]", "[bold green]OK[/bold green] (Bình thường)")
        menu_table.add_row("[2]", "[bold yellow]WARNING[/bold yellow] (Cảnh báo)")
        menu_table.add_row("[3]", "[bold red]ERROR[/bold red] (Lỗi nghiêm trọng)")

        console.print(Panel(
            menu_table,
            title=f"[bold yellow]🔍 KIỂM TRA: {part_name.upper()} 🔍[/bold yellow]",
            border_style="cyan",
            padding=(1, 2)
        ))

        # Vòng lặp kiểm tra nhập liệu hợp lệ
        while True:
            try:
                choice_status = int(input("\nNhập số tương ứng với tình trạng (1-3): "))
                if 1 <= choice_status <= len(statuses):
                    selected_status = statuses[choice_status - 1]
                    break
                else:
                    console.print("[bold red]Lỗi: Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 3.[/bold red]")
            except ValueError:
                console.print("[bold red]Lỗi: Vui lòng nhập một số nguyên hợp lệ![/bold red]")
        
        # Thêm trạng thái vào danh sách kết quả
        utils.inspection_results.append(selected_status)

    # Hiển thị bảng kết quả kiểm tra xe
    clear_screen()
    
    result_table = Table(border_style="white", header_style="cyan")
    result_table.add_column("STT", justify="center", style="white")
    result_table.add_column("Bộ phận", style="white", justify="center")
    result_table.add_column("Trạng thái", justify="center", style="white")

    has_error = False
    
    # Ghép từng bộ phận với kết quả tương ứng
    for idx, (part_name, st) in enumerate(zip(parts, utils.inspection_results), start=1):
        # Định dạng màu sắc & icon theo trạng thái
        if st == "OK":
            status_text = "[bold green]✔ OK[/bold green]"
        elif st == "WARNING":
            status_text = "[bold yellow]⚠️ WARNING[/bold yellow]"
            issue.create_issue(part_name, st)
        else:  # ERROR
            status_text = "[bold red]❌ ERROR[/bold red]"
            issue.create_issue(part_name, st)
            has_error = True

        result_table.add_row(str(idx), part_name, status_text)

    # Đóng gói Bảng kết quả vào Panel
    console.print(Panel(
        result_table,
        title="[bold yellow]📋 KẾT QUẢ KIỂM TRA TỔNG THỂ 📋[/bold yellow]",
        border_style="green",
        padding=(0, 1)
    ))

    # Hiển thị cảnh báo tổng thể bên dưới bảng
    if has_error:
        alert_panel = Panel(
            "[bold red]🚨 [CẢNH BÁO]: Phát hiện bộ phận ở trạng thái ERROR!\nHệ thống đã tự động ghi nhận Issue. Vui lòng kiểm tra và bảo dưỡng ngay.[/bold red]",
            border_style="red"
        )
    else:
        alert_panel = Panel(
            "[bold green]✔ [THÔNG BÁO]: Tất cả bộ phận đều hoạt động tốt hoặc ở mức chấp nhận được.[/bold green]",
            border_style="green"
        )
    
    console.print(alert_panel)
    input("\nNhấn ENTER để quay về menu chính...")



   

    



    


