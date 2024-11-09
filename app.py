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
    """
    Configure the Generative AI model using the API key from environment variables.
    
    Returns:
        genai.GenerativeModel: Configured Generative AI model or None if API key is missing.
    """
    api_key = os.getenv('GOOGLE_API_KEY')
    if (api_key):
        genai.configure(api_key=api_key)
        return genai.GenerativeModel("gemini-1.5-flash")
    else:
        st.error("Google API key not found. Please set the GOOGLE_API_KEY environment variable.")
        return None

model = configure_genai()

def info_extract(df, model):
    """
    Extract information from a specified column in the DataFrame using a base prompt.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        model (genai.GenerativeModel): The configured Generative AI model.
    """
    if df is not None:
        st.header("Information Extraction")
        st.markdown("Use `{entity}` as a placeholder for the column values in your prompt.")
        prompt = st.text_input("Enter the base prompt for generating queries")
        column = st.selectbox("Select the column to extract information from", df.columns)
        
        # Add button to trigger information extraction
        extract_button = st.button("Extract Information")
        
        # Check if button is clicked
        if extract_button:
            if prompt and column:
                if model:
                    # Run the asynchronous extraction within a synchronous context
                    with st.spinner('Extracting information...'):
                        results_df = asyncio.run(info_extract_all(prompt, df.head(100), column, model))
                    st.dataframe(results_df)
                    
                    # Add button to download the extracted DataFrame
                    csv = results_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download Extracted Data as CSV",
                        data=csv,
                        file_name='extracted_data.csv',
                        mime='text/csv',
                    )
                else:
                    st.warning("Generative AI model configuration failed due to missing API key.")
            else:
                st.warning("Please provide a prompt and select a column.")

# Streamlit App Title and Headers
st.title("Data Upload and Display")
st.header("Upload CSV File or Provide Google Sheets URL")

# Data Loading Function
def load_data(file=None, google_sheet_url=None):
    """
    Load data from a CSV file or Google Sheets URL.
    
    Args:
        file (UploadedFile): The uploaded CSV file.
        google_sheet_url (str): The Google Sheets URL.
    
    Returns:
        pd.DataFrame: DataFrame containing the loaded data or None if loading fails.
    """
    try:
        if file:
            df = pd.read_csv(file)
            return df
        elif google_sheet_url:
            df = Load_DataFrame(google_sheet_url, Gsheet=True)
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
