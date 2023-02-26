import csv
import random
from datetime import datetime, timedelta

# Define the list of SKU values and the number of SKU columns
sku_list = ['SKU1', 'SKU2', 'SKU3']
num_sku_cols = len(sku_list)

# Define the number of rows to generate
num_rows = 200

# Open the output CSV file for writing
with open('output.csv', 'w', newline='') as csvfile:
    # Define the CSV writer and write the header row
    writer = csv.writer(csvfile)
    header_row = ['Store_ID', 'Transaction_Date']
    for i in range(num_sku_cols):
        header_row.extend([sku_list[i] + '_Quantity', sku_list[i] + '_UnitCost'])
    writer.writerow(header_row)

    # Generate random data and write to the CSV file
    for row_num in range(num_rows):
        # Generate Store_ID and Transaction_Date
        store_id = random.randint(1, 10)
        #SKU = 'B' +str(random.randint(100000, 999999))
        
        transaction_date = datetime.now() - timedelta(days=random.randint(0, 365))

        # Generate SKU data for each SKU column
        sku_data = []
        for i in range(num_sku_cols):
            quantity = random.randint(1, 10)
            unit_cost = int(random.uniform(100, 500))
            SKU = 'B' +str(random.randint(100000, 999999))
            sku_data.extend([SKU, quantity, unit_cost])

        # Write the row to the CSV file
        writer.writerow([str(store_id), transaction_date.strftime('%Y-%m-%d')] + sku_data)