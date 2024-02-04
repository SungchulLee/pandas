import matplotlib.pyplot as plt
import yfinance as yf

def main():
    df = yf.Ticker("AAPL").history(start="2024-01-01",end="2024-12-31")
    dg = df.Close.resample(rule='5d', label='right', origin="end").mean()
    print(df.Close.head())
    print(dg.head())
    
    _, ax = plt.subplots(figsize=(12,3))
    ax.plot(df.index,df.Close,label="close")
    ax.plot(dg.index,dg,label="5d_avg")
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()