import pandas as pd
from infoExtraction import info_extraction

def info_extract_all(prompt, df, column, model):
    """
    Extract information from a DataFrame column using a specified model.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to extract information from.
        model (object): The model used to generate content based on the query.

    Returns:
        pd.DataFrame: DataFrame containing the row and the generated response.
    """
    results_df = pd.DataFrame(columns=[column, 'Response'])
    for i, row in enumerate(df[column]):
        prompt_model = f"{prompt} {row}"
        result_df1 = info_extraction(prompt_model, model)
        result_df1[column] = row  # Add the row data to the result DataFrame
        results_df = pd.concat([results_df, result_df1], ignore_index=True)
    return results_df