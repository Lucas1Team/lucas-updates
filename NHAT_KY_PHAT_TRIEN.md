# Nhật ký phát triển dự án

## [04/11/2026 11:35] - Tích hợp bộ nhớ dài hạn AgentMemory 17 skills
- **Nội dung:** Đồng bộ 17 kỹ năng bộ nhớ vĩnh viễn () vào  và khóa phiên bản qua .
- **Cấu hình:** Bổ sung quy chuẩn tương tác bộ nhớ MCP (, , ) vào .



## [04/11/2026 11:45] - Tích hợp Cơ chế Tự động Kích hoạt Bộ nhớ cho AI trên Máy Khác (Auto Bootstrap)
- **Cơ chế:** Đã đóng gói bộ script tự động hóa cross-platform `.agents/setup_agentmemory.py`, `.agents/setup_agentmemory.ps1`, `.agents/setup_agentmemory.sh`.
- **Hành vi AI:** Khi code được clone/pull sang máy mới (Windows / Mac / Linux), nếu AI phát hiện chưa có MCP tool `memory_recall`, AI sẽ tự động kích hoạt script bootstrap để cài đặt runtime, đăng ký MCP server toàn cục và đồng bộ 17 skills mà không cần người dùng can thiệp thủ công.

