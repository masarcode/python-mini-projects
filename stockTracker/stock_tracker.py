import yfinance as yf

def format_market_cap(value):
    if value is None:
        return "N/A"
    if value >= 1_000_000_000_000:
            return f"${value / 1_000_000_000_000:.2f}T"
    elif value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    elif value >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"
    else:
        return f"${value:,}"

def track_stock(ticker_symbol):
    print(f"Fetching data for ${ticker_symbol.upper()}...")

    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info

        price = info.get("currentPrice") or info.get("regularMarketPrice")
        high = info.get("dayHigh")
        low = info.get("dayLow")
        market_cap = info.get("marketCap")
        forward_pe = info.get("forwardPE")
        dividend_yield = info.get("dividendYield")

        print(f"\n--- {info.get('shortName', 'Unknown Company')} ({ticker_symbol.upper()}) ---")
        print(f"Current Price: ${price:.2f}" if price else "Current Price: N/A")
        print(f"Day High: ${high:.2f}" if high else "Day High: N/A")
        print(f"Day Low: ${low:.2f}" if low else "Day Low: N/A")
        print(f"Market Cap: {format_market_cap(market_cap)}")
        print(f"Forward P/E: {forward_pe:.2f}" if forward_pe else "Forward P/E: N/A")
        if dividend_yield:
            if dividend_yield < 0.01:
                print(f"Dividend Yield: {dividend_yield * 100:.3f}%")
            else:
                print(f"Dividend Yield: {dividend_yield:.2f}%")
        else:
            print("Dividend Yield: None")

    except Exception as e:
        print("Could not fetch stock data.")
        print("Error:", e)

symbol = input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT): ")
track_stock(symbol)