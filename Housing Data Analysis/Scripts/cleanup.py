import pandas as pd

#1. load the data
df = pd.read_csv('../Data/UK-HPI-full-file-2024-02.csv')

#2. Filtering for relavent columns
columns_to_keep= [
    'Date','RegionName','AreaCode','AveragePrice','Index','DetachedPrice','SemiDetachedPrice','TerracedPrice','FlatPrice'
]
df_clean=df[columns_to_keep].copy()

#3. Column name cleanup
df_clean.columns=[col.lower().replace(' ','_') for col in df_clean.columns]

#4. Missing value handeling 
df_clean=df_clean.dropna(subset=['averageprice'])

#5. Date conversion
df_clean['date']=pd.to_datetime(df_clean['date'])

df_clean.to_csv('../Data/cleaned_uk_housing_data.csv', index=False)

print("Data cleaned!")