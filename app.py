import streamlit as st
import pandas as pd
import numpy as np
import datetime
import random
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go



# Set page title
st.set_page_config(page_title='Item Demand Forecasting', page_icon=':bar_chart:', layout='wide')

# Page title and description
st.title('Item Demand Forecasting')
st.write('''This app generates item demand forecasting for next 7 days based on a user input. Once
         a user inputs a value, the program will build a dummy dataset of a item demand forecast and then
         build a forecasting model on and predicts the forecasting for next 7 days.''')

# User input
user_input = st.number_input('Enter an integer value for your current demand', value=50, step=1)

# Input for How many days

user_input_days = st.number_input('Enter Number of Days you want to forecast (min 3 and max 14 Days)',
                                  value=7, step=1, max_value=14, min_value = 3)
# Current date
today = datetime.date.today() + datetime.timedelta(days=1)

# Generate random data points
data_points = [random.randint(user_input-5, user_input+5) for _ in range(user_input_days)]

# Create dataframe with dates and data points
df = pd.DataFrame({
    'date': pd.date_range(start=today, periods=user_input_days),
    'data_point': data_points
})

# # Create line chart
# fig, ax = plt.subplots(figsize=(20, 4))
# ax.plot(df['date'], df['data_point'], marker='o')
# ax.set_xlabel('Date')
# ax.set_ylabel('Quantity')
# ax.set_title('Item Demand Forecasting for next 7 Days')

# Create Plotly line chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['date'], y=df['data_point'], mode='lines+markers', name='Data Points'))
fig.update_layout(title='Item Demand Forecasting for next 7 Days', xaxis_title='Date', yaxis_title='Demand Quantity',
                  width=1450, height=400)

# Display chart
st.plotly_chart(fig)
# Display chart
# st.pyplot(fig)
