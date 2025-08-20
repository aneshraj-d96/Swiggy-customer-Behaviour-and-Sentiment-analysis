import streamlit as st
import pandas as pd
import pickle

# Load model
model_path = 'C:\\Users\\Dhusyath\\Downloads\\PROJECTS_DA\\PROJECTS_DA\\swiggy customer beh & sentiment analysis\\rf_model.pkl'
model = pickle.load(open(model_path, "rb"))

# Load dataset (optional, for reference or future use)
data_path = 'C:\\Users\\Dhusyath\\Downloads\\PROJECTS_DA\\PROJECTS_DA\\swiggy customer beh & sentiment analysis\\swiggy_data.csv'
df = pd.read_csv(data_path)

# App title
st.title(" Swiggy Bangalore Sentiment Predictor")

st.markdown("Predict customer sentiment based on order details and ratings.")

# User inputs
order_value = st.slider(" Order Value (₹)", min_value=100, max_value=1000, value=350)
delivery_time = st.slider(" Delivery Time (minutes)", min_value=15, max_value=90, value=30)
delivery_rating = st.selectbox(" Delivery Rating", [1, 2, 3, 4, 5])
food_rating = st.selectbox(" Food Rating", [1, 2, 3, 4, 5])
age = st.slider(" Customer Age", min_value=18, max_value=65, value=30)

# Prepare input data
input_data = pd.DataFrame({
    "Order_Value": [order_value],
    "Delivery_Time_Min": [delivery_time],
    "Delivery_Rating": [delivery_rating],
    "Food_Rating": [food_rating],
    "Customer_Age": [age]
})

# Predict sentiment
predicted_sentiment = model.predict(input_data)[0]

# Display result
st.subheader("🧠 Prediction Result")
st.write(f"Predicted Sentiment: **{predicted_sentiment}**")

# Optional: Show input summary
st.markdown("### 📋 Input Summary")
st.write(input_data)
