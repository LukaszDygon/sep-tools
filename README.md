# SEP Crawler

## Overview

SEP Crawler is a Python script designed to automatically download and save HTML content from the Stanford Encyclopedia of Philosophy (SEP) index page for a specific archive (e.g., Spring 2024). The script navigates through each link found in the designated content division of the SEP archive index page, fetches the linked pages, and saves the HTML content of each page into separate files within a specified directory.

## How to Run

Before running SEP Crawler, ensure you have Python 3 and Poetry installed.

### Setting Up the Environment

1. **Create and Activate a Virtual Environment**:
   Use Poetry to create and manage a virtual environment. Navigate to the project directory and run:

   ```bash
   poetry config virtualenvs.in-project true
   poetry install
   ```

   This will create a `.venv` directory within your project folder and install the required dependencies (`requests`, `beautifulsoup4`) as specified in the `pyproject.toml` file.

2. **Activate the Virtual Environment**:
   To activate the virtual environment, use the following command:

   ```bash
   source .venv/bin/activate
   ```

   On Windows, the command might differ slightly:

   ```cmd
   .\.venv\Scripts\activate
   ```

### Running the Script

1. **Set the Index URL and Output Folder**: At the bottom of the `sep_crawler.py` script, set the `index_url` variable to the URL of the SEP archive index page you want to crawl. Also, specify the `output_folder` where the HTML files will be saved.

2. **Execute the Script**: Run the script from your command line within the activated virtual environment:

   ```bash
   python sep_crawler.py
   ```

   The script will create the output directory if it doesn't exist, fetch each linked page from the index page, and save the content in the specified output folder.

### Output

The script saves each fetched page's content in an HTML file named after the last segment of the page's URL. These files are stored in the directory specified by the `output_folder` variable.

### Customization

You can customize the script by modifying the `index_url` and `output_folder` to point to different SEP archives or save locations.
