import os
import time
from dotenv import load_dotenv
from telegram import send_telegram_message
from binance_scan import check_binance_breakouts

load_dotenv()

while True:
    try:
        signals = check_binance_breakouts()
        for signal in signals:
            send_telegram_message(signal)
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(60)  # interval za testiranje (1 minuta)
