import pandas as pd
import asyncio
from infoExtraction import info_extraction

async def info_extract_all(prompt, df, column, model):
    """
    Extract information from a DataFrame column using a specified model.
    
    Args:
        prompt (str): The base prompt string for generating queries.
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to extract information from.
        model (object): The model used to generate content based on the query.

    Returns:
        pd.DataFrame: DataFrame containing the row and the generated response.
    """
    tasks = []
    for i, row in enumerate(df[column]):
        # Replace placeholder with actual row data if present
        if "{entity}" in prompt:
            prompt_model = prompt.replace("{entity}", str(row))
        else:
            prompt_model = f"{prompt} {row}"
        tasks.append(info_extraction(prompt_model, model))
    
    results = await asyncio.gather(*tasks)
    
    # Include the row data in the results DataFrame
    results_df = pd.DataFrame({
        column: df[column],
        'Response': [result['Response'][0] for result in results]
    })
    
    return results_df