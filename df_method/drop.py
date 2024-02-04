import pandas as pd
import yfinance as yf

def main():
    df = yf.Ticker('SPY').history(start='2023-01-01',end='2024-12-31')
    df.drop(columns=['High', 'Low', 'Volume', 'Dividends', 'Stock Splits'], inplace=True)
    #df.drop(['High', 'Low', 'Volume', 'Dividends', 'Stock Splits'], axis=1, inplace=True)
    print(df.head())

if __name__ == "__main__":
    main()