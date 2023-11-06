yimport pandas as pd
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
        'Square_Feet': [2000, 2000],
        'Bedrooms': [3, 3],
        'Bathrooms': [2, 2],
        'Garage': [2, 2],            # Number of garage spaces
        'Year_Built': [2023, 2023],  # Year the house was built
        'Fireplace': ['Yes', 'No'],  # Whether the house has a fireplace
        'Pool': ['Yes', 'No'],       # Whether the house has a pool
        'School_rating': [9, 9],     # Rating of the nearest school (1-10)
        'Crime_Rate': [3.5, 3.5],    # Crime rate in the neighborhood (per 1000 residents)
        'Market_Distance': [1.5, 1.5]  # Distance to the nearest market (miles)
    }
    
    # Calculate the predicted prices and add them to the data
    predicted_prices = [predict_house_price(location, area, bedrooms, bathrooms, garage, year_built, fireplace, pool, school_rating, crime_rate, market_distance) for location, area, bedrooms, bathrooms, garage, year_built, fireplace, pool, school_rating, crime_rate, market_distance in zip(data['Location'], data['Square_Feet'], data['Bedrooms'], data['Bathrooms'], data['Garage'], data['Year_Built'], data['Fireplace'], data['Pool'], data['School_Rating'], data['Crime_Rate'], data['Market_Distance'])]
    data['Predicted_Price'] = predicted_prices
    
    return pd.DataFrame(data)

# Simulated live house price prediction function (replace with your actual model)
def predict_house_price(location, area, bedrooms, bathrooms, garage, year_built, fireplace, pool, school_rating, crime_rate, market_distance):
    # Replace with your trained model and appropriate coefficients
    # In practice, you should load your trained model and use it for predictions.
    
    # Example coefficients (replace with your actual coefficients)
    coefficients = [100, 50, 75, 25, 20, -10, 15, 10, 5, 15]  # Adjust to match the number of features

    # Encode categorical features like 'Fireplace' and 'Pool'
    fireplace_encoded = 1 if fireplace == 'Yes' else 0
    pool_encoded = 1 if pool == 'Yes' else 0
    
    # Ensure that coefficients and features are of numeric data types
    coefficients = [float(c) for c in coefficients]  # Convert to float if needed
    
    # Construct the feature vector
    features = [area, bedrooms, bathrooms, garage, year_built, school_rating, crime_rate, market_distance, fireplace_encoded, pool_encoded]
    features = [float(f) for f in features]  # Convert to float if needed
    
    # Perform the prediction
    predicted_price = np.dot(features, coefficients)
    return predicted_price

# Page config with custom title, icon, and layout
st.set_page_config(
    page_title="Live House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Main content
st.markdown("<h1 style='text-align: center;'>HOUSE PRICE PREDICTION🏠</h1>", unsafe_allow_html=True)

# Create a centered section using Markdown
st.markdown("<h1 style='text-align: center;'>House Features🏠</h1>", unsafe_allow_html=True)

# Input elements for user input in the center of the app
location = st.selectbox("Location", ["Downtown", "Suburb"])
area = st.number_input("Area (Square Feet)", min_value=0, value=2000)
bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
bathrooms = st.number_input("Bathrooms", min_value=0, value=2)
garage = st.number_input("Garage Spaces", min_value=0, value=1)
year_built = st.number_input("Year Built", min_value=1800, value=2000)
fireplace = st.radio("Fireplace", ["Yes", "No"])
pool = st.radio("Pool", ["Yes", "No"])
school_rating = st.slider("School Nearby (1-10)", min_value=1, max_value=10, value=8)
crime_rate = st.number_input("Crime Rate (per 1000 residents)", min_value=0.0, value=3.0)
market_distance = st.number_input("Distance to Nearest Market (miles)", min_value=0.0, value=1.0)

# Add a "Predict" button
if st.button("Predict"):
    # Use st.spinner to indicate that the prediction is being processed
    with st.spinner("Predicting..."):
        try:
            # Perform live house price prediction when the button is clicked
            predicted_price = predict_house_price(location, area, bedrooms, bathrooms, garage, year_built, fireplace, pool, school_rating, crime_rate, market_distance)
    
            # Display predicted prices
            st.markdown(f"<h2 style='text-align: center;color:red;'>Predicted Price: ${predicted_price:,.2f}</h2>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Remove the time.sleep(1) line; it's not needed

# Display the simulated live data in the sidebar as a vertical table
st.sidebar.markdown("<h1 style='text-align: center;'>Simulated Live Data</h1>", unsafe_allow_html=True)
live_data = fetch_live_data()
st.sidebar.table(live_data)
