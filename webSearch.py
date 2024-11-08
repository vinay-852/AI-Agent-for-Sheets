import json
import asyncio
from langchain_community.document_loaders import SeleniumURLLoader
from googlesearch import search as google_search

async def fetch_page_content(url):
    """
    Fetch page content using Selenium.
    
    Args:
        url (str): URL of the page to load.

    Returns:
        str: Content of the page.
    """
    try:
        loader = SeleniumURLLoader(urls=[url], headless=True)
        result = loader.load()
        return result[0].page_content if result else ""
    except Exception as e:
        print(f"Failed to load URL {url}: {e}")
        return ""

async def get_data_without_proxies(prompt: str, max_results: int = 3):
    """
    Get data from the web without using proxies.

    Args:
        prompt (str): The search query.
        max_results (int): The maximum number of results to return.

    Returns:
        str: The JSON response containing the prompt and data content.
    """
    # Fetch top links from Google search
    google_links = list(google_search(prompt, num_results=max_results, sleep_interval=0.5))
    data_content = ""

    # Use asynchronous loading to speed up content retrieval
    tasks = [fetch_page_content(url) for url in google_links]
    contents = await asyncio.gather(*tasks)

    for content in contents:
        data_content += content

    return json.dumps({'prompt': prompt, 'data': data_content})