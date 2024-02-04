import yfinance as yf

def main():
    df = yf.Ticker("AAPL").history(start="2023-01-01",end="2024-12-31")
    print(f"{df.tail() = }")
    print(f"{df.tail(3) = }")

if __name__ == "__main__":
    main()