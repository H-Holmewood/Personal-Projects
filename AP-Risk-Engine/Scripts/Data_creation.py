import pandas as pd
import random
from faker import Faker 

fake = Faker('en_GB')
data=[]

for i in range(500):
    amount=round(random.uniform(10.0,5000.0),2)
    data.append({
        "InvoiceID":i,
        "SupplierID":random.randint(5001,5050),
         "InvoiceNumber":fake.bothify(text='INV-####??'),
         "Amount":amount,
         "Date":fake.date_between(start_date='-1y',end_date='today'),
         "Channel":random.choice(['EDI','Portal','Email','Paper']),
         "Status":random.choice(['paid','Pending','Flagged']),
         "Dept": random.choice(['Logistics','Marketihng','IT','Operations'])

    })

df=pd.DataFrame(data)
df.to_csv('AP_Audit_Data.csv',index=False)