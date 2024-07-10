
-- Total Orders per Vendor
SELECT
    vendor_id,
    SUM(successful_orders + fail_orders) AS total_orders
FROM
    orders
GROUP BY
    vendor_id;

-- Success Rate per Vendor
SELECT
    vendor_id,
    SUM(successful_orders) AS successful_orders,
    SUM(fail_orders) AS failed_orders,
    (SUM(successful_orders) / SUM(successful_orders + fail_orders)) * 100 AS success_rate
FROM
    orders
GROUP BY
    vendor_id;

-- Orders Over Time
SELECT
    DATE(date) AS order_date,
    SUM(successful_orders + fail_orders) AS total_orders
FROM
    orders
GROUP BY
    order_date
ORDER BY
    order_date;

-- City-wise Analysis
SELECT
    city_id,
    SUM(successful_orders + fail_orders) AS total_orders
FROM
    orders
GROUP BY
    city_id;

-- Food Type Popularity
SELECT
    spec AS food_type,
    SUM(successful_orders + fail_orders) AS total_orders
FROM
    orders
GROUP BY
    spec
ORDER BY
    total_orders DESC;

-- Daily Orders Analysis
SELECT
    DATE(date) AS order_date,
    SUM(successful_orders + fail_orders) AS total_orders
FROM
    orders
GROUP BY
    order_date
ORDER BY
    order_date;

-- Success Rate by City
SELECT
    city_id,
    SUM(successful_orders) AS successful_orders,
    SUM(fail_orders) AS failed_orders,
    (SUM(successful_orders) / SUM(successful_orders + fail_orders)) * 100 AS success_rate
FROM
    orders
GROUP BY
    city_id
ORDER BY
    success_rate DESC;

-- Vendor-wise Food Type Popularity
SELECT
    vendor_id,
    spec AS food_type,
    SUM(successful_orders + fail_orders) AS total_orders
FROM
    orders
GROUP BY
    vendor_id, spec
ORDER BY
    vendor_id, total_orders DESC;

-- Chain Performance Over Time
SELECT
    chain_id,
    DATE(date) AS order_date,
    SUM(successful_orders + fail_orders) AS total_orders
FROM
    orders
GROUP BY
    chain_id, order_date
ORDER BY
    chain_id, order_date;

-- Impact of Date on Order Success
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


-- Average Order Size per Vendor
SELECT
    vendor_id,
    AVG(successful_orders + fail_orders) AS avg_order_size
FROM
    orders
GROUP BY
    vendor_id
ORDER BY
    avg_order_size DESC;

-- Monthly Orders Trend
SELECT
    strftime('%Y-%m', date) AS month,
    SUM(successful_orders + fail_orders) AS total_orders
FROM
    orders
GROUP BY
    month
ORDER BY
    month;

-- Top 5 Vendors by Successful Orders in Each City
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
    rank <= 5;

-- Order Success Rate Over Time
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

-- Distribution of Orders by Food Type and City
SELECT
    city_id,
    spec AS food_type,
    SUM(successful_orders + fail_orders) AS total_orders
FROM
    orders
GROUP BY
    city_id, food_type
ORDER BY
    city_id, total_orders DESC;
