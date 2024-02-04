import matplotlib.pyplot as plt
import yfinance as yf

def main():
    df = yf.Ticker("AAPL").history(start="2024-01-01",end="2024-12-31")
    print(df.mean())

if __name__ == "__main__":
    main()