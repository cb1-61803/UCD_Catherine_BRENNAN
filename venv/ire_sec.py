import pandas as pd

file = 'Tvenv/sector_year_ire.csv'

df = pd.read_csv(file)

print(df.head())