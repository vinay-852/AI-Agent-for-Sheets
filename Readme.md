# AI Agent for Sheets

This project provides tools for extracting information from web searches and Google Sheets using AI models.

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/vinay-852/AI-Agent-for-Sheets.git
    cd AI-Agent-for-Sheets
    ```

2. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Create a `.env` file and add your Google API key:**
    ```sh
    touch .env
    echo "GOOGLE_API_KEY=your_google_api_key_here" >> .env
    ```

4. **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```

## Usage

### Upload CSV or Google Sheets URL

1. **Upload a CSV file:**
    - Click on "Choose a CSV file" and select your CSV file.

2. **Provide a Google Sheets URL:**
    - Enter the Google Sheets URL in the provided text input.

### Information Extraction

1. **Enter the base prompt:**
    - Provide a base prompt for generating queries.

2. **Select the column:**
    - Choose the column from which you want to extract information.

3. **Extract Information:**
    - Click on "Extract Information" to start the extraction process.

### Example

1. **Upload a CSV file or provide a Google Sheets URL.**
2. **Enter a prompt like "Summarize the content of" and select the desired column.**
3. **Click "Extract Information" to see the results.**

## Files

- `app.py`: Main Streamlit application.
- `loadData.py`: Functions for loading data from CSV or Google Sheets.
- `infoExtraction.py`: Functions for extracting information using AI models.
- `infoExtractionOfAll.py`: Functions for extracting information from all rows in a DataFrame.
- `webSearch.py`: Functions for performing web searches and retrieving data.

## License

This project is licensed under the MIT License.

## AI Model

This project uses the Generative AI model "gemini-1.5-flash" from Google for information extraction.

## Technologies Used

- **Python**: Programming language used for the project.
- **Streamlit**: Framework for building interactive web applications.
- **Pandas**: Library for data manipulation and analysis.
- **Requests**: Library for making HTTP requests.
- **Selenium**: Tool for web scraping.
- **DuckDuckGo Search**: API for performing web searches.
- **LangChain**: Library for working with language models.
- **Google Generative AI**: AI model used for information extraction.
- **dotenv**: Library for loading environment variables from a `.env` file.