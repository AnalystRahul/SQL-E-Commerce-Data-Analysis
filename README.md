
# 📊 Comprehensive SQL Analysis Project

## 🌟 Overview

This project involves a detailed analysis of an orders dataset using SQL. The analysis is divided into **initial** and **advanced** segments, each providing valuable insights into vendor performance, order trends, food type popularity, and other key metrics. The results are visualized to aid in understanding and decision-making.

## 📁 Project Structure

```plaintext
sql-project/
├── data/
│   └── orders.csv
├── scripts/
│   ├── load_data.py
│   ├── queries.sql
│   ├── run_queries.py
│   ├── visualize_results.py
│   └── visualize_results_advanced.py
├── results/
│   ├── results.md
│   ├── advanced_results.md
│   ├── average_order_size_per_vendor.png
│   ├── monthly_orders_trend.png
│   ├── top_5_vendors_city_23.png
│   ├── order_success_rate_over_time.png
│   ├── orders_distribution_by_food_type_city_23.png
│   ├── daily_orders_analysis.png
│   └── combined_results.md
├── README.md
└── requirements.txt
```

## 🚀 Setup Instructions

### 1. Clone the Repository

```sh
git clone <repository_url>
cd sql-project
```

### 2. Install Required Packages

```sh
pip install -r requirements.txt
```

### 3. Load Data into SQLite Database

```sh
python scripts/load_data.py
```

### 4. Run SQL Queries

```sh
python scripts/run_queries.py
```

### 5. Visualize Results

#### Initial Queries

```sh
python scripts/visualize_results.py
```

#### Advanced Queries

```sh
python scripts/visualize_results_advanced.py
```

## 📊 Data Description

The data file `orders.csv` should be placed in the `data/` directory. This file contains the following columns:
- **date**: The date of the orders.
- **vendor_id**: The ID of the vendor.
- **chain_id**: The ID of the chain.
- **city_id**: The ID of the city.
- **spec**: The type of food (e.g., Sushi, Pizza).
- **successful_orders**: The number of successful orders.
- **fail_orders**: The number of failed orders.

## 🔍 Key Findings

### Initial SQL Project

#### 1. Total Orders per Vendor

```sql
SELECT
    vendor_id,
    SUM(successful_orders + fail_orders) AS total_orders
FROM
    orders
GROUP BY
    vendor_id;
```

![Total Orders per Vendor](results/daily_orders_analysis.png)

- Vendor ID 3857 had the highest total orders (4,870), followed by Vendor ID 3756 (2,444).

#### 2. Success Rate per Vendor

```sql
SELECT
    vendor_id,
    SUM(successful_orders) AS successful_orders,
    SUM(fail_orders) AS failed_orders,
    (SUM(successful_orders) / SUM(successful_orders + fail_orders)) * 100 AS success_rate
FROM
    orders
GROUP BY
    vendor_id;
```

- Vendor ID 3813 had the highest success rate (98.93%).

#### 3. Orders Over Time

```sql
SELECT
    DATE(date) AS order_date,
    SUM(successful_orders + fail_orders) AS total_orders
FROM
    orders
GROUP BY
    order_date
ORDER BY
    order_date;
```

![Orders Over Time](results/daily_orders_analysis.png)

- Order volumes show clear trends and peaks over time, indicating periods of high demand.

#### 4. City-wise Analysis

```sql
SELECT
    city_id,
    SUM(successful_orders + fail_orders) AS total orders
FROM
    orders
GROUP BY
    city_id;
```

- City ID 23 had the highest total orders (48,059), followed by City ID 25 (24,947).

#### 5. Food Type Popularity

```sql
SELECT
    spec AS food type,
    SUM(successful_orders + fail orders) AS total orders
FROM
    orders
GROUP BY
    spec
ORDER BY
    total orders DESC;
```

- Sushi (2,444 orders) and Russian cuisine (956 orders) were the most popular food types.

