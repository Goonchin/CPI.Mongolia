import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

st.title("Consumer Price Index in Mongolia")

columns = ['Alcohol And Tobacco', 'Clothing,Footwear,and Cloth','Communications','Education Services','Food And Non-Alcoholic Beverages',
           'Health','Housing,Water,Electricity,Fuels','Overall Index','Recreation and Culture','Transport'] # add other columns here
selected_column = st.selectbox("Select a column", columns)

@st.cache
def load_data(column):
    if column == "Alcohol And Tobacco":
        df = pd.read_csv("Data/alcohol and tobacco.csv", thousands=",")
    elif column == "Clothing,Footwear,and Cloth":
        df = pd.read_csv("Data/clothing, footwear, and cloth.csv", thousands=",")
    elif column == "Communications":
        df = pd.read_csv("Data/communications.csv", thousands=",")
    elif column == "Education Services":
        df = pd.read_csv("Data/education services.csv", thousands=",")
    elif column == "Food And Non-Alcoholic Beverages":
        df = pd.read_csv("Data/food and non-alchoholic beverages.csv", thousands=",")    
    elif column == "Health":
        df = pd.read_csv("Data/health.csv", thousands=",")
    elif column == "Housing,Water,Electricity,Fuels":
        df = pd.read_csv("Data/housing, water, electricity, fuels.csv", thousands=",")
    elif column == "Overall Index":
        df = pd.read_csv("Data/overall Index.csv", thousands=",")
    elif column == "Recreation and Culture":
        df = pd.read_csv("Data/recreation and culture.csv", thousands=",") 
    elif column == "Transport":
        df = pd.read_csv("Data/transport.csv", thousands=",")    
    # add more elif blocks for other columns
    return df

df = load_data(selected_column)

model = Prophet()
model.fit(df)

#Make predictions
future = model.make_future_dataframe(periods=36, freq='M')
forecast = model.predict(future)

st.write("Analysing the inflation over the years and how they relate to the average prices of goods and services in Mongolia, using Facebook Prophet. All the data was obtained from 1212.mn from the Consumer Price Index section.")

# Plot the predictions
fig =model.plot(forecast)
st.pyplot(fig)

if selected_column == "Alcohol And Tobacco":
    description = "The price of alcohol and tobacco products in Mongolia over the next 36 months, will continue to increase due to inflation and overall increasing costs for materials and labor."
elif selected_column == "Clothing,Footwear,and Cloth":
    description = "The price of clothing, footwear, and cloth products in Mongolia over the next 36 months will continue to increase due to inflation and overall increasing costs for materials and labor."
elif selected_column == "Communications":
    description = "The price of communication in Mongolia over the next 36 months will continue to stay stagnant due to relative costs over the years, showing not much change overall."
elif selected_column == "Education Services":
    description = "The price of education services in Mongolia over the next 36 months will continue to increase due to inflation and overall increasing costs for labor and supplies."
elif selected_column == "Food And Non-Alcoholic Beverages":
    description = "The price of food and non-alcoholic beverage products in Mongolia over the next 36 months will continue to increase due to inflation and overall increasing costs for materials and labor."
elif selected_column == "Health":
    description = "The price of health products and services in Mongolia over the next 36 months will continue to increase due to inflation and overall increasing costs for materials and labor."
elif selected_column == "Housing,Water,Electricity,Fuels":
    description = "The price of housing,water,electricity and fuels in Mongolia over the next 36 months will continue to increase due to inflation, scarcity and maintenance costs."
elif selected_column == "Overall Index":
    description = "The prices of the overall index costs will continue to increase, due to an increase of all the difference consumer goods and services."
elif selected_column == "Recreation and Culture":
    description = "The price for recreation and culture will continue to increase due to levels of high tourism and overall costs for recreational activities increase as well."
elif selected_column == "Transport":
    description = "The price for transport might decrease, due to the high influctution the past several months, but they also have a high chance of increasing due to other costs increaseing."
# Add more elif blocks for other columns with their respective descriptions
else:
    description = "The price of the selected product category in Mongolia over the next 36 months, will overall increase over the years."

st.write(description)
