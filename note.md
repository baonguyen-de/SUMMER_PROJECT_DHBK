# 📝 TIẾN TRÌNH PHÁT TRIỂN DỰ ÁN (PROJECT PROGRESS LOG)

## 📌 Tổng Quan Dự Án
- **Tên dự án:** Carcare Manager
- **Ngôn ngữ:** Python
- **Cấu trúc:** Đa module (`utils.py`, `car.py`, `trip.py`, `report.py`, `menu.py`...)

---

## 🚀 Tiến Trình Hoàn Thành (Milestones)

### 1. Quản lý thông tin xe (`car.py`) - [Hoàn thành ✅]
- [x] Xây dựng các hàm nhập dữ liệu chuẩn hóa với bẫy lỗi (`car_km`, `car_year`, `car_name`...).
- [x] Đã đồng bộ số km ban đầu của xe vào bộ nhớ chung: `utils.initial_car_km = CARKM`.
- [x] Khởi tạo danh sách lưu trữ `utils.car_info`.

### 2. Quản lý lịch sử chuyến đi (`trip.py`) - [Hoàn thành ✅]
- [x] Xây dựng hàm `add_trip()` để thêm chuyến đi vào `utils.trips`.
- [x] Xây dựng hàm `view_trip()` hiển thị danh sách các chuyến đi đã nhập.
- [x] Xây dựng hàm `total_distance()` tính tổng số km của tất cả các chuyến đi.
- [x] Đã bẫy lỗi danh sách rỗng cho hàm `show_summary()` / tìm chuyến đi dài nhất (`max()`).

### 3. Module Báo cáo tổng hợp (`report.py`) - [Hoàn thành ✅]
- [x] Tích hợp hiển thị toàn bộ thông tin xe, chuyến đi, chi phí, tiêu thụ năng lượng.
- [x] Tự động cập nhật số km hiện tại của xe bằng tổng số km trip cộng với số km ban đầu.

---

## 🛠️ Lịch Sử Sửa Lỗi & Cải Tiến (Bug Fixes & Refactoring)

1. **Sửa lỗi `IndexError` khi lấy số km chuyến đi:**
   - *Nguyên nhân:* Hiểu nhầm `utils.trips` là list 1 chiều thay vì list 2 chiều.
   - *Khắc phục:* Duyệt qua từng trip trong `utils.trips` và lấy giá trị khoảng cách ở vị trí `trip[3]`.

2. **Khắc phục lỗi cộng dồn số km vô hạn:**
   - *Nguyên nhân:* Dùng phép cộng dồn `+=` trong hàm `report()`, khiến mỗi lần mở menu Báo cáo xem thì số km xe lại nhảy vọt lên.
   - *Khắc phục:* Chuyển sang công thức gán tuyệt đối:  
     `utils.car_info[3] = utils.initial_car_km + trip.total_distance()`

3. **Sửa lỗi `ValueError: max() iterable argument is empty`:**
   - *Nguyên nhân:* Gọi hàm `max()` tìm chuyến đi dài nhất khi `utils.trips` chưa có dữ liệu (list rỗng).
   - *Khắc phục:* Thêm điều kiện kiểm tra `if not utils.trips:` trả về thông báo an toàn trước khi tìm `max()`.

---

## 🎯 Trạng Thái Hiện Tại & Bước Tiếp Theo

- **Trạng thái:** Dữ liệu số km và báo cáo đã hoạt động chính xác, ổn định, không bị crash chương trình.
- **Tính năng cần phát triển/tối ưu tiếp theo:**
  - [ ] Hoàn thiện thêm/sửa/xóa chuyến đi và kiểm tra lại việc tự động tính lại số km xe.
  - [ ] Kiểm tra các module bảo dưỡng (`maintenance.py`), chi phí (`expense.py`), sự cố (`issue.py`).