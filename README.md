# CARCARE MANAGER

## Hệ thống quản lý và kiểm soát ô tô cá nhân bằng Python

---

# 1. Tổng quan đề tài

## 1.1. Tên đề tài

**CarCare Manager – Hệ thống quản lý và kiểm soát ô tô cá nhân**

Tên tiếng Anh:

> **CarCare Manager: A Python-Based Personal Vehicle Management and Monitoring System**

---

## 1.2. Giới thiệu

Trong quá trình sử dụng ô tô, chủ xe cần theo dõi nhiều thông tin khác nhau như tình trạng phương tiện, lịch sử hành trình, mức tiêu thụ năng lượng, lịch bảo dưỡng, chi phí vận hành và các vấn đề phát sinh trong quá trình sử dụng.

Tuy nhiên, các thông tin này thường được ghi nhớ hoặc lưu trữ một cách rời rạc, gây khó khăn cho việc theo dõi và tổng hợp dữ liệu về chiếc xe.

**CarCare Manager** là một hệ thống quản lý và kiểm soát ô tô cá nhân được xây dựng bằng ngôn ngữ lập trình Python.

Khác với các hệ thống quản lý nhiều phương tiện, project tập trung vào việc **quản lý duy nhất một chiếc ô tô**. Hệ thống mô phỏng quá trình người dùng theo dõi toàn bộ vòng đời sử dụng của chiếc xe thông qua các dữ liệu do người dùng nhập vào.

Hệ thống cho phép người dùng:

* Quản lý thông tin chiếc xe.
* Theo dõi lịch sử hành trình.
* Theo dõi mức tiêu thụ năng lượng.
* Quản lý lịch sử bảo dưỡng.
* Theo dõi chi phí sử dụng xe.
* Kiểm tra tình trạng các bộ phận của xe.
* Theo dõi các vấn đề và cảnh báo của xe.
* Quản lý các phụ kiện và trang bị trên xe.
* Xem báo cáo tổng hợp về tình trạng và quá trình sử dụng xe.

Người dùng tương tác với hệ thống thông qua **giao diện dòng lệnh CLI**.

Để tăng tính trực quan và tạo cảm giác giống một hệ thống quản lý thực tế, menu của chương trình được điều khiển bằng:

* Phím mũi tên lên `↑`.
* Phím mũi tên xuống `↓`.
* Phím `Enter`.

---

# 2. Mục tiêu của project

## 2.1. Mục tiêu chính

Xây dựng một chương trình Python có khả năng quản lý và theo dõi toàn bộ thông tin liên quan đến **một chiếc ô tô cá nhân**.

## 2.2. Mục tiêu học tập

Project giúp sinh viên áp dụng các kiến thức Python cơ bản:

* Biến và kiểu dữ liệu.
* List.
* String.
* Number.
* Câu lệnh điều kiện.
* Vòng lặp.
* Hàm.
* Đọc và ghi file JSON.
* Xử lý dữ liệu nhập từ người dùng.
* Chia chương trình thành nhiều module.
* Làm việc nhóm và quản lý source code bằng GitHub.

---

# 3. Các giới hạn kỹ thuật của project

Để đảm bảo phù hợp với sinh viên mới học Python, project tuân thủ các giới hạn sau:

## Được sử dụng

* `list`
* `str`
* `int`
* `float`
* `if / elif / else`
* `for`
* `while`
* `def`
* `input()`
* `print()`
* File JSON
* Module Python cơ bản

## Không sử dụng

* OOP.
* Class.
* Dictionary.
* Set.
* Database.
* API.
* Machine Learning.
* AI.
* Thuật toán nâng cao.
* Framework.
* Web application.

> Toàn bộ dữ liệu trong chương trình được biểu diễn và xử lý bằng **List**.

---

# 4. Ý tưởng tổng thể của hệ thống

CarCare Manager chỉ quản lý **một chiếc xe duy nhất**.

Ví dụ:

> VinFast VF MPV7

Hệ thống hoạt động theo mô hình:

```text
Người dùng
    ↓
Menu điều khiển ↑ ↓ Enter
    ↓
Chọn module
    ↓
Nhập dữ liệu
    ↓
Xử lý bằng Python
    ↓
Lưu dữ liệu vào JSON
    ↓
Hiển thị thông tin / cảnh báo / báo cáo
```

---

# 5. Cấu trúc dữ liệu chính

Do project không sử dụng Dictionary, thông tin xe được lưu bằng **List**.

## 5.1. Thông tin xe

```python
car = [
    "VF MPV7",
    "Electric",
    "71A-XXXXX",
    1250,
    2026
]
```

Quy ước dữ liệu:

```text
car[0] → Tên xe
car[1] → Loại xe
car[2] → Biển số
car[3] → Số km hiện tại
car[4] → Năm sản xuất
```

Để tránh việc thành viên trong nhóm quên vị trí dữ liệu, có thể ghi chú:

```python
CAR_NAME = 0
CAR_TYPE = 1
CAR_LICENSE = 2
CAR_KM = 3
CAR_YEAR = 4
```

Ví dụ:

```python
print(car[CAR_NAME])
```

Cách này vẫn chỉ sử dụng kiến thức Python cơ bản.

---

# 6. Cấu trúc thư mục GitHub

```text
CarCare-Manager/
│
├── main.py
│
├── menu.py
├── car.py
├── trip.py
├── energy.py
├── maintenance.py
├── expense.py
├── inspection.py
├── issue.py
├── accessory.py
├── report.py
│
├── file_handler.py
│
├── data/
│   ├── car.json
│   ├── trips.json
│   ├── energy.json
│   ├── maintenance.json
│   ├── expenses.json
│   ├── inspections.json
│   ├── issues.json
│   └── accessories.json
│
└── README.md
```

---

# 7. MODULE MENU CONTROL

## 7.1. Mục đích

Đây là module điều khiển giao diện chính của hệ thống.

Người dùng không cần nhập số lựa chọn.

Ví dụ:

```text
╔══════════════════════════════════╗
║        CARCARE MANAGER            ║
╠══════════════════════════════════╣
║ > Thông tin xe                    ║
║   Quản lý hành trình              ║
║   Theo dõi năng lượng             ║
║   Bảo dưỡng                       ║
║   Chi phí                         ║
║   Kiểm tra xe                     ║
║   Vấn đề và cảnh báo              ║
║   Phụ kiện                        ║
║   Báo cáo                         ║
║   Thoát                            ║
╚══════════════════════════════════╝
```

Người dùng:

```text
↑ ↓ → Di chuyển
Enter → Chọn
```

## 7.2. Hướng code

```python
def show_menu(options):
    selected = 0

    while True:
        for i in range(len(options)):
            if i == selected:
                print("> " + options[i])
            else:
                print("  " + options[i])

        key = get_key()

        if key == "UP":
            selected = selected - 1

        elif key == "DOWN":
            selected = selected + 1

        elif key == "ENTER":
            return selected

        if selected < 0:
            selected = len(options) - 1

        if selected >= len(options):
            selected = 0
```

Với Linux, nhóm có thể dùng `curses`.

---

# 8. MODULE 1 – VEHICLE INFORMATION

## Quản lý thông tin xe

Đây là module quản lý thông tin cơ bản của chiếc xe.

## Chức năng

```text
Thông tin xe
│
├── Xem thông tin xe
├── Cập nhật số km
├── Cập nhật thông tin xe
└── Xóa dữ liệu xe
```

## Dữ liệu

```python
car = [
    "VF MPV7",
    "Electric",
    "71A-XXXXX",
    1250,
    2026
]
```

## Ví dụ hiển thị

```text
========== VEHICLE INFORMATION ==========

Tên xe: VF MPV7
Loại xe: Electric
Biển số: 71A-XXXXX
Số km hiện tại: 1250 km
Năm sản xuất: 2026
```

## Hướng code

```python
def show_car(car):
    print("Ten xe:", car[0])
    print("Loai xe:", car[1])
    print("Bien so:", car[2])
    print("So km:", car[3])
    print("Nam san xuat:", car[4])
```

---

# 9. MODULE 2 – TRIP MANAGEMENT

## Quản lý hành trình

Module theo dõi lịch sử các chuyến đi của xe.

## Chức năng

```text
Hành trình
│
├── Thêm hành trình
├── Xem lịch sử
├── Tính tổng quãng đường
├── Tìm chuyến đi xa nhất
└── Xóa hành trình
```

## Dữ liệu

```python
trips = [
    ["17/07/2026", "Ben Tre", "TPHCM", 120, "Normal"],
    ["18/07/2026", "TPHCM", "Cu Chi", 80, "Eco"]
]
```

Quy ước:

```text
trip[0] → Ngày
trip[1] → Điểm đi
trip[2] → Điểm đến
trip[3] → Quãng đường
trip[4] → Chế độ lái
```

## Tính tổng quãng đường

```python
total = 0

for trip in trips:
    total = total + trip[3]
```

## Tìm chuyến xa nhất

```python
max_distance = 0
max_trip = []

for trip in trips:
    if trip[3] > max_distance:
        max_distance = trip[3]
        max_trip = trip
```

---

# 10. MODULE 3 – ENERGY MONITORING

## Theo dõi năng lượng

Module theo dõi mức tiêu thụ năng lượng của xe.

Project có thể hỗ trợ hai loại phương tiện:

```text
Electric
Gasoline
```

## Trường hợp xe điện

Dữ liệu:

```python
energy = [
    [80, 55, 120],
    [90, 70, 100]
]
```

Quy ước:

```text
energy[0] → Một lần sử dụng
energy[0][0] → Pin đầu chuyến
energy[0][1] → Pin cuối chuyến
energy[0][2] → Quãng đường
```

## Tính pin tiêu thụ

```python
used = start_battery - end_battery
```

## Ví dụ

```text
Pin đầu chuyến: 80%
Pin cuối chuyến: 55%
Quãng đường: 120 km

Đã sử dụng: 25% pin
```

## Trường hợp xe xăng

```python
consumption = fuel / distance * 100
```

Ví dụ:

```text
30 L
400 km

Mức tiêu thụ: 7.5 L/100km
```

---

# 11. MODULE 4 – MAINTENANCE MANAGEMENT

## Quản lý bảo dưỡng

Module theo dõi lịch sử bảo dưỡng của xe.

## Chức năng

```text
Bảo dưỡng
│
├── Thêm lịch sử bảo dưỡng
├── Xem lịch sử
├── Xóa lịch sử
└── Kiểm tra cảnh báo bảo dưỡng
```

## Dữ liệu

```python
maintenance = [
    ["Kiem tra lop", "17/07/2026", 1000, 500000],
    ["Kiem tra phanh", "20/07/2026", 5000, 300000]
]
```

Quy ước:

```text
maintenance[0] → Tên hạng mục
maintenance[1] → Ngày
maintenance[2] → Số km
maintenance[3] → Chi phí
```

## Cảnh báo

```python
distance = current_km - last_maintenance_km

if distance >= 10000:
    print("CAN BAO DUONG")
```

---

# 12. MODULE 5 – EXPENSE MANAGEMENT

## Quản lý chi phí

Module theo dõi các khoản chi phí liên quan đến xe.

## Các loại chi phí

```text
Energy
Maintenance
Insurance
Accessory
Other
```

## Dữ liệu

```python
expenses = [
    ["Sac xe", "Energy", 120000],
    ["Bao duong", "Maintenance", 500000],
    ["Bao hiem", "Insurance", 8000000]
]
```

## Chức năng

```text
Chi phí
│
├── Thêm chi phí
├── Xem lịch sử
├── Tính tổng chi phí
├── Tính chi phí theo loại
└── Xóa chi phí
```

## Tính tổng

```python
total = 0

for expense in expenses:
    total = total + expense[2]
```

## Tính chi phí trung bình trên mỗi km

```python
average = total_expense / total_distance
```

---

# 13. MODULE 6 – VEHICLE INSPECTION

## Kiểm tra tình trạng xe

Module mô phỏng việc kiểm tra tình trạng các bộ phận của xe.

## Các hạng mục

```python
items = [
    "Lop xe",
    "Phanh",
    "Den",
    "Dieu hoa",
    "Pin"
]
```

## Trạng thái

```python
status = [
    "OK",
    "OK",
    "ERROR",
    "OK",
    "OK"
]
```

Hai List có cùng vị trí:

```text
items[0] ↔ status[0]
Lốp xe   ↔ OK
```

## Kiểm tra lỗi

```python
for i in range(len(items)):
    if status[i] == "ERROR":
        print("Phat hien loi:", items[i])
```

## Ví dụ

```text
========== VEHICLE INSPECTION ==========

Lop xe       [OK]
Phanh        [OK]
Den          [ERROR]
Dieu hoa     [OK]
Pin          [OK]

⚠️ Phát hiện vấn đề ở Đèn xe
```

---

# 14. MODULE 7 – ISSUE & ALERT MANAGEMENT

## Quản lý vấn đề và cảnh báo

Đây là module mới giúp project có tính "kiểm soát xe" rõ hơn.

## Ý tưởng

Người dùng có thể ghi nhận các vấn đề phát sinh.

Ví dụ:

```text
Đèn xe bị lỗi
Điều hòa hoạt động không tốt
Lốp xe có dấu hiệu bất thường
```

## Dữ liệu

```python
issues = [
    ["Den xe bi loi", "High", "Open"],
    ["Dieu hoa hoi yeu", "Low", "Closed"]
]
```

Quy ước:

```text
issue[0] → Nội dung
issue[1] → Mức độ
issue[2] → Trạng thái
```

## Chức năng

```text
Vấn đề
│
├── Thêm vấn đề
├── Xem vấn đề
├── Đóng vấn đề
└── Xóa vấn đề
```

## Ví dụ cảnh báo

```text
⚠️ ACTIVE VEHICLE ISSUES

1. Đèn xe bị lỗi
Mức độ: HIGH
Trạng thái: OPEN
```

---

# 15. MODULE 8 – ACCESSORY MANAGEMENT

## Quản lý phụ kiện xe

Module này giúp theo dõi các phụ kiện hoặc trang bị đã lắp trên xe.

Ví dụ:

```text
Camera hành trình
Phim cách nhiệt
Lót sàn
Camera 360
Sạc
```

## Dữ liệu

```python
accessories = [
    ["Camera hanh trinh", 1500000],
    ["Phim cach nhiet", 8700000],
    ["Lot san", 500000]
]
```

## Chức năng

```text
Phụ kiện
│
├── Thêm phụ kiện
├── Xem danh sách
├── Tính tổng chi phí
└── Xóa phụ kiện
```

Module này **rất hợp với chủ đề ô tô cá nhân** và giúp project lớn hơn.

---

# 16. MODULE 9 – REPORT & DASHBOARD

## Báo cáo tổng hợp

Đây là module tổng hợp dữ liệu từ toàn bộ hệ thống.

## Ví dụ

```text
╔════════════════════════════════════╗
║        CARCARE DASHBOARD            ║
╠════════════════════════════════════╣
║ Vehicle: VF MPV7                    ║
║                                    ║
║ Total Distance: 1,250 km            ║
║ Total Trips: 12                     ║
║ Total Expense: 8,750,000 VND        ║
║ Maintenance Records: 3             ║
║ Active Issues: 1                    ║
║ Accessories: 4                      ║
║                                    ║
║ Vehicle Status: WARNING             ║
╚════════════════════════════════════╝
```

## Các báo cáo

### Báo cáo sử dụng

* Tổng số chuyến.
* Tổng quãng đường.
* Chuyến đi xa nhất.

### Báo cáo chi phí

* Tổng chi phí.
* Chi phí bảo dưỡng.
* Chi phí năng lượng.
* Chi phí phụ kiện.

### Báo cáo tình trạng

* Số lỗi.
* Số vấn đề đang mở.
* Trạng thái xe.

---

# 17. MODULE FILE HANDLER

## Quản lý file JSON

Module này chịu trách nhiệm đọc và ghi dữ liệu.

## Đọc dữ liệu

```python
import json

def load_data(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        return []
```

## Ghi dữ liệu

```python
def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
```

---

# 18. Thiết kế file JSON

## car.json

```json
[
    "VF MPV7",
    "Electric",
    "71A-XXXXX",
    1250,
    2026
]
```

## trips.json

```json
[
    [
        "17/07/2026",
        "Ben Tre",
        "TPHCM",
        120,
        "Normal"
    ]
]
```

## energy.json

```json
[
    [
        80,
        55,
        120
    ]
]
```

## maintenance.json

```json
[
    [
        "Kiem tra lop",
        "17/07/2026",
        1000,
        500000
    ]
]
```

## expenses.json

```json
[
    [
        "Sac xe",
        "Energy",
        120000
    ]
]
```

## inspections.json

```json
[
    [
        "Lop xe",
        "OK"
    ],
    [
        "Phanh",
        "OK"
    ],
    [
        "Den",
        "ERROR"
    ]
]
```

---

# 19. Luồng hoạt động của main.py

```text
START
  ↓
Load data from JSON
  ↓
Show Main Menu
  ↓
User presses ↑ ↓ Enter
  ↓
Select module
  ↓
Execute module
  ↓
Update data
  ↓
Save data to JSON
  ↓
Return Main Menu
  ↓
Exit?
  ↓
END
```

## Hướng code

```python
from file_handler import load_data, save_data
from menu import show_menu

car = load_data("data/car.json")
trips = load_data("data/trips.json")

while True:

    options = [
        "Vehicle Information",
        "Trip Management",
        "Energy Monitoring",
        "Maintenance",
        "Expense",
        "Vehicle Inspection",
        "Issues",
        "Accessories",
        "Report",
        "Exit"
    ]

    choice = show_menu(options)

    if choice == 0:
        pass

    elif choice == 1:
        pass

    elif choice == 2:
        pass

    elif choice == 9:
        break

save_data("data/car.json", car)
save_data("data/trips.json", trips)
```

---

# 20. Kế hoạch thực hiện trong 4 tuần

## TUẦN 1 – CORE SYSTEM

### Mục tiêu

Xây dựng nền tảng chương trình.

### Công việc

* Tạo repository GitHub.
* Tạo cấu trúc thư mục.
* Xây dựng `menu.py`.
* Xây dựng `file_handler.py`.
* Đọc và ghi JSON.
* Xây dựng module thông tin xe.

### Kết quả

Có thể:

```text
Mở chương trình
↓
Di chuyển bằng ↑ ↓
↓
Enter
↓
Xem thông tin xe
```

---

## TUẦN 2 – VEHICLE MANAGEMENT

### Công việc

* Trip Management.
* Energy Monitoring.
* Maintenance Management.

### Kết quả

Hệ thống có thể theo dõi:

```text
Hành trình
Năng lượng
Bảo dưỡng
```

---

## TUẦN 3 – VEHICLE CONTROL

### Công việc

* Expense Management.
* Vehicle Inspection.
* Issue & Alert Management.
* Accessory Management.

### Kết quả

Hệ thống có thể quản lý gần như toàn bộ quá trình sử dụng xe.

---

## TUẦN 4 – INTEGRATION & REPORT

### Công việc

* Dashboard.
* Báo cáo.
* Kiểm thử.
* Sửa lỗi.
* Viết README.
* Hoàn thiện GitHub.
* Chuẩn bị demo.

---

# 21. Phân chia công việc nhóm

## Thành viên 1 – Core System

* `main.py`
* `menu.py`
* `file_handler.py`

## Thành viên 2 – Vehicle Usage

* `car.py`
* `trip.py`
* `energy.py`

## Thành viên 3 – Vehicle Maintenance

* `maintenance.py`
* `inspection.py`
* `issue.py`

## Thành viên 4 – Cost & Report

* `expense.py`
* `accessory.py`
* `report.py`

---

# 22. Kết luận

CarCare Manager là một project Python cơ bản nhưng có quy mô tương đối lớn, tập trung vào việc quản lý duy nhất một chiếc ô tô cá nhân.

Project không sử dụng OOP, Dictionary, Set hay các thuật toán nâng cao. Thay vào đó, hệ thống sử dụng các kiến thức Python nền tảng như List, vòng lặp, điều kiện, hàm và đọc ghi JSON.

Việc chia hệ thống thành nhiều module giúp sinh viên hiểu được cách tổ chức một chương trình lớn hơn thay vì viết toàn bộ code trong một file duy nhất.

Đặc biệt, hệ thống sử dụng giao diện menu điều khiển bằng phím mũi tên và Enter, giúp project có tính tương tác cao hơn và gần với một ứng dụng quản lý thực tế.

**CarCare Manager mô phỏng quá trình người dùng theo dõi, quản lý và kiểm soát toàn bộ thông tin sử dụng của một chiếc ô tô cá nhân.**
