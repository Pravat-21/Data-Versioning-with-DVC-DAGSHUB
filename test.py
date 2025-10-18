import pandas as pd
import numpy as np

df=pd.read_csv("https://raw.githubusercontent.com/Pravat-21/DATASET-24/refs/heads/main/sample-csv/addresses.csv")
print(df.head(3))

df.drop(columns=['state_province','country'],inplace=True)
print(df.head(3))

df.to_csv("data/raw_1.csv")