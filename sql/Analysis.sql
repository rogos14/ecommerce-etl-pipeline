-- Revenue by category
SELECT 
	p.category,
	SUM(o.total_price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;


-- Revenue by category monthly
SELECT 
	DATE_TRUNC('month', o.order_date) AS month,
	p.category, 
	SUM(o.total_price) AS revenue
FROM orders o
JOIN products p on o.product_id = p.product_id
GROUP BY month, p.category
ORDER BY month;

--Top sold products
SELECT 
	p.product_name,
	SUM(o.total_price) as revenue,
	SUM(o.qty) as total_units_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_units_sold DESC
LIMIT 10