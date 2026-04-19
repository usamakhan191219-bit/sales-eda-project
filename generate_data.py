import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed so results are the same every time
np.random.seed(42)

# Create date range (1 year of sales)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Generate 5000 random sales records
num_records = 5000

data = {
    'Order_ID': range(1, num_records + 1),
    'Order_Date': np.random.choice(dates, num_records),
    'State': np.random.choice(['California', 'Texas', 'New York', 'Florida', 'Illinois'], num_records),
    'Gender': np.random.choice(['Male', 'Female'], num_records),
    'Age': np.random.randint(18, 70, num_records),
    'Product_Category': np.random.choice(['Electronics', 'Clothing', 'Furniture', 'Books', 'Toys'], num_records),
    'Quantity': np.random.randint(1, 10, num_records),
    'Unit_Price': np.random.uniform(10, 500, num_records),
    'Customer_Satisfaction': np.random.randint(1, 6, num_records)  # 1 to 5 stars
}

df = pd.DataFrame(data)

# Calculate Total_Price = Quantity * Unit_Price
df['Total_Price'] = df['Quantity'] * df['Unit_Price']

# Round to 2 decimals
df['Unit_Price'] = df['Unit_Price'].round(2)
df['Total_Price'] = df['Total_Price'].round(2)

# Save to CSV
df.to_csv('sales_data.csv', index=False)

print("✅ sales_data.csv created successfully!")
print(f"📊 Total records: {len(df)}")
print(df.head())