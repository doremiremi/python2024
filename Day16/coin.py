import ccxt


exchange = ccxt.binance()
ticker = exchange.fetch_ticker('BTC/USD')
current_price = ticker['last']
prev_price = current_price

while True:
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('BTC/USD')
    current_price = ticker['last']
    print(f"현재가격:{current_price}")
    if prev_price - current_price > 0:
        print("돔황챠")
    else:
        print("오뎅하나 추가")
    print(f"BCT/USD 현재 가격:{current_price}")

