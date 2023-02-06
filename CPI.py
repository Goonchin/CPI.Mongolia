import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px

st.title("How Does Inflation Affect The Mongolian Economy?")
st.subheader("Take a look at the current records of prices of different products and services in Mongolia.")

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

st.write("By looking at the graph, It can be seen that there are certain trends and different fluctuations in the price points for general products or services. As an economic standpoint it’s pretty adamant that, for consumer’s the price for goods and services will continue increasing, as well as overall living costs. ")

# Plot the predictions
fig = px.line(forecast, x='ds', y='yhat', title="Forecast of " + selected_column + " using Prophet")
fig.update_layout(xaxis_title="Date", yaxis_title="Price")
st.plotly_chart(fig)

if selected_column == "Alcohol And Tobacco":
    description = "The recorded data starts in 2006-2022. There is a slight 'hump' between 2011-2015 which can be assumed that taxes for alcohol production increased or due to the sudden inflow of foriegn investors in Mongolia in 2011, supply increased so therefore, prices followed. Using Prophet we can then make a prediction for the next few years after our latest record, which is shown in the above interactive graph. The price of alcohol and tobacco products in Mongolia over the next 36 months, will continue to increase due to inflation and overall increasing costs for materials and labor."
elif selected_column == "Clothing,Footwear,and Cloth":
    description = "The recorded data starts in 2006-2022. Similar to the alcohol and tobacco chart, we can see that 'hump' again between 2011-2015, due to economic growth. The price of clothing, footwear, and cloth products in Mongolia over the next 36 months will continue to increase due to inflation and overall increasing costs for materials and labor."
elif selected_column == "Communications":
    description = "The recorded data starts in 2006-2022. Unlike the rest of the charts, communications flucuated much differently. It's shown that 2008-2011 there was a huge increase in price, which is probably due to growth in communications, as well as new laws being introduced concerning information technology field. The price of communication in Mongolia over the next 36 months will continue to stay stagnant due to relative costs over the years, showing not much change overall."
elif selected_column == "Education Services":
    description = "The recorded data starts in 2006-2022. Over the years, education increased steadily, due to costs and implementations of newer systems and technology for educational services. The price of education services in Mongolia over the next 36 months will continue to increase mainly due to inflation."
elif selected_column == "Food And Non-Alcoholic Beverages":
    description = "The recorded data starts in 2006-2022. Recently COVID-19 was a big suprise for everyone in the world. Border closures as well as limited importing skyrocketed prices for everything. But the steady increase of food and beverages are mainly from the growth and development of Mongolia. The price of food and non-alcoholic beverage products in Mongolia over the next 36 months will continue to increase due to inflation, and harder access to imports(materials and goods)."
elif selected_column == "Health":
    description = "The recorded data starts in 2006-2022. The development over the years, as well as new medicine and technologies caused the increase of overall healthcare or health services. The price of health products and services in Mongolia over the next 36 months will continue to increase due to inflation, scarcity of medication, and increasing population."
elif selected_column == "Housing,Water,Electricity,Fuels":
    description = "The recorded data starts in 2006-2022. The housing sector of Mongolia has increased dramatically over the years, including more development in and outside parts of the city, this can include anything from resturants, office building and of course real estate. The price of housing, water, electricity and fuels in Mongolia over the next 36 months will continue to increase due to development, inflation, and increasing population."
elif selected_column == "Overall Index":
    description = "The recorded data starts in 2006-2022. Overall, when taking in the big picture, we see that costs for consumers will continue to increase. As Mongolia further develops products and services will get more expensive. Over the next 36 months, it shows the same general incline and increase."
elif selected_column == "Recreation and Culture":
    description = "The recorded data starts in 2006-2022. Similar to the other charts and sectors, showing increases in price over the years. The price for recreation and culture over the next 36 months will continue to increase due to levels of high tourism, inflation, and maintaining tradtions and culture."
elif selected_column == "Transport":
    description = "The recorded data starts in 2006-2022. Transportation costs over the years have been rather explainable. The sudden pandemic recently limiting fuel imports and resources, but overall costs for transportation will always increase in any country that relies on petrol operated vehicals. The price for transport might decrease, due to the high influctution the past several months, but they also have a high chance of increasing due to other costs increasing."
# Add more elif blocks for other columns with their respective descriptions
else:
    description = "The price of the selected product category in Mongolia over the next 36 months, will overall increase over the years."

st.write(description)
