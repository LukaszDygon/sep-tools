import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_index_page(url: str, output_folder: str):
    # Send a GET request to the index page
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the div with id 'content'
        content_div = soup.find('div', id='content')
        if content_div:
            # Find all anchor tags with relative href attributes within the 'content' div
            links = content_div.find_all('a', href=True)
            for link in links:
                href = link['href']
                # Join the relative URL with the base URL to get the absolute URL
                absolute_url = urljoin(url, href)
                # Fetch content from the linked page
                fetch_content(absolute_url, output_folder)
        else:
            print('No content div found on the index page')
    else:
        print('Failed to fetch the index page')

def fetch_content(url: str, output_folder: str):
    output_file = os.path.join(output_folder, f'{url.split('/')[-2]}.html')

    if os.path.exists(output_file):
        print(f'File {output_file} exists. Skipping:', url)
        return

    print('Fetching:', url)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article_div = soup.find('div', id='article')
        if article_div:
            print('Writing content to:', output_file)
            with open(output_file, 'w+') as f:
                f.write(str(article_div))
        else:
            print('No content found for:', url)
    else:
        print('Failed to fetch page:', url)

index_url = 'https://plato.stanford.edu/archives/spr2024/contents.html'
output_folder = os.path.join('data', 'html')
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
crawl_index_page(index_url, output_folder=output_folder)