import streamlit as st
import pandas as pd
from main import scrape_it_companies

st.set_page_config(page_title="IT Companies in Noida", layout="wide")
st.title(" IT Company Scraper (Google Maps)")

if st.button("Scrape IT Companies"):
    with st.spinner("Scraping data from Google Maps..."):
        csv_file, data = scrape_it_companies()

    st.success(f"Scraping completed! Found {len(data)} companies.")
    df = pd.read_csv(csv_file)
    st.dataframe(df)

    st.download_button(
        label=" Download CSV",
        data=df.to_csv(index=False),
        file_name="it_companies_noida.csv",
        mime="text/csv"
    ) 