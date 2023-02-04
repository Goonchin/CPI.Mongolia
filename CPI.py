import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fbprophet import Prophet

@st.cache
def load_data():
    df = pd.read_csv("/content/drive/MyDrive/Captone CPI/CPI.csv", thousands=",")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.dropna()
    return df

df = load_data()

st.title("Consumer Price Index in Mongolia")
st.write("Analysing the inflation over the years and how they relate to the average prices of goods and services in Mongolia")

columns = df.columns[1:]
selected_column = st.selectbox("Select a column", columns)

st.line_chart(df[["Date", selected_column]])

st.write("Analyzing the trend using Facebook Prophet")
model = Prophet(yearly_seasonality=True)
model.fit(df[["Date", selected_column]])
future = model.make_future_dataframe(periods=12, freq='M')
forecast = model.predict(future)

st.line_chart(forecast[["ds", "yhat"]])

st.write("Forecasted values for the next year")
forecast[["ds", "yhat"]].tail(12)