import pandas as pd
import streamlit as st
import pandaslib as pl
import os

st.title("Data Extraction and Cleaning Pipeline")

survey_url = pd.read_csv('https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv')
st.info("Loading survey data...")
survey_url.to_csv('cache/survey.csv')

survey_url['year'] = survey_url['Timestamp'].apply(pl.extract_year_mdy)
st.success("Year extracted from timestamp!")

os.makedirs('cache', exist_ok=True)
survey_url.to_csv('cache/survey.csv', index=False)
st.write("Saved cleaned survey data to 'cache/survey.csv'.")

years = survey_url['year'].dropna().unique()
st.write(f"Found data for years: {years}")

for year in years:
    st.info(f"Fetching cost of living data for {year}...")
    try:
        col_year = pd.read_html(f"https://www.numbeo.com/cost-of-living/rankings.jsp?title={int(year)}&displayColumn=0")
        col_year = col_year[1]
        col_year['year'] = int(year)
        col_year.to_csv(f'cahce/col_{int(year)}.csv', index=False)
        st.success(f"Saved: 'cache/col_{int(year)}.csv'")
    except Exception as e:
        st.error(f"Failed to fetch COL data for {year}: {e}")

st.info("Downloading U.S. states reference table...")
state_url = "https://docs.google.com/spreadsheets/d/14wvnQygIX1eCVo7H5B7a96W1v5VCg6Q9yeRoESF6epw/export?format=csv"
try:
    state_table = pd.read_csv(state_url)
    state_table.to_csv('cache/survey.csv', index=False)
    st.success("Saved U.S. states to 'cache/survey.csv'.")
except Exception as e:
    st.error(f"Error loading states file: {e}")