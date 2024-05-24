#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# Define player names
players = ['Player A', 'Player B', 'Player C', 'Player D']

# Generate random values for goals, shots, assists, and runs
np.random.seed(0)  # For reproducibility
goals = np.random.randint(0, 10, size=4)
shots = np.random.randint(0, 20, size=4)
assists = np.random.randint(0, 10, size=4)
runs = np.random.randint(0, 50, size=4)

# Create a dictionary with the data
data = {
    'Name': players,
    'Goals': goals,
    'Shots': shots,
    'Assists': assists,
    'Runs': runs
}

# Create the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# In[2]:


# Define player names
players = ['Player A', 'Player B', 'Player C', 'Player D']

# Generate random values for sprints, accelerations, walking, and running
np.random.seed(1)  # For reproducibility
sprints = np.random.randint(0, 10, size=4)
accelerations = np.random.randint(0, 10, size=4)
walking = np.random.randint(0, 10, size=4)
running = np.random.randint(0, 10, size=4)

# Create a dictionary with the data
data = {
    'Name': players,
    'Sprints': sprints,
    'Accelerations': accelerations,
    'Walking': walking,
    'Running': running
}

# Create the DataFrame
df_sports = pd.DataFrame(data)

# Display the DataFrame
print(df_sports)


# In[3]:


# Define player names
team_name = 'Team A'

# Generate random values for shots, running distance, goals, and distance covered
np.random.seed(2)  # For reproducibility
shots = np.random.randint(0, 20, size=1)[0]
running_distance = np.random.randint(1000, 15000, size=1)[0]  # in meters
goals = np.random.randint(0, 5, size=1)[0]
distance_covered = np.random.randint(5000, 20000, size=1)[0]  # in meters

# Create a dictionary with the data
data = {
    'Team': [team_name],
    'Shots': [shots],
    'Running Distance (meters)': [running_distance],
    'Goals': [goals],
    'Distance Covered (meters)': [distance_covered]
}

# Create the DataFrame
df_team = pd.DataFrame(data)

# Display the DataFrame
print(df_team)


# In[4]:


import streamlit as st
import pandas as pd


# In[5]:


# Sample DataFrames
df = pd.DataFrame({
    'Name': ['Player A', 'Player B', 'Player C', 'Player D'],
    'Goals': [5, 0, 3, 3],
    'Shots': [12, 15, 0, 3],
    'Assists': [9, 5, 4, 7],
    'Runs': [22, 18, 11, 24]
})

df_sports = pd.DataFrame({
    'Name': ['Player A', 'Player B', 'Player C', 'Player D'],
    'Sprints': [5, 9, 0, 7],
    'Accelerations': [8, 5, 0, 6],
    'Walking': [9, 0, 1, 9],
    'Running': [5, 0, 7, 8]
})

df_team = pd.DataFrame({
    'Team': ['Team A'],
    'Shots': [15],
    'Running Distance (meters)': [8429],
    'Goals': [3],
    'Distance Covered (meters)': [12498]
})


# In[6]:


# Streamlit App
st.title('2024 Statistics')

option = st.selectbox('Select Data', ['Player Technical Data', 'Player Physical Data', 'Team Data'])

if option == 'Player Technical Data':
    st.write("### Player Technical Data")
    st.write(df)
elif option == 'Player Physical Data':
    st.write("### Player Physical Data")
    st.write(df_sports)
else:
    st.write("### Team Data")
    st.write(df_team)


# In[ ]:




