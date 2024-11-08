import re
import pandas as pd

def get_Key(url: str) -> str:
    """
    Extracts the key from a Google Sheets URL.

    Args:
        url (str): The Google Sheets URL.

    Returns:
        str: The extracted key or an error message.
    """
    try:
        key = re.search(r'd/([-\w]+)/', url).group(1)
        return key
    except Exception as e:
        return str(e)

def Load_DataFrame(path: str, Gsheet: bool = False) -> pd.DataFrame:
    """
    Loads data from a CSV file or Google Sheets.

    Args:
        path (str): Path to the CSV file or Google Sheets URL.
        Gsheet (bool): Whether the path is a Google Sheets URL.

    Returns:
        pd.DataFrame: DataFrame containing the data.
    """
    try:
        if Gsheet:
            key = get_Key(path)
            sheet_url = f'https://docs.google.com/spreadsheets/d/{key}/export?format=csv'
            df = pd.read_csv(sheet_url)
        else:
            df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on failure