import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
import google.generativeai as genai
from loadData import Load_DataFrame
from infoExtractionOfAll import info_extract_all
import asyncio

# Load environment variables
load_dotenv()

# Configure Generative AI model
def configure_genai():
    api_key = os.getenv('GOOGLE_API_KEY')
    if (api_key):
        genai.configure(api_key=api_key)
        return genai.GenerativeModel("gemini-1.5-flash")
    else:
        st.error("Google API key not found. Please set the GOOGLE_API_KEY environment variable.")
        return None

model = configure_genai()

def info_extract(df, model):
    """Extract information from a specified column in the DataFrame using a base prompt."""
    if df is not None:
        st.header("Information Extraction")
        prompt = st.text_input("Enter the base prompt for generating queries")
        column = st.selectbox("Select the column to extract information from", df.columns)
        
        # Add button to trigger information extraction
        extract_button = st.button("Extract Information")
        
        # Check if button is clicked
        if extract_button:
            if prompt and column:
                if model:
                    # Run the asynchronous extraction within a synchronous context
                    results_df = asyncio.run(info_extract_all(prompt, df.head(100), column, model))
                    st.dataframe(results_df)
                else:
                    st.warning("Generative AI model configuration failed due to missing API key.")
            else:
                st.warning("Please provide a prompt and select a column.")

# Streamlit App Title and Headers
st.title("Data Upload and Display")
st.header("Upload CSV File or Provide Google Sheets URL")

# Data Loading Function
def load_data(file=None, google_sheet_url=None):
    """Load data from a CSV file or Google Sheets URL."""
    try:
        if file:
            df = pd.read_csv(file)
            st.success("CSV file uploaded successfully!")
            return df
        elif google_sheet_url:
            df = Load_DataFrame(google_sheet_url, Gsheet=True)
            st.success("Google Sheets data loaded successfully!")
            return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# File Upload and Google Sheets Input
file_upload = st.file_uploader("Choose a CSV file", type="csv")
google_sheet_url = st.text_input("Or enter Google Sheets URL")

# Data Loading and Display
df = load_data(file=file_upload, google_sheet_url=google_sheet_url)
if df is not None:
    st.dataframe(df.head())
    info_extract(df, model)
else:
    st.info("Please upload a CSV file or enter a Google Sheets URL.")
