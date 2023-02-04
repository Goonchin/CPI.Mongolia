import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

st.title("Consumer Price Index in Mongolia")

columns = ['Alcohol And Tobacco', 'Clothing,Footwear,and Cloth','Communications','Education Services','Food And Non-Alcoholic Beverages','Furnishings, Household Equipment, and tools',
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
    elif column == "Furnishings, Household Equipment and Tools":
        df = pd.read_csv("Data/furnishings, household equipment and tools.csv", thousands=",")    
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

df.index = df['Date']
df = df[['Prices']]
df.rename(columns={'Prices': 'y'}, inplace=True)
df['ds'] = df.index

model = Prophet()
model.fit(df)

#Make predictions
future = model.make_future_dataframe(periods=12, freq='M')
forecast = model.predict(future)

st.write("Analysing the inflation over the years and how they relate to the average prices of goods and services in Mongolia, using Facebook Prophet. By using past recorded data to make predictions for the price changes for the next 12 months.")

# Plot the predictions
fig = model.plot(forecast)
st.pyplot(fig)
