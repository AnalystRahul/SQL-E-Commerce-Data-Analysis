
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('../data/orders.db')
cursor = conn.cursor()

# Fetch the daily orders analysis data
query = '''
    SELECT
        DATE(date) AS order_date,
        SUM(successful_orders + fail_orders) AS total_orders
    FROM
        orders
    GROUP BY
        order_date
    ORDER BY
        order_date;
'''
cursor.execute(query)
daily_orders = cursor.fetchall()

# Convert to DataFrame
daily_orders_df = pd.DataFrame(daily_orders, columns=['Order Date', 'Total Orders'])

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(daily_orders_df['Order Date'], daily_orders_df['Total Orders'], marker='o')
plt.title('Daily Orders Analysis')
plt.xlabel('Order Date')
plt.ylabel('Total Orders')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('../results/daily_orders_analysis.png')
plt.show()

# Close connection
conn.close()
