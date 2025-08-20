#  Data Analyst Queries


# 1. Average Delivery Time by City
SELECT City, AVG(Delivery_Time_Min) AS Avg_Delivery_Time
FROM restaurant_orders
GROUP BY City
ORDER BY Avg_Delivery_Time DESC;

# 2. Distribution of Ratings
SELECT Delivery_Rating, COUNT(*) AS Delivery_Count,
       Food_Rating, COUNT(*) AS Food_Count
FROM restaurant_orders
GROUP BY Delivery_Rating, Food_Rating;

# 3. Most Common Cuisine Types
SELECT Cuisine_Type, COUNT(*) AS Total_Orders
FROM restaurant_orders
GROUP BY Cuisine_Type
ORDER BY Total_Orders DESC
LIMIT 10;

# 4. Delivery Time vs. Ratings Correlation
SELECT Delivery_Time_Min, AVG(Delivery_Rating) AS Avg_Delivery_Rating
FROM restaurant_orders
GROUP BY Delivery_Time_Min
ORDER BY Delivery_Time_Min;

# 5. Null or Anomalous Data Check
SELECT *
FROM restaurant_orders
WHERE Order_Value <= 0 OR Delivery_Time_Min <= 0;


#  Business Analyst Queries


# 6. Total Revenue by City
SELECT City, SUM(Order_Value) AS Total_Revenue
FROM restaurant_orders
GROUP BY City
ORDER BY Total_Revenue DESC;

# 7. Top Performing Restaurants
SELECT Restaurant_Name, SUM(Order_Value) AS Revenue, AVG(Food_Rating) AS Avg_Food_Rating
FROM restaurant_orders
GROUP BY Restaurant_Name
ORDER BY Revenue DESC
LIMIT 10;

# 8. Customer Age Segmentation
SELECT 
  CASE 
    WHEN Customer_Age < 20 THEN 'Teen'
    WHEN Customer_Age BETWEEN 20 AND 35 THEN 'Young Adult'
    WHEN Customer_Age BETWEEN 36 AND 50 THEN 'Adult'
    ELSE 'Senior'
  END AS Age_Group,
  COUNT(*) AS Total_Customers
FROM restaurant_orders
GROUP BY Age_Group;

# 9. Sentiment Analysis by City
SELECT City, Sentiment, COUNT(*) AS Sentiment_Count
FROM restaurant_orders
GROUP BY City, Sentiment
ORDER BY City, Sentiment_Count DESC;

# 10. Payment Method Preferences
SELECT Payment_Method, COUNT(*) AS Usage_Count
FROM restaurant_orders
GROUP BY Payment_Method
ORDER BY Usage_Count DESC;

# 11. Gender-Based Spending Patterns
SELECT Customer_Gender, AVG(Order_Value) AS Avg_Spend
FROM restaurant_orders
GROUP BY Customer_Gender;
