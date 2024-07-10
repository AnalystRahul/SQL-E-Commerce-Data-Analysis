
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('../data/orders.db')
cursor = conn.cursor()

# Fetch the average order size per vendor data
query = '''
    SELECT
        vendor_id,
        AVG(successful_orders + fail_orders) AS avg_order_size
    FROM
        orders
    GROUP BY
        vendor_id
    ORDER BY
        avg_order_size DESC
    LIMIT 10;
'''
cursor.execute(query)
avg_order_size = cursor.fetchall()
avg_order_size_df = pd.DataFrame(avg_order_size, columns=['vendor_id', 'avg_order_size'])

# Plot the data
plt.figure(figsize=(10, 6))
avg_order_size_df.plot(kind='bar', x='vendor_id', y='avg_order_size', title='Average Order Size per Vendor', figsize=(10, 6))
plt.xlabel('Vendor ID')
plt.ylabel('Average Order Size')
plt.savefig('../results/average_order_size_per_vendor.png')
plt.show()

# Fetch the monthly orders trend data
query = '''
    SELECT
        strftime('%Y-%m', date) AS month,
        SUM(successful_orders + fail_orders) AS total_orders
    FROM
        orders
    GROUP BY
        month
    ORDER BY
        month;
'''
cursor.execute(query)
monthly_orders_trend = cursor.fetchall()
monthly_orders_trend_df = pd.DataFrame(monthly_orders_trend, columns=['month', 'total_orders'])

# Plot the data
plt.figure(figsize=(10, 6))
monthly_orders_trend_df.plot(kind='line', x='month', y='total_orders', title='Monthly Orders Trend', figsize=(10, 6), marker='o')
plt.xlabel('Month')
plt.ylabel('Total Orders')
plt.savefig('../results/monthly_orders_trend.png')
plt.show()

# Fetch the top 5 vendors by successful orders in city 23
query = '''
    WITH ranked_vendors AS (
        SELECT
            city_id,
            vendor_id,
            SUM(successful_orders) AS total_successful_orders,
            RANK() OVER (PARTITION BY city_id ORDER BY SUM(successful_orders) DESC) AS rank
        FROM
            orders
        GROUP BY
            city_id, vendor_id
    )
    SELECT
        city_id,
        vendor_id,
        total_successful_orders
    FROM
        ranked_vendors
    WHERE
        rank <= 5
        AND city_id = 23;
'''
cursor.execute(query)
top_vendors_city_23 = cursor.fetchall()
top_vendors_city_23_df = pd.DataFrame(top_vendors_city_23, columns=['city_id', 'vendor_id', 'total_successful_orders'])

# Plot the data
plt.figure(figsize=(10, 6))
top_vendors_city_23_df.plot(kind='bar', x='vendor_id', y='total_successful_orders', title='Top 5 Vendors by Successful Orders in City 23', figsize=(10, 6))
plt.xlabel('Vendor ID')
plt.ylabel('Total Successful Orders')
plt.savefig('../results/top_5_vendors_city_23.png')
plt.show()

# Fetch the order success rate over time data
query = '''
    SELECT
        DATE(date) AS order_date,
        SUM(successful_orders) AS successful_orders,
        SUM(fail_orders) AS failed_orders,
        (SUM(successful_orders) / SUM(successful_orders + fail_orders)) * 100 AS success_rate
    FROM
        orders
    GROUP BY
        order_date
    ORDER BY
        order_date;
'''
cursor.execute(query)
success_rate_over_time = cursor.fetchall()
success_rate_over_time_df = pd.DataFrame(success_rate_over_time, columns=['order_date', 'successful_orders', 'failed_orders', 'success_rate'])

# Plot the data
plt.figure(figsize=(10, 6))
success_rate_over_time_df.plot(kind='line', x='order_date', y='success_rate', title='Order Success Rate Over Time', figsize=(10, 6), marker='o')
plt.xlabel('Order Date')
plt.ylabel('Success Rate (%)')
plt.savefig('../results/order_success_rate_over_time.png')
plt.show()

# Fetch the distribution of orders by food type in city 23
query = '''
    SELECT
        city_id,
        spec AS food_type,
        SUM(successful_orders + fail_orders) AS total_orders
    FROM
        orders
    WHERE
        city_id = 23
    GROUP BY
        city_id, food_type
    ORDER BY
        total_orders DESC;
'''
cursor.execute(query)
orders_distribution_food_type_city_23 = cursor.fetchall()
orders_distribution_food_type_city_23_df = pd.DataFrame(orders_distribution_food_type_city_23, columns=['city_id', 'food_type', 'total_orders'])

# Plot the data
plt.figure(figsize=(10, 6))
orders_distribution_food_type_city_23_df.plot(kind='bar', x='food_type', y='total_orders', title='Distribution of Orders by Food Type in City 23', figsize=(10, 6))
plt.xlabel('Food Type')
plt.ylabel('Total Orders')
plt.savefig('../results/orders_distribution_by_food_type_city_23.png')
plt.show()

# Close connection
conn.close()
