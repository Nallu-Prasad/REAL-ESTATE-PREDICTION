import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import time

# Simulated live data retrieval (replace with your data source)
def fetch_live_data():
    # Simulated data for demonstration purposes
    data = {
        'Timestamp': [pd.Timestamp.now(), pd.Timestamp.now() - pd.Timedelta(minutes=5)],
        'House_ID': [1, 2],
        'Location': ['Downtown', 'Suburb'],
        'Square_Feet': [2000, 2500],
        'Bedrooms': [3, 4],
        'Bathrooms': [2, 3]
    }
    return pd.DataFrame(data)

# Simulated live house price prediction function (replace with your actual model)
def predict_house_price(location, area, bedrooms, bathrooms):
    # Simulated linear regression model (replace with your trained model)
    # In practice, you should load your trained model and use it for predictions.
    
    # Encode the location feature using one-hot encoding
    location_encoded = 1 if location == 'Downtown' else 0
    
    # Ensure that coefficients and features are of numeric data types
    coefficients = [100, 50, 75, 25]  # Adjust to match the number of features
    coefficients = [float(c) for c in coefficients]  # Convert to float if needed
    
    features = [area, bedrooms, bathrooms, location_encoded]  # Include location as a feature
    features = [float(f) for f in features]  # Convert to float if needed
    
    predicted_price = np.dot(features, coefficients)
    return predicted_price

# Page config with custom title, icon, and layout
st.set_page_config(
    page_title="Live House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Main content
st.markdown("<h1 style='text-align: center;'>REAL ESTATE PREDICTION</h1>", unsafe_allow_html=True)

# Create a centered section using Markdown
st.markdown("<h1 style='text-align: center;'>House Features</h1>", unsafe_allow_html=True)

# Input elements for user input in the center of the app
location = st.selectbox("Location", ["Downtown", "Suburb"])
area = st.number_input("Area (Square Feet)", min_value=0, value=2000)
bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
bathrooms = st.number_input("Bathrooms", min_value=0, value=2)

# Add a "Predict" button
if st.button("Predict"):
    # Perform live house price prediction when the button is clicked
    predicted_price = predict_house_price(location, area, bedrooms, bathrooms)
    
    # Display predicted prices
    st.markdown(f"<h2 style='text-align: center;color:red;'>Predicted Price: ${predicted_price:,.2f}</h2>", unsafe_allow_html=True)

# Add a delay for updates
time.sleep(1)  # Replace this with your update logic
