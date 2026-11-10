# -*- coding: utf-8 -*-
"""
[Update: 11/11/2026 01:48] Hỗ trợ chia nhỏ tin nhắn tự động khi gửi báo cáo dài đầy đủ, cấm cắt xén.
Kênh thông báo Telegram tự động 24/7 của EVO Assistant (EA) & Hạm Đội Agent.
Gửi báo cáo tiến độ, mốc hoàn thành và cảnh báo trực tiếp về Telegram của Sếp TOM qua bot @tcmPJmanager_bot.
"""
import sys
import os
import json
import time
import urllib.request
import urllib.error

# Khắc phục triệt để lỗi mã hóa tiếng Việt trên Windows Console (cp1252)
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Thông số chuẩn của EVO Assistant Bot (@tcmPJmanager_bot) & Sếp TOM (Lê Thành)
BOT_TOKEN_TCM_MANAGER = "8811827454:AAFRtgwWMCPv3vVt1y1iUdyXJ4wMDlzVZm8"
DEFAULT_CHAT_ID = "5888492139"

def get_config():
    token = os.environ.get("EVO_TELEGRAM_BOT_TOKEN", "").strip() or BOT_TOKEN_TCM_MANAGER
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip() or DEFAULT_CHAT_ID
    return token, chat_id

def split_message(text, max_len=3800):
    """Chia nhỏ tin nhắn an toàn để không vượt giới hạn 4096 ký tự của Telegram."""
    text = text.strip()
    if len(text) <= max_len:
        return [text]

    chunks = []
    remaining = text
    while len(remaining) > max_len:
        split_idx = remaining.rfind('\n', 0, max_len)
        if split_idx == -1 or split_idx < max_len // 2:
            split_idx = remaining.rfind(' ', 0, max_len)
        if split_idx == -1:
            split_idx = max_len
        chunks.append(remaining[:split_idx].strip())
        remaining = remaining[split_idx:].strip()
    if remaining:
        chunks.append(remaining)
    return chunks

def _send_single(chunk, parse_mode="HTML"):
    token, chat_id = get_config()
    if not token or not chat_id:
        print("[Telegram Notify Error] Chưa cấu hình TELEGRAM_BOT_TOKEN hoặc TELEGRAM_CHAT_ID")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": chunk,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            res_body = response.read().decode("utf-8")
            res_json = json.loads(res_body)
            if res_json.get("ok"):
                print("[Telegram Notify @tcmPJmanager_bot] Gửi thành công!")
                return True
            else:
                print(f"[Telegram Notify Error] API response: {res_body}")
                return False
    except urllib.error.HTTPError as e:
        if e.code == 400 and parse_mode:
            payload.pop("parse_mode", None)
            data_fb = json.dumps(payload).encode("utf-8")
            req_fb = urllib.request.Request(url, data=data_fb, headers={"Content-Type": "application/json"})
            try:
                with urllib.request.urlopen(req_fb, timeout=15) as fb_resp:
                    if json.loads(fb_resp.read().decode("utf-8")).get("ok"):
                        print("[Telegram Notify @tcmPJmanager_bot] Gửi thành công (Fallback PlainText)!")
                        return True
            except Exception:
                pass
        print(f"[Telegram Notify Exception] Lỗi kết nối Telegram: {e}")
        return False
    except Exception as e:
        print(f"[Telegram Notify Exception] Lỗi kết nối Telegram: {e}")
        return False

def send_telegram(message, parse_mode="HTML"):
    chunks = split_message(message)
    total = len(chunks)
    all_ok = True
    for i, c in enumerate(chunks, 1):
        if total > 1:
            prefix = f"<b>[Phần {i}/{total}]</b>\n" if parse_mode == "HTML" else f"[{i}/{total}]\n"
            chunk_to_send = prefix + c
        else:
            chunk_to_send = c
        ok = _send_single(chunk_to_send, parse_mode=parse_mode)
        if not ok:
            all_ok = False
        if total > 1 and i < total:
            time.sleep(0.5)
    return all_ok

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--file":
        filepath = sys.argv[2]
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                msg = f.read()
        else:
            msg = f"[Lỗi] Không tìm thấy file báo cáo: {filepath}"
    elif len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
    elif not sys.stdin.isatty():
        msg = sys.stdin.read()
    else:
        msg = "🔔 <b>EVO Assistant</b>: Kiểm tra tín hiệu kết nối bot @tcmPJmanager_bot."
    send_telegram(msg)
