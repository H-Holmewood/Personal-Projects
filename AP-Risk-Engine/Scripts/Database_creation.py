import sqlite3
import pandas as pd

# Load your generated data
df = pd.DataFrame(pd.read_csv('AP_Audit_Data.csv'))

# Create/Connect to the database
conn = sqlite3.connect('AP_Operations.db')

# Write the data to a table
df.to_sql('Raw_Invoices', conn, if_exists='replace', index=False)

print("Database 'AP_Operations.db' created successfully!")
conn.close()