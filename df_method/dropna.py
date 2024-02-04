import numpy as np
import pandas as pd

def main():
    df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                       "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                       "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT]})
    print(df.head())

    if 1:
        df.dropna(axis=1, inplace=True) # Drop Column or Columns
    elif 1:
        df.dropna(axis=0, inplace=True) # Drop Index or Indices (Default)
    elif 1:
        df.dropna(inplace=True) # Drop Index or Indices (Default)
    print(df.head())

if __name__ == "__main__":
    main()