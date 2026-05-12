import pandas as pd
import sqlite3

df= pd.read_csv('../Data/cleaned_uk_housing_data.csv')

conn = sqlite3.connect('housing_analysis.db')

df.to_sql('propert_prices',conn , if_exists='replace',index=False)

print("Data in sql!")
conn.close()