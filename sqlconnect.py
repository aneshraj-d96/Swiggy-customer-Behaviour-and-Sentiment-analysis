import pandas as pd
import mysql.connector
from datetime import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root_",
    database="projects"
)

cursor = conn.cursor()

# Load CSV
df = pd.read_csv("restaurant_orders.csv")

# Convert Order_Date to datetime format
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS restaurant_orders (
        Customer_ID VARCHAR(50),
        Order_Date DATETIME,
        Restaurant_Name VARCHAR(255),
        Area VARCHAR(255),
        Cuisine_Type VARCHAR(100),
        Order_Value FLOAT,
        Delivery_Time_Min INT,
        Delivery_Rating INT,
        Food_Rating INT,
        Payment_Method VARCHAR(50),
        Customer_Age INT,
        Customer_Gender VARCHAR(10),
        Sentiment VARCHAR(50),
        City VARCHAR(100)
    )
""")

# Insert data row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO restaurant_orders (
            Customer_ID, Order_Date, Restaurant_Name, Area, Cuisine_Type,
            Order_Value, Delivery_Time_Min, Delivery_Rating, Food_Rating,
            Payment_Method, Customer_Age, Customer_Gender, Sentiment, City
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['Customer_ID'],
        row['Order_Date'].to_pydatetime() if pd.notnull(row['Order_Date']) else None,
        row['Restaurant_Name'],
        row['Area'],
        row['Cuisine_Type'],
        float(row['Order_Value']),
        int(row['Delivery_Time_Min']),
        int(row['Delivery_Rating']),
        int(row['Food_Rating']),
        row['Payment_Method'],
        int(row['Customer_Age']),
        row['Customer_Gender'],
        row['Sentiment'],
        row['City']
    ))

conn.commit()
print("Restaurant order data imported successfully!")
