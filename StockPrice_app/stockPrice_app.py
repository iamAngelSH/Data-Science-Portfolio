# =========================================================================================
#                                IMPORT LIBRARIES
# =========================================================================================

import pandas as pd
import numpy as np
from datetime import date
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
import streamlit as st

# STOCK DATA FROM YAHOO FINANCE
import yfinance as yf

# =========================================================================================
#                               CONFIGURE PAGE | PAGE DETAILS
# =========================================================================================

# --- CONGIF PAGE AND PAGE LAYOUT ---

st.set_page_config(page_title='Stock Price Prediction', # APP NAME FOR BROWSER
                    layout= 'wide' # PAGE LAYOUT
                    )

st.title("Stock Price Prediction 🤑💲") # SET PAGE TITLE
# --- END CONFIG PAGE ---


st.markdown('---') # Add a page break


# --- DESCRIBE WEB APPLICATION ---
st.header('How to use the web app?') 

bullet_points = '''
- FIRST INPUT:
    - Enter the ticker symbol for stock of your choice.
    - You can use the table to the side to search through different stocks.
- SECOND INPUT:
    - Enter the amount of days out you would like to see the predicted stock price.
    - ONLY positive numbers, please :)
- As you update the stock you want to see, there will be a line graph to show you the price trend.


'''
with st.expander('🧑‍🏫 INSTRUCTIONS'):
    st.markdown(bullet_points)

not_a_recommendation = '''
- This is not a tool to actually predict stock prices.
- Do not consult this app for your PERSONAL choices on buying stock.
- THIS APP IS JUST FOR FUN AND TO TEST MY PERSONAL KNOWLEDGE OF MACHINE LEARNING.

'''

with st.expander('⚠️ PLEASE READ'):
    st.markdown(not_a_recommendation)

st.markdown('---') # Add a page break

# --- END DESCRIPTION ---
# =========================================================================================


# --- FUNCTION TO READ IN DATA ---
def showStockNames():
    # ONLY NEED SYMBOL AND NAME
    stockName_df = pd.read_csv(
        'Data/stockNames.csv', 
        index_col = 0, 
        usecols= ['Symbol', 'Name']
        )

    return stockName_df

# --- END READ DATA FUNCTION ---


# =========================================================================================
#                                   INPUT LAYOUTS
# =========================================================================================
# PAGE LAYOUT
user_column, forecast_column, stock_column = st.columns((1, 1, 2))

# SYMBOL INPUT
with user_column:
    userInput = st.text_input('Enter a stock you would like to check?')
    userInput = userInput.upper()

# PREDICT NUMBER OF DAYS OUT
with forecast_column:
    forecastDays = st.number_input(label = 'Forecast Days...', step=1)
    if forecastDays < 0:
        st.write('ERROR: Number must be positive')

# SHOW STOCKS FOR USERS TO LOOK THROUGH
with stock_column:
    st.write("Need help? Look for stock names HERE.")
    st.dataframe(showStockNames())
# =========================================================================================
