import numpy as np
import pandas as pd
df=pd.read_csv("/Users/KC/Desktop/Henry Harvin/pywork/pyprojects/pyanalytics/Denco Corp/denco.csv")
df
df.size
df.shape
df.describe
df.columns
df0=df
df0.columns
df0.revenue
df0.groupby('revenue')
df0.groupby('revenue').size()
df0.groupby('revenue').describe()
