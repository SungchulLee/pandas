import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

def custom_resampler(arraylike):
    data = np.array(arraylike)
    weight = np.array([0.0,0.1,0.2,0.3,0.4])[-len(data):]
    weight = weight / weight.sum()
    return np.sum( data * weight )

def main():
    df = yf.Ticker("AAPL").history(start="2024-01-01",end="2024-12-31")
    dg = df.Close.resample(rule='5d', label='right', origin="end").apply(custom_resampler)
    print(df.Close.head())
    print(dg.head())
    
    _, ax = plt.subplots(figsize=(12,3))
    ax.plot(df.index,df.Close,label="close")
    ax.plot(dg.index,dg,label="5d_avg")
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()