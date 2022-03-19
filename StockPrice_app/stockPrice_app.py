# =========================================================================================
#                                IMPORT LIBRARIES
# =========================================================================================

import pandas as pd
import numpy as np
from datetime import date
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

st.title("Stock Price Prediction") # SET PAGE TITLE
# --- END CONFIG PAGE ---


st.markdown('---') # Add a page break


# --- DESCRIBE WEB APPLICATION ---
st.header('How to use the web app?') 

bullet_points = '''
- Search for a stock using the search bar
- Input the number of days you would like the price to be predicted
- See a price trend graph
- See the predicted stock price results

'''
st.markdown(bullet_points)

st.markdown('---') # Add a page break