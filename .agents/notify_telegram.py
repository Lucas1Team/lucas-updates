# -*- coding: utf-8 -*-
"""
Kênh thông báo Telegram tự động 24/7 của EVO Assistant (EA) & Hạm Đội Agent.
Gửi báo cáo tiến độ, mốc hoàn thành và cảnh báo trực tiếp về Telegram của Sếp TOM qua bot @tcmPJmanager_bot.
"""
import sys
import os
import json
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

def send_telegram(message, parse_mode="HTML"):
    token, chat_id = get_config()
    if not token or not chat_id:
        print("[Telegram Notify Error] Chưa cấu hình TELEGRAM_BOT_TOKEN hoặc TELEGRAM_CHAT_ID")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
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
                with urllib.request.urlopen(req_fb, timeout=10) as fb_resp:
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

if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
    else:
        msg = "🔔 <b>EVO Assistant</b>: Kiểm tra tín hiệu kết nối bot @tcmPJmanager_bot."
    send_telegram(msg)
