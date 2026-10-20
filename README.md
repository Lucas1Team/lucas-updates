<!-- [Update: 20/10/2026 21:00]
Cập nhật README kênh OTA Lucas-1Changer Pro v2.3.5 Chính thức.
Bổ sung liên kết tải Hướng dẫn sử dụng HTML & PDF v2.3.5. -->
# ⚡ Lucas-1Changer Pro - Kênh Cập Nhật Chính Thức (OTA Updates)

Kênh phân phối và lưu trữ các gói cập nhật OTA tự động chính thức dành cho phần mềm **Lucas-1Changer Pro**.

---

## 🚀 Thông Tin Bản Phát Hành Mới Nhất
* **Phiên bản hiện tại:** `v2.3.5` (Official Release)
* **Ngày phát hành:** 20/10/2026
* **Trạng thái:** Bản phát hành chính thức ổn định, sẵn sàng OTA 1-Click.

### 📋 Điểm Mới Nổi Bật Trong Bản v2.3.5:
1. **Chuẩn hóa Cột "Dòng máy" (thay thế "Tên máy"):** Tự động giải mã các mã phần cứng kỹ thuật (`SM-9373`, `SM-G973`, `SM-S911`, `2201123G`...) thành tên thương mại quen thuộc (Samsung Galaxy S10, Galaxy S23, Xiaomi 12 Pro...). Form phân cấp 4 tầng: `Hãng` -> `Dòng máy` -> `Mã máy` -> `Phiên bản Android` kèm nút `🎲 Random giữ dòng máy`.
2. **Hộp thoại "⚡ Xếp Lưới Màn Hình Live Ra Desktop" Đa Kích Thước:**
   - Bộ chọn kích thước màn hình theo tỷ lệ 9:16 phong phú: *Mặc định (320x570)*, *Tiêu chuẩn (280x500)*, *Nhỏ gọn (240x426)*, *Lớn (360x640)*, *Rất lớn (400x710)*, *Tự co giãn vừa Desktop*, hoặc *Tùy chỉnh WxH*.
   - Checkbox tích chọn từng thiết bị độc lập kèm nút `[✓ Chọn tất cả]` và `[✕ Bỏ chọn cả]`.
   - Tự động căn góc trên bên trái Desktop (Top-Left: `Left + 2, Top + 2`) dàn đều sang phải theo thứ tự `#1, #2, #3...`, tự động xuống hàng khi chạm mép phải Desktop.
   - Tự ghi nhớ vị trí cửa sổ Scrcpy trên Desktop (Desktop Slot Memory).
3. **Lá chắn bảo vệ toàn vẹn Sandbox Tar Extraction Shield (`RESTORE_SANDBOX_INTEGRITY_TOKEN`):** Ngăn chặn tuyệt đối mọi sửa đổi làm ảnh hưởng đến chức năng Khôi phục dữ liệu và an toàn phân vùng Root.
4. **Khắc phục triệt để Tab Thay đổi thông tin trên máy thật:** Can thiệp sâu toàn bộ partition properties qua `resetprop` đa nền tảng (Magisk, KernelSU, APatch), cập nhật SSAID và đồng bộ file cấu hình JSON đa vị trí kèm restart Zygote trong 2 giây.
5. **Tích hợp nút Hướng Dẫn Sử Dụng 1-Click:** Bấm `[📖 Hướng dẫn sử dụng]` ở thanh trạng thái để mở ngay tài liệu cẩm nang.

---

## 📖 Cẩm Nang Hướng Dẫn Sử Dụng (HDSD v2.3.5)
* 🌐 **Xem trực tuyến (HTML):** [HUONG_DAN_SU_DUNG.html](https://raw.githubusercontent.com/Lucas1Team/lucas-updates/main/HUONG_DAN_SU_DUNG.html)
* 📄 **Tải file PDF in ấn chuẩn đẹp (5 MB):** [HUONG_DAN_SU_DUNG.pdf](https://raw.githubusercontent.com/Lucas1Team/lucas-updates/main/HUONG_DAN_SU_DUNG.pdf)

---

## 📥 Tải Về Cập Nhật (OTA)

| Tệp tin | Mô tả | Dung lượng | Tải xuống |
| :--- | :--- | :--- | :--- |
| **LucasChanger_Pro_v2.3.5.exe** | File thực thi chính v2.3.5 (Bản mới nhất) | ~600 KB | [Tải EXE](https://raw.githubusercontent.com/Lucas1Team/lucas-updates/main/LucasChanger_Pro_v2.3.5.exe) |
| **LucasChanger_Pro_v2.3.4.exe** | Bản cập nhật v2.3.4 | ~580 KB | [Tải EXE](https://raw.githubusercontent.com/Lucas1Team/lucas-updates/main/LucasChanger_Pro_v2.3.4.exe) |
| **version.json** | Cấu hình kiểm tra phiên bản OTA v2.3.5 | ~2 KB | [Xem JSON](https://raw.githubusercontent.com/Lucas1Team/lucas-updates/main/version.json) |

---
© 2026 Lucas Team. All rights reserved.
