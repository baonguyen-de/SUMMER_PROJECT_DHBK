# 🚗 CarCare Manager

## Hệ thống quản lý và theo dõi ô tô theo phiên sử dụng

---

## 📌 1. Giới thiệu

**CarCare Manager** là một hệ thống quản lý và theo dõi ô tô được xây dựng bằng ngôn ngữ Python.

Dự án mô phỏng quá trình quản lý **một chiếc ô tô duy nhất** trong một phiên sử dụng. Người dùng có thể quản lý thông tin xe, theo dõi các chuyến đi, kiểm tra mức tiêu thụ năng lượng, quản lý bảo dưỡng, chi phí, tình trạng xe, các vấn đề phát sinh và phụ kiện của xe.

Hệ thống được xây dựng dưới dạng **ứng dụng chạy trên giao diện dòng lệnh (Command-Line Interface)**.

Người dùng có thể điều khiển menu bằng:

```text
↑       Di chuyển lên
↓       Di chuyển xuống
Enter   Chọn
```

### Đặc điểm chính

CarCare Manager hoạt động theo mô hình **quản lý theo phiên sử dụng**.

Tất cả dữ liệu chỉ được lưu tạm thời trong bộ nhớ của chương trình bằng các **List trong Python**.

Khi chương trình kết thúc, toàn bộ dữ liệu của phiên hiện tại sẽ bị xóa.

---

## 🎯 2. Mục tiêu dự án

Mục tiêu chính của dự án là áp dụng các kiến thức Python cơ bản để xây dựng một hệ thống tương đối lớn và được chia thành nhiều module.

Thông qua dự án, sinh viên có thể thực hành:

* Biến và các kiểu dữ liệu cơ bản.
* List.
* Câu lệnh điều kiện.
* Vòng lặp.
* Hàm.
* Xử lý dữ liệu nhập từ người dùng.
* Xử lý chuỗi.
* Chia chương trình thành nhiều module.
* Xây dựng ứng dụng giao diện dòng lệnh.
* Làm việc nhóm và quản lý mã nguồn bằng GitHub.

---

## 🚘 3. Ý tưởng của dự án

CarCare Manager quản lý **một chiếc xe duy nhất trong một phiên chạy chương trình**.

Luồng hoạt động của hệ thống:

```text
Khởi động chương trình
        ↓
Khởi tạo phiên quản lý xe
        ↓
Quản lý và theo dõi xe
        ↓
Xem báo cáo phiên sử dụng
        ↓
Thoát chương trình
        ↓
Dữ liệu bị xóa
```

Mỗi lần chạy chương trình là một **phiên quản lý mới**.

---

## 🧠 4. Phạm vi kỹ thuật

Dự án được thiết kế dành cho **sinh viên mới học lập trình Python**.

### Các kiến thức được sử dụng

* Python.
* List.
* String.
* Integer.
* Float.
* Câu lệnh `if`, `elif`, `else`.
* Vòng lặp `for`.
* Vòng lặp `while`.
* Hàm.
* Module.
* Xử lý input từ người dùng.
* Giao diện dòng lệnh.

### ❌ Các kiến thức không sử dụng

Để phù hợp với mục tiêu Python cơ bản, dự án **không sử dụng**:

* Lập trình hướng đối tượng (OOP).
* Class.
* Dictionary.
* Set.
* Cơ sở dữ liệu.
* File JSON.
* Đọc và ghi file.
* API.
* Web Framework.
* Artificial Intelligence.
* Machine Learning.
* Thuật toán nâng cao.

> Dự án tập trung vào việc sử dụng các kiến thức Python cơ bản để xây dựng một hệ thống có nhiều chức năng và được chia thành nhiều module.

---

## 🚗 5. Phạm vi quản lý xe

Hệ thống chỉ quản lý **một chiếc xe duy nhất**.

Hệ thống không hỗ trợ:

* Quản lý nhiều xe.
* Quản lý đội xe.
* Tài khoản người dùng.
* Nhiều người dùng.

Thông tin xe được khởi tạo khi chương trình bắt đầu.

Ví dụ:

```text
Tên xe: VF MPV7
Loại xe: Xe điện
Biển số: 71A-XXXXX
```

---

# 🧩 6. Các module chính

CarCare Manager bao gồm các module:

* 🚗 Quản lý thông tin xe.
* 🛣️ Quản lý chuyến đi.
* ⚡ Theo dõi năng lượng.
* 🔧 Quản lý bảo dưỡng.
* 💰 Quản lý chi phí.
* 🔍 Kiểm tra tình trạng xe.
* ⚠️ Quản lý vấn đề và cảnh báo.
* 🧰 Quản lý phụ kiện.
* 📊 Báo cáo phiên sử dụng.

---

# 🧩 7. Chi tiết các module

## 7.1. Module Quản lý thông tin xe

Module này quản lý các thông tin cơ bản của xe.

### Các chức năng chính

* Xem thông tin xe.
* Cập nhật thông tin xe.
* Cập nhật số kilomet hiện tại.

### Thông tin có thể quản lý

```text
Tên xe
Loại xe
Biển số
Số kilomet hiện tại
Năm sản xuất
```

### Ví dụ

```text
========== THÔNG TIN XE ==========

Tên xe: VF MPV7
Loại xe: Xe điện
Biển số: 71A-XXXXX
Số kilomet: 1250 km
Năm sản xuất: 2026
```

---

## 7.2. Module Quản lý chuyến đi

Module này quản lý lịch sử các chuyến đi của xe trong phiên hiện tại.

### Các chức năng chính

* Thêm chuyến đi.
* Xem lịch sử chuyến đi.
* Tính tổng quãng đường.
* Tìm chuyến đi dài nhất.
* Xóa chuyến đi.

### Thông tin một chuyến đi

```text
Ngày
Điểm bắt đầu
Điểm đến
Quãng đường
Chế độ lái
```

### Ví dụ

```text
Ngày: 17/07/2026
Điểm đi: Bến Tre
Điểm đến: Thành phố Hồ Chí Minh
Quãng đường: 120 km
Chế độ lái: Normal
```

### Cách lưu dữ liệu

Mỗi chuyến đi được lưu dưới dạng một `List`.

```python
trip = [
    "17/07/2026",
    "Bến Tre",
    "Thành phố Hồ Chí Minh",
    120,
    "Normal"
]
```

Các chuyến đi được quản lý trong một `List` lớn hơn.

```python
trips = [
    [
        "17/07/2026",
        "Bến Tre",
        "Thành phố Hồ Chí Minh",
        120,
        "Normal"
    ]
]
```

---

## 7.3. Module Theo dõi năng lượng

Module này theo dõi mức tiêu thụ năng lượng của xe.

Hệ thống hỗ trợ hai loại xe:

* Xe điện.
* Xe sử dụng nhiên liệu.

### Đối với xe điện

Hệ thống quản lý:

* Phần trăm pin ban đầu.
* Phần trăm pin sau chuyến đi.
* Quãng đường di chuyển.

Ví dụ:

```text
Pin ban đầu: 80%
Pin sau chuyến đi: 55%
Quãng đường: 120 km
```

Hệ thống tính lượng pin đã sử dụng:

```text
Pin đã sử dụng = Pin ban đầu - Pin sau chuyến đi
```

### Đối với xe sử dụng nhiên liệu

Hệ thống quản lý:

* Lượng nhiên liệu đã sử dụng.
* Quãng đường di chuyển.

Công thức tiêu thụ nhiên liệu:

```text
Mức tiêu thụ = Lượng nhiên liệu / Quãng đường × 100
```

---

## 7.4. Module Quản lý bảo dưỡng

Module này quản lý lịch sử bảo dưỡng của xe.

### Các chức năng chính

* Thêm lịch sử bảo dưỡng.
* Xem lịch sử bảo dưỡng.
* Xóa lịch sử bảo dưỡng.
* Kiểm tra cảnh báo bảo dưỡng.

### Thông tin bảo dưỡng

```text
Hạng mục bảo dưỡng
Ngày thực hiện
Số kilomet
Chi phí
```

### Ví dụ

```text
Hạng mục: Kiểm tra lốp
Ngày: 17/07/2026
Số kilomet: 1000 km
Chi phí: 500000 VND
```

Hệ thống có thể so sánh số kilomet hiện tại với lần bảo dưỡng gần nhất.

Nếu xe đã đi quá một khoảng kilomet được quy định, hệ thống hiển thị cảnh báo:

```text
⚠️ XE CÓ THỂ CẦN ĐƯỢC BẢO DƯỠNG
```

---

## 7.5. Module Quản lý chi phí

Module này quản lý các khoản chi phí liên quan đến xe.

### Các nhóm chi phí

* Năng lượng.
* Bảo dưỡng.
* Bảo hiểm.
* Phụ kiện.
* Khác.

### Các chức năng chính

* Thêm chi phí.
* Xem lịch sử chi phí.
* Tính tổng chi phí.
* Tính chi phí theo nhóm.
* Xóa chi phí.

### Ví dụ

```text
Mô tả: Sạc xe
Loại chi phí: Năng lượng
Số tiền: 120000 VND
```

Hệ thống có thể tính tổng số tiền đã chi trong phiên hiện tại.

---

## 7.6. Module Kiểm tra tình trạng xe

Module này mô phỏng việc kiểm tra một số bộ phận của xe.

### Các bộ phận có thể kiểm tra

* Lốp xe.
* Hệ thống phanh.
* Đèn xe.
* Điều hòa.
* Pin hoặc hệ thống năng lượng.

Mỗi bộ phận có thể có một trạng thái:

```text
OK
WARNING
ERROR
```

### Ví dụ

```text
========== KIỂM TRA XE ==========

Lốp xe          [OK]
Phanh           [OK]
Đèn xe          [ERROR]
Điều hòa        [OK]
Pin             [OK]
```

Nếu phát hiện trạng thái `ERROR`, hệ thống hiển thị cảnh báo.

---

## 7.7. Module Quản lý vấn đề và cảnh báo

Module này quản lý các vấn đề phát sinh trong quá trình sử dụng xe.

### Các chức năng chính

* Thêm vấn đề.
* Xem các vấn đề đang tồn tại.
* Đóng vấn đề.
* Xóa vấn đề.

### Thông tin vấn đề

```text
Mô tả vấn đề
Mức độ nghiêm trọng
Trạng thái
```

### Ví dụ

```text
Vấn đề: Đèn xe bị lỗi
Mức độ: HIGH
Trạng thái: OPEN
```

Hệ thống có thể hiển thị các vấn đề đang mở:

```text
⚠️ CÁC VẤN ĐỀ ĐANG TỒN TẠI
```

---

## 7.8. Module Quản lý phụ kiện

Module này quản lý các phụ kiện được lắp đặt hoặc sử dụng trên xe.

### Ví dụ phụ kiện

* Camera hành trình.
* Phim cách nhiệt.
* Lót sàn.
* Camera 360.
* Các phụ kiện khác.

### Các chức năng chính

* Thêm phụ kiện.
* Xem danh sách phụ kiện.
* Tính tổng chi phí phụ kiện.
* Xóa phụ kiện.

### Ví dụ

```text
Tên phụ kiện: Camera hành trình
Chi phí: 1500000 VND
```

---

## 7.9. Module Báo cáo phiên sử dụng

Module này tổng hợp toàn bộ thông tin của xe trong phiên hiện tại.

### Nội dung báo cáo

* Thông tin xe.
* Tổng số chuyến đi.
* Tổng quãng đường.
* Tổng mức tiêu thụ năng lượng.
* Tổng chi phí.
* Số lần bảo dưỡng.
* Số vấn đề đang tồn tại.
* Số lượng phụ kiện.
* Trạng thái tổng quan của xe.

### Ví dụ

```text
╔════════════════════════════════════╗
║       BÁO CÁO PHIÊN SỬ DỤNG        ║
╠════════════════════════════════════╣
║ Xe: VF MPV7                         ║
║                                    ║
║ Tổng chuyến đi: 5                   ║
║ Tổng quãng đường: 620 km            ║
║ Tổng chi phí: 1,200,000 VND         ║
║                                    ║
║ Lịch sử bảo dưỡng: 2                ║
║ Vấn đề đang tồn tại: 1              ║
║ Số phụ kiện: 4                      ║
║                                    ║
║ Trạng thái xe: WARNING              ║
╚════════════════════════════════════╝
```

---

# 🖥️ 8. Giao diện chương trình

CarCare Manager sử dụng giao diện dòng lệnh.

Menu chính được điều khiển bằng:

```text
↑       Di chuyển lên
↓       Di chuyển xuống
Enter   Chọn
```

### Ví dụ menu chính

```text
╔════════════════════════════════════╗
║          CARCARE MANAGER            ║
╠════════════════════════════════════╣
║ > Quản lý thông tin xe              ║
║   Quản lý chuyến đi                 ║
║   Theo dõi năng lượng               ║
║   Quản lý bảo dưỡng                 ║
║   Quản lý chi phí                   ║
║   Kiểm tra tình trạng xe            ║
║   Vấn đề và cảnh báo                ║
║   Quản lý phụ kiện                  ║
║   Báo cáo phiên sử dụng             ║
║   Thoát                             ║
╚════════════════════════════════════╝
```

Ký hiệu `>` thể hiện mục đang được chọn.

---

# 💾 9. Cách quản lý dữ liệu

CarCare Manager sử dụng **dữ liệu tạm thời trong bộ nhớ chương trình**.

Hệ thống **không sử dụng**:

* File JSON.
* File TXT.
* Cơ sở dữ liệu.
* Bộ nhớ ngoài.

Ví dụ:

```python
car = [
    "VF MPV7",
    "Electric",
    "71A-XXXXX",
    1250,
    2026
]

trips = []

energy = []

maintenance = []

expenses = []

inspections = []

issues = []

accessories = []
```

Tất cả dữ liệu chỉ tồn tại khi chương trình đang chạy.

Khi người dùng thoát chương trình:

```text
Thoát chương trình
        ↓
Kết thúc phiên
        ↓
Dữ liệu bị xóa
```

Mỗi lần chạy lại chương trình, hệ thống bắt đầu với một phiên mới và dữ liệu rỗng.

---

# 📁 10. Cấu trúc dự án

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
└── report.py
```

---

# 🔄 11. Luồng hoạt động của chương trình

```text
START
  ↓
Khởi tạo thông tin xe
  ↓
Khởi tạo các List dữ liệu
  ↓
Hiển thị Menu chính
  ↓
Người dùng chọn module
  ↓
Thực hiện chức năng
  ↓
Quay lại Menu chính
  ↓
Người dùng chọn Thoát
  ↓
Hiển thị Báo cáo phiên
  ↓
END
```

---

# 🛠️ 12. Kế hoạch phát triển

## Tuần 1 – Xây dựng hệ thống cơ bản

* Tạo GitHub Repository.
* Thiết kế cấu trúc project.
* Xây dựng luồng chương trình chính.
* Xây dựng menu điều hướng bằng phím mũi tên.
* Xây dựng module quản lý thông tin xe.

### Kết quả mong đợi

Chương trình có thể:

* Khởi động một phiên quản lý xe.
* Hiển thị menu chính.
* Điều hướng bằng phím lên, xuống.
* Chọn chức năng bằng Enter.
* Xem thông tin xe.

---

## Tuần 2 – Quản lý sử dụng và bảo dưỡng

* Xây dựng module Quản lý chuyến đi.
* Xây dựng module Theo dõi năng lượng.
* Xây dựng module Quản lý bảo dưỡng.

### Kết quả mong đợi

Hệ thống có thể quản lý:

* Các chuyến đi.
* Quãng đường.
* Mức tiêu thụ năng lượng.
* Lịch sử bảo dưỡng.

---

## Tuần 3 – Quản lý và kiểm soát xe

* Xây dựng module Quản lý chi phí.
* Xây dựng module Kiểm tra tình trạng xe.
* Xây dựng module Vấn đề và cảnh báo.
* Xây dựng module Quản lý phụ kiện.

### Kết quả mong đợi

Hệ thống có thể quản lý:

* Chi phí sử dụng xe.
* Tình trạng các bộ phận.
* Các vấn đề phát sinh.
* Phụ kiện của xe.

---

## Tuần 4 – Tích hợp và kiểm thử

* Xây dựng module Báo cáo phiên sử dụng.
* Tích hợp tất cả các module.
* Kiểm thử toàn bộ hệ thống.
* Sửa lỗi.
* Cải thiện giao diện.
* Hoàn thiện README.
* Chuẩn bị demo project.

---

# 🧪 13. Kiểm thử

Hệ thống được kiểm thử bằng phương pháp **kiểm thử chức năng thủ công**.

Mentor hoặc người dùng sẽ khởi động chương trình và thao tác trực tiếp thông qua giao diện menu.

### Một số tình huống kiểm thử

* Nhập thông tin xe hợp lệ.
* Thêm nhiều chuyến đi.
* Tính tổng quãng đường.
* Thêm chi phí.
* Tính tổng chi phí.
* Thêm lịch sử bảo dưỡng.
* Kiểm tra cảnh báo bảo dưỡng.
* Thêm vấn đề cho xe.
* Kiểm tra trạng thái xe.
* Thêm và xóa phụ kiện.
* Kiểm tra báo cáo phiên sử dụng.
* Thoát chương trình và khởi động lại.

Do hệ thống hoạt động theo mô hình phiên sử dụng, mỗi lần khởi động chương trình sẽ bắt đầu với dữ liệu mới.

---

# 👥 14. Phân công nhóm

| Thành viên   | Phụ trách                             |
| ------------ | ------------------------------------- |
| Thành viên 1 | Hệ thống chính và Menu                |
| Thành viên 2 | Thông tin xe, Chuyến đi và Năng lượng |
| Thành viên 3 | Bảo dưỡng, Kiểm tra xe và Vấn đề      |
| Thành viên 4 | Chi phí, Phụ kiện và Báo cáo          |

---

# 🎓 15. Mục đích học tập

CarCare Manager được xây dựng như một project Python dành cho sinh viên mới bắt đầu học lập trình.

Dự án minh họa cách kết hợp các kiến thức Python cơ bản để xây dựng một hệ thống có nhiều chức năng và được chia thành nhiều module.

Thông qua project, sinh viên có thể cải thiện:

* Tư duy lập trình Python.
* Kỹ năng sử dụng List.
* Kỹ năng xây dựng hàm.
* Kỹ năng chia module.
* Kỹ năng xây dựng ứng dụng giao diện dòng lệnh.
* Kỹ năng làm việc nhóm bằng GitHub.

---

# 📌 16. Kết luận

CarCare Manager là một hệ thống quản lý và theo dõi một chiếc ô tô trong một phiên sử dụng.

Hệ thống cho phép người dùng quản lý thông tin xe, chuyến đi, năng lượng, bảo dưỡng, chi phí, tình trạng xe, các vấn đề và phụ kiện.

Dự án không sử dụng lưu trữ dữ liệu lâu dài. Toàn bộ dữ liệu chỉ tồn tại tạm thời trong bộ nhớ chương trình và sẽ bị xóa khi chương trình kết thúc.

Bằng cách chỉ sử dụng các kiến thức Python cơ bản, CarCare Manager tạo ra một bài toán đủ lớn để sinh viên rèn luyện kỹ năng lập trình, tổ chức code và làm việc nhóm thông qua GitHub.
