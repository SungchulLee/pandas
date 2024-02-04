import matplotlib.pyplot as plt
import yfinance as yf

def main():
    df = yf.Ticker("AAPL").history(start="2024-01-01",end="2024-12-31")
    dg = df.Close.resample(rule='5d', label='right', origin="end").mean()
    dh = df.Close.rolling(5).mean()
    print(df.Close.head())
    print(dg.head())
    
    _, ax = plt.subplots(figsize=(12,3))
    ax.plot(df.index,df.Close,label="close")
    ax.plot(dg.index,dg,label="5d_avg_resample")
    ax.plot(dh.index,dh,label="5d_avg_rolling")
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()