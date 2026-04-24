DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;

CREATE TABLE products(
	product_id INT PRIMARY KEY,
	product_name TEXT,
	category TEXT
);

CREATE TABLE orders(
	order_id TEXT, 
	order_date TIMESTAMP,
	customer_id TEXT,
	product_id INT REFERENCES products(product_id),
	qty INT, 
	unit_price NUMERIC,
	currency TEXT,
	total_price NUMERIC
);