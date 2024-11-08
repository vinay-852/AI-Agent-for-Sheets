import requests
from duckduckgo_search import DDGS
from langchain_community.document_loaders import SeleniumURLLoader
import json
import time
import random

def perform_duckduckgo_search(prompt: str, max_results: int = 2):
    """
    Perform a search on DuckDuckGo and return the top results.
    
    Args:
        prompt (str): The search query.
        max_results (int): The maximum number of results to return.

    Returns:
        list: A list of URLs for the top search results.
    """
    results = DDGS().text(prompt, max_results=max_results)
    return [result['href'] for result in results[:max_results]]

def get_data_without_proxies(prompt: str, max_results: int = 2):
    """
    Get data from the web without using proxies.

    Args:
        prompt (str): The search query.
        max_results (int): The maximum number of results to return.
    
    Returns:
        str: The JSON response containing the prompt and data content.
    """
    top_links = perform_duckduckgo_search(prompt, max_results)
    data_content = ""

    for url in top_links:
        retries = 5
        for i in range(retries):
            try:
                loader = SeleniumURLLoader(urls=[url])
                result = loader.load()
                if result:
                    data_content += result[0].page_content
                break
            except requests.exceptions.RequestException as e:
                if i < retries - 1:
                    wait_time = (2 ** i) + random.uniform(0, 1)
                    print(f"Rate limit hit. Retrying in {wait_time:.2f} seconds...")
                    time.sleep(wait_time)
                else:
                    print("Max retries reached. Exiting.")
                    raise e

    return json.dumps({'prompt': prompt, 'data': data_content})