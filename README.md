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

   This will create a `.venv` directory within your project folder and install the required dependencies as specified in the `pyproject.toml` file.

1. **Activate the Virtual Environment**:
   To activate the virtual environment, use the following command:

   ```bash
   source .venv/bin/activate
   ```

   On Windows, the command might differ slightly:

   ```cmd
   .\.venv\Scripts\activate
   ```
1. Install [Docker](https://docs.docker.com/engine/install/)
1. Install [just](https://github.com/casey/just)
1. Install [Helm](https://helm.sh/docs/intro/install/)
1. Install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)
1. Install [minikube](https://minikube.sigs.k8s.io/docs/start/)


### Running the Script

#### Download sep index

```bash
python sep_crawler.py
```

Or, to set the index URL and output folder using command-line arguments:

```bash
python sep_crawler.py --url https://plato.stanford.edu/archives/sum2023/contents.html --output_folder data/html/sum2023
```

The script will create the output directory if it doesn't exist, fetch each linked page from the index page, and save the content in the specified output folder.

#### Convert entries to Markdown

```bash
python sep_to_markdown.py data/html
```

This will convert all the HTML files in the `data/html` directory to Markdown and save them to the `data/html/md` directory.

You can also specify a custom output folder using the `--output_folder` argument:

```bash
python sep_to_markdown.py data/html --output_folder data/markdown
```
