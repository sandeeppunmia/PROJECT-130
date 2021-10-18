import pandas as pd
import csv

df=pd.read_csv("total_stars.csv")
print(df.shape)

del df["Luminosity"]
del df["Star_name2"]
del df["Mass2"]
del df["Radius2"]
del df["Distance2"]
df=df[df['Radius'].notna()]
df=df[df['Mass'].notna()]
df=df[df['Distance'].notna()]
print(df.shape)

df.to_csv('final.csv')
