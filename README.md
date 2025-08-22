# 🍽️ Swiggy Customer Behaviour and Sentiment Analysis

A full-stack analytics solution designed to explore customer behavior, delivery performance, and sentiment trends across Bangalore’s food delivery ecosystem. This project analyzes **200,000+ orders** to uncover insights on cuisine preferences, delivery ratings, payment methods, and customer sentiment—empowering operations teams and marketing strategists with predictive insights and interactive dashboards.

---

## 🚗 GitHub Project Repository  
🔗 [Click to view Swiggy-customer-Behaviour-and-Sentiment-analysis](https://github.com/aneshraj-d96/Swiggy-customer-Behaviour-and-Sentiment-analysis)

---

## 🧠 Project Overview

Customer satisfaction in food delivery hinges on speed, quality, and experience. This project delivers an end-to-end analytics platform that enables:

- 📊 Behavioral analysis across demographics and locations  
- 😊 Sentiment tracking and prediction  
- 🕒 Delivery performance benchmarking  
- 📍 Cuisine and payment preference mapping  

---

## 🎯 Key Objectives

- Clean and preprocess customer order data  
- Engineer features for delivery satisfaction modeling  
- Build classification models to predict delivery ratings  
- Deploy interactive dashboards for stakeholder decision-making  

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
| `swiggy customer behaviour and sentiment analysis.pbix`  | Power BI dashboard visualizing customer trends and satisfaction metrics    |

---

## 🧹 Data Preprocessing

- Converted `Order_Date` to datetime format  
- Extracted time-based features (`hour`, `day`, `month`)  
- Encoded categorical variables (`Cuisine_Type`, `Payment_Method`, `Sentiment`, `Gender`)  
- Removed duplicates and handled missing values  
- Normalized `Order_Value` and `Delivery_Time_Min` for modeling  

---

## 📈 Exploratory Data Analysis

- 📍 Cuisine popularity across Bangalore areas  
- 🕒 Delivery time distribution by age and gender  
- 💳 Sentiment trends by payment method and food rating  
- 😊 Correlation between delivery rating and customer satisfaction  
- 📅 Time-of-day impact on delivery performance  

---

## 🤖 Modeling Approach

- **Target Variable**: `Delivery_Rating`  
- **Algorithms Used**: Random Forest, Logistic Regression  
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1 Score  
- **Top Features**: `Delivery_Time_Min`, `Order_Value`, `Cuisine_Type`, `Sentiment`, `Customer_Age`  

---

## 📊 Dashboard Overview

### 🔷 Power BI Dashboard  
Visualizes customer behavior and delivery performance:

- 📊 Cuisine preference by area  
- ⏱️ Delivery time and rating analysis  
- 💳 Payment method trends  
- 😊 Sentiment distribution across demographics  
- 📅 Monthly order volume and satisfaction metrics  

![Power BI Preview](https://image2url.com/images/1755863744561-f7938bc8-a62f-444b-ae01-10ebf181f22e.png)  
![Power BI Preview](https://image2url.com/images/1755864852413-9215d9da-2dc0-4c8a-8534-41bcd7ee9d33.png)

---

### 🟢 Streamlit App  
Interactive dashboard for real-time customer insights:

- 📍 Area-wise cuisine preferences  
- 🕒 Delivery time and rating analysis  
- 💳 Payment method segmentation  
- 😊 Sentiment prediction and visualization  

![Streamlit Preview](https://image2url.com/images/1755864889746-9e0efb35-0865-4168-8617-b1a9184a0e2a.png)  
![Streamlit Preview](https://image2url.com/images/1755864937500-2721b6be-d066-41b2-b846-da2dd7746720.png)  
![Streamlit Preview](https://image2url.com/images/1755864964953-43aae3a9-88d7-445b-86b0-cdb396f7f0a8.png)

---

## 🚀 Deployment

- Model serialized with `joblib` as `rf_model.pkl`  
- Dashboard deployed via **Streamlit Cloud**  
- SQL integration for dynamic customer filtering  
- Power BI presentation deck created for stakeholder review  

---

## 🧠 Business Impact

- Identifies key drivers of customer satisfaction  
- Optimizes delivery operations and service quality  
- Supports targeted marketing based on sentiment and behavior  
- Enables data-driven decisions for restaurant partnerships  

---

## 🛠️ Tech Stack

- **Python**: Pandas, NumPy, Scikit-learn, Streamlit  
- **SQL**: Data extraction and filtering  
- **Visualization**: Power BI, Matplotlib, Seaborn, Plotly  
- **Deployment**: Streamlit Cloud, GitHub  

---

## 📌 Future Enhancements

- Integrate real-time order tracking and feedback  
- Add NLP-based sentiment scoring from reviews  
- Enable geospatial mapping of delivery hotspots  
- Expand dashboard to include loyalty and churn metrics  

---

## 👤 Author

**Anesh Raj**  

🔗 [GitHub Profile](https://github.com/aneshraj-d96)
