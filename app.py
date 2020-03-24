import pandas as pd
import streamlit as st

st.title("Hospital, stat!")
st.subheader("Map of DC Area Primary Care Facilities")

# st.cache saves the data so we save on network calls
@st.cache
def fetch_data():
    df = pd.read_csv('https://opendata.arcgis.com/datasets/018890d7399245759f05c7932261ef44_7.csv')
    # rename for ST map function requirement & simplicity
    df = df.rename(columns={
        'X': 'lon',
        'Y': 'lat',
        'PrimaryCarePtWARD': 'ward'
        })
    
    return df

data = fetch_data()

# Chart 1: Interactive Map

st.write('## Map of Hospitals')
st.map(data)

# Chart 2: Bar chart of hospitals by ward
@st.cache
def hospitals_by_ward(data):
    return data['ward'].value_counts()

st.write('## Hospital count by ward')
st.bar_chart(hospitals_by_ward(data))

# Table 1: Raw data
st.write('## Raw hospital data')
st.dataframe(data)
