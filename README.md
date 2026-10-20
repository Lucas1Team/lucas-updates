<!-- [Update: 20/10/2026 22:35]
Cập nhật README kênh OTA Lucas-1Changer Pro v2.3.6 Chính thức.
Bổ sung liên kết tải LucasChanger_Pro_v2.3.6.exe, Hướng dẫn sử dụng HTML & PDF v2.3.6. -->
# ⚡ Lucas-1Changer Pro - Kênh Cập Nhật Chính Thức (OTA Updates)

Kênh phân phối và lưu trữ các gói cập nhật OTA tự động chính thức dành cho phần mềm **Lucas-1Changer Pro**.

---

## 🚀 Thông Tin Bản Phát Hành Mới Nhất
* **Phiên bản hiện tại:** `v2.3.6` (Official Release)
* **Ngày phát hành:** 20/10/2026
* **Trạng thái:** Bản phát hành chính thức ổn định, sẵn sàng OTA 1-Click.

### 📋 Điểm Mới Nổi Bật Trong Bản v2.3.6:
1. **Tái Cấu Trúc & Tinh Gọn Giao Diện Theo Mockup Demo v8:**
   - Thu gọn bề ngang tổng thể về 1100px vừa vặn, hiển thị hoàn hảo trên mọi độ phân giải.
   - Top Action Bar phẳng hóa: Loại bỏ các nút thừa/trùng lặp (Làm mới cấu hình, Đăng xuất, Bật/tắt log, Xếp lưới nhỏ phía trên). Các nút bấm hiển thị văn bản phẳng, rõ ràng, không icon rối mắt.
   - Đóng khung viền bao riêng cố định 4 ô Dòng máy & Hệ điều hành (Hãng, Dòng máy, Phiên bản Android, Tên phiên bản) có Suggest Dropdown List tiện dụng.
   - Bố trí 8 ô thông số phần cứng đối xứng 2 cột tăm tắp kèm 2 nút xem trước chuẩn chữ đỏ: *[Random giữ dòng máy (xem trước)]* & *[Random toàn bộ (xem trước)]*.
2. **Nút Gộp Thông Minh [Dán Mail & Khôi Phục] (Màu Xanh Dương):**
   - Tự động nhận diện chuỗi Mail|Pass|2FA|Recovery trong Clipboard, lưu vào danh mục quản lý và kích hoạt quy trình Bung nén khôi phục (Restore App Data) chỉ trong 1 cú nhấp chuột duy nhất.
3. **Phân Cấp 4 Nút Hành Động Chuẩn (Thực Thi Trực Tiếp Lên Điện Thoại):**
   - **Nút 1 (Màu Xanh ngọc Teal `#0f766e` - Ưu tiên số 1):** `RANDOM & CHANGE (Giữ Dòng Máy: Galaxy S23)` - Tự động sinh danh tính phần cứng mới nhưng bảo toàn 100% dòng máy đang kết nối. Tên dòng máy cập nhật động theo thiết bị.
   - **Nút 2 (Màu Indigo `#4338ca`):** `RANDOM & CHANGE (Dòng Máy Bất Kỳ)` - Sinh ngẫu nhiên sang một dòng máy mới bất kỳ trong kho dữ liệu.
   - **Nút 3 (Màu Xanh Dương `#2563eb`):** `CHANGE THEO THÔNG SỐ VỪA TẠO` - Áp dụng chính xác những giá trị đang hiển thị trên 12 ô thông số.
   - **Nút 4 (Màu Hổ Phách `#d97706`):** `RESTORE VỀ GỐC CỦA MÁY` - Đưa thiết bị về đúng thông số xuất xưởng ban đầu.
   - Tích hợp Checkbox `[Tự động làm sạch ứng dụng (Wipe Clean Data)]` ngay trên tiêu đề nhóm hành động nhanh.
4. **Hotfix Scrcpy Chống Giật Lag Cho PC Yếu & Auto Dọn Dẹp Khi Thoát:**
   - Luôn truyền tham số tối ưu `--max-size 480 --max-fps 25 -b 2M` giúp máy tính PC yếu, Core i3, Ram 8GB hay laptop văn phòng vẫn mở mượt mà hàng chục máy.
   - Tùy chọn `--turn-screen-off` tự động tắt màn hình vật lý trên điện thoại khi remote, giúp mát máy và chống chai phù pin.
   - Cơ chế `CloseAllScrcpySilent` tự động kết thúc triệt để mọi tiến trình `scrcpy.exe` ngầm ngay khi đóng Lucas-1Changer, giải phóng 100% RAM và CPU.
5. **Kế Thừa Toàn Bộ Các Tính Năng Đỉnh Cao Của v2.3.5:**
   - Lá chắn bảo vệ toàn vẹn Sandbox Tar Extraction Shield (`RESTORE_SANDBOX_INTEGRITY_TOKEN`).
   - Can thiệp sâu phần cứng qua `resetprop` đa nền tảng, cập nhật SSAID và restart Zygote trong 2 giây.
   - Hộp thoại Xếp lưới Desktop Top-Left đa kích thước (9:16) kèm bộ nhớ tọa độ cửa sổ độc lập.

---

## 📖 Cẩm Nang Hướng Dẫn Sử Dụng (HDSD v2.3.6)
* 🌐 **Xem trực tuyến (HTML):** [HUONG_DAN_SU_DUNG.html](https://raw.githubusercontent.com/Lucas1Team/lucas-updates/main/HUONG_DAN_SU_DUNG.html)
* 📄 **Tải file PDF in ấn chuẩn đẹp (5 MB):** [HUONG_DAN_SU_DUNG.pdf](https://raw.githubusercontent.com/Lucas1Team/lucas-updates/main/HUONG_DAN_SU_DUNG.pdf)

---

## 📥 Tải Về Cập Nhật (OTA)

| Tệp tin | Mô tả | Dung lượng | Tải xuống |
| :--- | :--- | :--- | :--- |
| **LucasChanger_Pro_v2.3.6.exe** | File thực thi chính v2.3.6 (Bản mới nhất) | ~616 KB | [Tải EXE](https://raw.githubusercontent.com/Lucas1Team/lucas-updates/main/LucasChanger_Pro_v2.3.6.exe) |
| **LucasChanger_Pro_v2.3.5.exe** | Bản cập nhật v2.3.5 (Lưu trữ ổn định) | ~612 KB | [Tải EXE](https://raw.githubusercontent.com/Lucas1Team/lucas-updates/main/LucasChanger_Pro_v2.3.5.exe) |
| **LucasChanger_Pro_v2.3.4.exe** | Bản cập nhật v2.3.4 | ~580 KB | [Tải EXE](https://raw.githubusercontent.com/Lucas1Team/lucas-updates/main/LucasChanger_Pro_v2.3.4.exe) |
| **version.json** | Cấu hình kiểm tra phiên bản OTA v2.3.6 | ~2 KB | [Xem JSON](https://raw.githubusercontent.com/Lucas1Team/lucas-updates/main/version.json) |

---
© 2026 Lucas Team. All rights reserved.