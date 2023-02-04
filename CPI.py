import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet

st.title("Consumer Price Index in Mongolia")
st.write("Analysing the inflation over the years and how they relate to the average prices of goods and services in Mongolia, using Facebook Prophet. By using past recorded data to make predictions for the price changes for the next 12 months.")

columns = ['Alcohol And Tobacco', 'Clothing,Footwear,and Cloth'] # add other columns here
selected_column = st.selectbox("Select a column", columns)

@st.cache
def load_data(column):
    if column == "Alcohol And Tobacco":
        df = pd.read_csv("Data/alcohol and tobacco.csv", thousands=",")
    elif column == "Clothing,Footwear,and Cloth":
        df = pd.read_csv("Data/clothing, footwear, and cloth.csv", thousands=",")
    # add more elif blocks for other columns
    return df

st.table(df)
