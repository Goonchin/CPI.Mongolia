#Import streamlit
import streamlit as st
#Import NumPy and Pandas for data manipulation 
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
from prophet.plot import plot_cross_validation_metric
#for encoding binary data to printable ASCII characters and decoding it  #back to binary form
import base64 
st.title('Time Series Forecasting Using Streamlit')
st.write("IMPORT DATA")
st.write("Import the time series CSV file. It should have two columns labelled as 'ds' and 'y'. The 'ds' column should be of DateTime format by Pandas. The 'y' column must be numeric representing the measurement to be forecasted.") 

if data is not None:
    appdata = pd.read_csv(data)  #read the data fro
    appdata['ds'] = pd.to_datetime(appdata['ds'],errors='coerce') 
    st.write(data) #display the data  
    max_date = appdata['ds'].max() #compute latest date in the data 
                
st.write("SELECT FORECAST PERIOD") #text displayedperiods_input = st.number_input('How many days forecast do you want?',
    min_value = 1, max_value = 365)
#The minimum number of days a user can select is one, while the maximum is  #365 (yearly forecast)

if data is not None:
        obj = Prophet() #Instantiate Prophet object
        obj.fit(appdata)  #fit the data 
    
    
