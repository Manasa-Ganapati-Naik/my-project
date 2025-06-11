import pandas as pd
import numpy as np
file = r"C:\Users\manas\OneDrive\Documents\Legal ML.xlsx"

df= pd.read_excel(file)
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())