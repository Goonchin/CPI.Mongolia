import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
from prophet.plot import plot_cross_validation_metric
import base64

st.title('Time Series Forecasting!')
df = pd.read_csv('https://github.com/Goonchin/CPI.Mongolia/blob/01c9b483697d1daebf8dd0ad9f1f20adf5708f46/Data/CPI.csv')
st.dataframe(df)
