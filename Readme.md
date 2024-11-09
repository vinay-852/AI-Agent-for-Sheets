# AI Agent for Sheets

This project provides a powerful toolset for extracting, analyzing, and transforming data from web searches and Google Sheets through AI-driven techniques. Designed for researchers, analysts, and users who need rapid, relevant information processing, **AI Agent for Sheets** leverages cutting-edge AI and automation to streamline data handling.

## Project Overview

The primary objective of this project is to harness Google’s Generative AI model to enable precise and efficient information extraction. By integrating this AI with robust web scraping and data processing tools, users can rapidly obtain insights from diverse data sources, making it ideal for both quick data reviews and in-depth research.

## Key Features

- **AI-Powered Information Extraction**: Utilizing Google’s Generative AI model for meaningful and contextual data extraction.
- **Seamless Integration with Google Sheets**: Direct access to data from Google Sheets and CSV uploads, allowing for flexibility in data sources.
- **Web Search Integration**: Automated web search capability to gather information beyond the uploaded dataset.
- **User-Friendly Web Interface**: Built on Streamlit, making the application interactive and accessible without coding experience.
- **Flexible Data Processing Options**: Supports uploading CSV files or providing Google Sheets URLs to specify data sources.

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Framework for developing an interactive web application.
- **Pandas**: Essential library for data handling and manipulation.
- **Selenium**: Automates web searches and gathers data.
- **Google Search API**: Facilitates web search integration.
- **LangChain**: Framework for AI model-based operations.
- **Google Generative AI**: "Gemini-1.5-flash" model used for contextual information extraction.
- **dotenv**: Manages environment variables securely.

## Setup Instructions

To set up the project on your local environment, follow these steps:

### 1. Clone the Repository
Clone the project repository to your local machine and navigate into the directory.
```sh
git clone https://github.com/vinay-852/AI-Agent-for-Sheets.git
cd AI-Agent-for-Sheets
```

### 2. Install Dependencies
Install all necessary Python packages using the requirements file.
```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory to store your Google API key.
```sh
echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
```


### 4. Launch the Streamlit App
Start the web application using Streamlit.
```sh
streamlit run app.py
```

## Usage Guide

Once the application is running, you can interact with the AI Agent for Sheets through a user-friendly interface.

### Step 1: Upload Data Source
Choose one of the following options to provide data to the application:


- **Upload a CSV File**: Select and upload a CSV file by clicking on "Choose a CSV file."
- **Enter a Google Sheets URL**: Paste a Google Sheets URL in the text input box.
  <img width="934" alt="Screenshot 2024-11-09 at 11 29 48 AM" src="https://github.com/user-attachments/assets/d5470e1f-2847-4793-b89a-53ff24be1db9">
  <img width="864" alt="Screenshot 2024-11-09 at 11 30 25 AM" src="https://github.com/user-attachments/assets/4b69bf84-3c0f-4503-8bcc-2f7d6e1b38cd">

### Step 2: Information Extraction

1. **Enter a Base Prompt**: Enter a base prompt to guide the AI model in extracting relevant information.

2. **Select a Column for Extraction**: Choose the column you wish to analyze or extract information from.

3. **Click "Extract Information"**: Start the extraction process. The AI will retrieve relevant data for up to 100 unique rows.

   <img width="797" alt="Screenshot 2024-11-09 at 11 31 24 AM" src="https://github.com/user-attachments/assets/d52abac3-22ba-4a5b-950b-d0c1bc8b9e3d">

**Note**: The application limits extraction to a maximum of 100 unique rows from the data source.

## Project Files

- **`app.py`**: Main Streamlit application file.
- **`loadData.py`**: Contains functions to load data from CSV or Google Sheets.
- **`infoExtraction.py`**: Handles data extraction using the Google Generative AI model.
- **`infoExtractionOfAll.py`**: Manages extraction of information from multiple rows in a DataFrame.
- **`webSearch.py`**: Provides functions to perform web searches and retrieve data.

## AI Model

This project utilizes Google’s **Generative AI model, "Gemini-1.5-flash,"** for high-quality information extraction, ensuring accurate and contextually relevant data insights.

## Example Data and Output

- **Sample Input**: [Input CSV file](https://docs.google.com/spreadsheets/d/1GSbjXCk2y1vE_YhpmV6RF21DHOLqaJf3DHYjhsOCYD8/edit?gid=0#gid=0).
- **Sample Output**: [Generated Output CSV](2024-11-08T16-19_export.csv), displaying extracted information.

## License

This project is licensed under the **MIT License**. See the LICENSE file for more details.
