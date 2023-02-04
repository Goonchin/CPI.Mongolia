import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet

@st.cache
def load_data(column):
    if column == "Alcohol And Tobacco":
        df = pd.read_csv("Data/alcohol and tobacco.csv", thousands=",")
    elif column == "Clothing,Footwear,and Cloth":
        df = pd.read_csv("Data/clothing, footwear, and cloth.csv", thousands=",")
    # add more elif blocks for other columns
    else:
        df = pd.read_csv("Data/CPI.csv", thousands=",")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.dropna()
    return df

st.title("Consumer Price Index in Mongolia")
st.write("Analysing the inflation over the years and how they relate to the average prices of goods and services in Mongolia, using Facebook Prophet. By using past recorded data to make predictions for the price changes for the next 12 months.")

columns = ['Alcohol And Tobacco', 'Clothing,Footwear,and Cloth'] # add other columns here
selected_column = st.selectbox("Select a column", columns)

df = load_data(selected_column)

st.line_chart(df[['ds', 'y']])

st.write("Analyzing the trend using Facebook Prophet")
model = Prophet(yearly_seasonality=True)
df_model = df[["ds", 'y']]
df_model = df_model.rename(columns={"ds": "Date", 'y': 'Prices'})
model.fit(df_model)
future = model.make_future_dataframe(periods=12, freq='M')
forecast = model.predict(future)

st.line_chart(forecast[["ds", "yhat"]])

st.write("Forecasted values for the next year")
forecast[["ds", "yhat"]].tail(12)

