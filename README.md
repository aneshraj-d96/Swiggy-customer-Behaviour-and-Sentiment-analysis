# 🍽️ Swiggy Customer Behaviour and Sentiment Analysis

An interactive analytics platform built to explore customer behavior, delivery performance, and sentiment trends across Bangalore's food delivery ecosystem. This project analyzes 200K+ orders to uncover insights on cuisine preferences, delivery ratings, payment methods, and customer sentiment.

---

## 🧠 Project Overview

Understanding customer behavior is key to improving service quality and retention. This project analyzes Swiggy order data to identify patterns in delivery time, food ratings, payment preferences, and sentiment across demographics and locations.

### 🔍 Key Objectives
- Clean and preprocess customer order data  
- Analyze sentiment and behavioral patterns  
- Build predictive models for delivery satisfaction  
- Deploy interactive dashboard and presentation for stakeholder insights  

---

## 📁 Project Structure

| File Name                                               | Description                                                                 |
|----------------------------------------------------------|-----------------------------------------------------------------------------|
| `swiggy_data.csv`                                        | Raw dataset with 200K+ customer orders                                      |
| `cleaned_swiggy.csv`                                     | Preprocessed dataset with engineered features                              |
| `rf_model.pkl`                                           | Trained Random Forest model for delivery rating prediction                 |
| `swiggy.sql`                                             | SQL queries for filtering and aggregating customer data                    |
| `sqlconnect.py`                                          | Python script for SQL database connection                                  |
| `app.py`                                                 | Streamlit app for dashboard deployment                                     |
| `swiggy customer behaviour and sentiment analysis.ipynb` | Jupyter notebook with EDA, modeling, and insights                          |
| `swiggy customer behaviour and sentiment analysis.pbix`  | PowerBI summarizing findings and business impact           |

---

## 🧹 Data Preprocessing

- Converted `Order_Date` to datetime format  
- Extracted time-based features (hour, day, month)  
- Encoded categorical variables (`Cuisine_Type`, `Payment_Method`, `Sentiment`, `Gender`)  
- Removed duplicates and handled missing values  
- Normalized `Order_Value` and `Delivery_Time_Min` for modeling  

---

## 📈 Exploratory Data Analysis

- Cuisine popularity across Bangalore areas  
- Delivery time distribution by age and gender  
- Sentiment trends by payment method and food rating  
- Correlation between delivery rating and customer satisfaction  
- Time-of-day impact on delivery performance  

---

## 🤖 Modeling Approach

- **Target Variable**: `Delivery_Rating`  
- **Algorithms Used**: Random Forest, Logistic Regression  
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1 Score  
- **Feature Importance**: `Delivery_Time_Min`, `Order_Value`, `Cuisine_Type`, `Sentiment`, `Customer_Age`  

---

## 📊 Dashboard Overview

Built using **Streamlit**, the dashboard includes:

- 📍 Area-wise cuisine preferences  
- 🕒 Delivery time and rating analysis  
- 💳 Payment method trends  
- 😊 Sentiment distribution across demographics  
- 📊 Predictive insights on delivery satisfaction  

> _Add your hosted dashboard screenshot or link here once available._

---

## 🚀 Deployment

- Model serialized with `joblib` as `rf_model.pkl`  
- Dashboard deployed via **Streamlit Cloud**  
- SQL integration for dynamic customer filtering  
- Presentation deck created in PowerPoint for stakeholder review  

---

## 🧠 Business Impact

- Identifies key drivers of customer satisfaction  
- Helps optimize delivery operations and service quality  
- Supports targeted marketing based on sentiment and behavior  
- Enables data-driven decisions for restaurant partnerships  

---

## 🛠️ Tech Stack

- **Python**: Pandas, NumPy, Scikit-learn, Streamlit  
- **SQL**: Data extraction and filtering  
- **Visualization**: Matplotlib, Seaborn, Plotly  
- **Deployment**: Streamlit Cloud, GitHub  
- **Bussiness visualization**:PowerBI  

---

## 📌 Future Enhancements

- Integrate real-time order tracking and feedback  
- Add NLP-based sentiment scoring from reviews  
- Enable geospatial mapping of delivery hotspots  
- Expand dashboard to include loyalty and churn metrics  

---

## 👤 Author

**Anesh Raj**  
Data Analyst | Data Scientist | Business Analyst  
Focused on multi-industry impact through predictive modeling and dashboarding.  
📍 Chennai, India
