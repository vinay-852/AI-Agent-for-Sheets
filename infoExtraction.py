import json
import pandas as pd
from webSearch import get_data_without_proxies

def info_extraction(prompt, model):
    """
    Extract information based on the given prompt and model.
    
    Args:
        prompt (str): The base prompt string for generating queries.
        model (object): The model used to generate content based on the query.
    
    Returns:
        pd.DataFrame: DataFrame containing the results JSON and the generated response.
    """
    result_json = get_data_without_proxies(prompt)
    
    if isinstance(result_json, str):
        result_json = json.loads(result_json)
    
    enhanced_prompt = (
        f"Based on the following data, please provide a one-word answer if possible. "
        f"Your response should only include direct answers to the query. "
        f"if you know the answer, respond with the word or phrase that best answers the question. "
        f"If the answer is unavailable, respond with 'None'. "
        f"Do not include any additional information or context."
        f"\n\nPrompt: {result_json['prompt']}\n"
        f"Web Results: {result_json['data']}"
    )
    response = model.generate_content(enhanced_prompt)
    
    # Store results JSON and response in a DataFrame
    results_df = pd.DataFrame({
        'Prompt': [result_json['prompt']],
        'Web Results': [result_json['data']],
        'Response': [response.text]
    })
    
    return results_df