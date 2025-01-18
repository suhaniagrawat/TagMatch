import sqlite3
import pandas as pd

# Connect to SQLite (it will create a new database if it doesn't exist)
conn = sqlite3.connect('database.db', timeout=10)  # Timeout set to 10 seconds
cursor = conn.cursor()

# List of CSV files
csv_files = ['mobilephones_data_site1.csv', 'mobilephones_data_site2.csv', 'laptops_data_site1.csv', 'laptops_data_site2.csv']

for csv_file in csv_files:
    # Read CSV file into DataFrame
    df = pd.read_csv(csv_file)

    # Convert DataFrame to SQL table
    table_name = csv_file.split('.')[0]  # Use the file name (without extension) as table name
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()
