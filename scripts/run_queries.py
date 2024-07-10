
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('../data/orders.db')
cursor = conn.cursor()

# Read SQL queries from file
with open('queries.sql', 'r') as file:
    sql_queries = file.read()

# Split queries by semicolon
queries = sql_queries.strip().split(';')

# Execute queries and save results
results = {}
for i, query in enumerate(queries):
    if query.strip():
        cursor.execute(query)
        results[f'Query_{i+1}'] = cursor.fetchall()

# Close connection
conn.close()

# Save results to a markdown file
with open('../results/results.md', 'w') as file:
    for query_name, result in results.items():
        file.write(f'## {query_name}\n\n')
        for row in result:
            file.write(f'{row}\n')
        file.write('\n')
