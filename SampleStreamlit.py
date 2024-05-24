#!/usr/bin/env python
# coding: utf-8

# In[1]:


# app.ipynb
import streamlit as st
import pandas as pd

# Title of the app
st.title('Simple Data Analysis App')

# File uploader widget
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)
    
    # Display the dataframe
    st.write("Dataframe:")
    st.write(df)
    
    # Display descriptive statistics
    st.write("Summary:")
    st.write(df.describe())


# In[ ]:




