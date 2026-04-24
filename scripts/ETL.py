import pandas as pd
from sqlalchemy import create_engine

#Load csv files
orders_df = pd.read_csv("E-Commerce ETL\data\orders.csv")
products_df = pd.read_csv("E-Commerce ETL\data\products.csv")

#Inspect files
# print(orders_df.head())
# print(orders_df.info())
# print(products_df.head())
# print(products_df.info())

#------------------------------
# CLEANING 
#------------------------------

#Standarize column names
orders_df.columns = orders_df.columns.str.strip().str.lower()
products_df.columns = products_df.columns.str.strip().str.lower()

#Clean both dataframes
orders_df = orders_df.drop_duplicates()
orders_df = orders_df.dropna()
products_df = products_df.drop_duplicates()
products_df = products_df.dropna()

#convert date type from object to datetime
orders_df['order_date'] = pd.to_datetime(orders_df["order_date"])

#----------------------------
# VALIDATION
#----------------------------

#Check if products_id in orders exists in products
missing_products = orders_df[~orders_df['product_id'].isin(products_df['product_id'])]

#Validate if products didn't match
print(orders_df['product_id'].isnull().sum())

#Create total price column
orders_df['total_price'] = orders_df['qty'] * orders_df['unit_price']

# print(orders_df.columns.tolist())
#Remove invalid rows
orders_df = orders_df[orders_df['product_id'].isin(products_df['product_id'])]
#-------------------------
# LOAD DATA
#-------------------------

#Create link postgre and python
engine = create_engine("postgresql://postgres:password@localhost:5432/E-Commerce")
print("Loading products...")
products_df.to_sql('products', engine, if_exists='append', index=False)

print("Loading orders...")
orders_df.to_sql('orders', engine, if_exists='append', index=False)
print("Done.")