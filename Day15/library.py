import yfinance

apple = yfinance.Ticker("AAPL")
current_price = apple.info['currentPrice']
print(f"애플주식의 현재가격:{current_price}")