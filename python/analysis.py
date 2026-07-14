import pandas as pd
df=pd.read_csv("data/website_traffic.csv")
print(df.head())
print(df.groupby("TrafficSource")["Users"].sum())
