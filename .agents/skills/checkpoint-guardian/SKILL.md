---
name: checkpoint-guardian
description: Tự động nhận diện từ khóa "ngon/ổn rồi" từ Sếp để chốt mốc Checkpoint Time-Machine, ghi ngữ cảnh chi tiết và bảo vệ code chống hồi quy (Anti-Regression).
---

# Checkpoint Guardian Skill (Bảo Vệ Mốc An Toàn Time-Machine)

## Mục tiêu
Loại bỏ triệt để điểm đau: vừa sửa vừa test ghi đè dẫn đến mất code cũ đang chạy ngon, không biết rollback về thời điểm nào, hoặc rollback toàn bộ làm mất code mới vừa viết.

## Kích hoạt khi nào?
Mỗi khi Sếp đưa ra tín hiệu hoàn thành hoặc hài lòng:
- Từ khóa: `"ngon"`, `"ngon rồi"`, `"ổn rồi"`, `"chốt"`, `"chốt mốc"`, `"ưng rồi"`, `"release được"`.

## Quy trình thực thi 6 bước bắt buộc của AI:
1. **Trích xuất Ngữ Cảnh Công Việc:**
   - Thời gian hiện tại: `YYYY-MM-DD HH:mm:ss`.
   - Tính năng/nghiệp vụ cụ thể vừa hoàn thành thành công.
   - Danh sách các file vừa sửa đổi và đã kiểm thử chạy ngon.
2. **Tạo Git Tag Ngữ Nghĩa (Semantic Tag):**
   - Định dạng: `git tag -a "checkpoint/YYYYMMDD_HHmm_<slug_tinh_nang>" -m "Mốc chạy ngon: <mo_ta>"`
   - Ví dụ: `checkpoint/20261104_1215_soft_reboot_ok`
3. **Cập nhật Bảng Tra Cứu `SO_TAY_KIEM_SOAT_PHIEN_BAN.md`:**
   - Thêm dòng mới vào đầu bảng với đầy đủ: Thời điểm, Ngữ cảnh, File thay đổi, Lệnh rollback chọn lọc 1-click.
4. **Lưu Ký Ức Vào AgentMemory:**
   - Gọi tool `memory_save`:
     - `concept`: "checkpoint, stable-milestone, <tên-dự-án>"
     - `content`: "Mốc checkpoint/<tag> chạy ổn định tính năng <ngữ_cảnh> vào ngày <thời_gian>."
5. **Báo Cáo Ngắn Gọn Cho Sếp:**
   - Thông báo mã mốc vừa chốt.
   - Hướng dẫn lệnh khôi phục chọn lọc nếu tương lai phát hiện bug.
6. **Bắn Thông Báo Telegram Tự Động Về Máy Sếp TOM (Bot PJ Manager):**
   - Tự động gọi: `python "c:\Antigravity Projects\EVO Assistant\.agents\notify_telegram.py" "👑 <b>[Tên Dự Án]:</b> Đã chốt mốc <tag> thành công cho Sếp TOM!"` để điện thoại Sếp nhận tin báo ngay lập tức qua bot PJ Manager (@tcmPJmanager_bot).
   - Tuyệt đối không báo qua bot xào bài bđs @bdstuan123bot.

## Nguyên tắc Phục Hồi Chọn Lọc (Selective Surgery Rollback):
Khi cần quay lại bản cũ, **TUYỆT ĐỐI KHÔNG DÙNG `git reset --hard`** vì sẽ làm mất sạch code mới.
Chỉ khôi phục đúng file logic bị hỏng:
```bash
git checkout <MÃ_CHECKPOINT> -- path/to/file_bi_loi.ext
```
