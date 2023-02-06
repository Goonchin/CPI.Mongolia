import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px

st.title("How Does Inflation Affect The Mongolian Economy?")
st.subheader("Take a look at the current records of prices of different products and services in Mongolia.")

columns = ['Alcohol And Tobacco', 'Clothing,Footwear,and Cloth','Communications','Education Services','Food And Non-Alcoholic Beverages',
           'Health','Housing,Water,Electricity,Fuels','Overall Index','Recreation and Culture','Transport','All'] # add other columns here
selected_column = st.selectbox("Select a column", columns)

@st.cache
def load_data(column):
    data_files = {
        "Alcohol And Tobacco": "alcohol and tobacco.csv",
        "Clothing,Footwear,and Cloth": "clothing, footwear, and cloth.csv",
        "Communications": "communications.csv",
        "Education Services": "education services.csv",
        "Food And Non-Alcoholic Beverages": "food and non-alchoholic beverages.csv",
        "Health": "health.csv",
        "Housing,Water,Electricity,Fuels": "housing, water, electricity, fuels.csv",
        "Recreation and Culture": "recreation and culture.csv",
        "Transport": "transport.csv",
        "Overall Index": "overall Index.csv",}
    
   if column == "All":
        dfs = [pd.read_csv(f"Data/{file}", thousands=",") for file in data_files.values()]
        df = pd.concat(dfs)
        df["category"] = [c for c in data_files.keys() for file in data_files.values()]
        return df
    else:
        df = pd.read_csv(f"Data/{data_files[column]}", thousands=",")
        return df

df = load_data(selected_column)

model = Prophet()
model.fit(df)

#Make predictions
future = model.make_future_dataframe(periods=36, freq='M')
forecast = model.predict(future)

st.write("By looking at the data, we can see certain trends and different fluctuations in the price points for general products or services. As an economic standpoint it’s pretty adamant that, for consumer’s the price for goods and services will continue increasing, as well as overall living costs. ")

# Plot the predictions
fig = px.line(forecast, x='ds', y='yhat', title="Forecast of " + selected_column + " using Prophet")
fig.update_layout(xaxis_title="Date", yaxis_title="Price")
st.plotly_chart(fig)

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
