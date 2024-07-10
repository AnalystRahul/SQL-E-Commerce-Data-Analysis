
import sqlite3
import pandas as pd

# Load data
orders_df = pd.read_csv('../data/orders.csv')

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('../data/orders.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    date TEXT,
    vendor_id INTEGER,
    chain_id INTEGER,
    city_id INTEGER,
    spec TEXT,
    successful_orders REAL,
    fail_orders REAL
)
''')

# Insert data into table
orders_df.to_sql('orders', conn, if_exists='replace', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()
