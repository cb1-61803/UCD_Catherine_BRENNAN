import pandas as pd

file = 'TABLE1_27012021182954715.csv'

df = pd.read_csv(file)

print(df.head())

