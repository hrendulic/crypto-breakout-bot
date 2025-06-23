import requests

def check_binance_breakouts():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    exchange_info_url = "https://api.binance.com/api/v3/exchangeInfo"
    result = []

    symbols = [
        s["symbol"] for s in requests.get(exchange_info_url).json()["symbols"]
        if s["quoteAsset"] == "USDT" and s["status"] == "TRADING"
    ]

    data = requests.get(url).json()
    for coin in data:
        if coin["symbol"] not in symbols:
            continue
        try:
            price_change = float(coin["priceChangePercent"])
            volume = float(coin["quoteVolume"])
            if 5 <= price_change <= 15 and volume > 1000000:
                result.append(
                    f"🔥 {coin['symbol']} breakout signal: {price_change:.2f}% in 24h. Volume: {volume:.0f} USDT"
                )
        except:
            continue
    return result
