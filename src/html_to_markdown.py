import argparse
import os
from markdownify import MarkdownConverter
from bs4 import BeautifulSoup

def all_to_markdown(source_folder: str, output_folder: str):
    for file in os.listdir(source_folder):
        if file.endswith('.html'):
            filepath = os.path.join(source_folder, file)
            output_file = os.path.join(output_folder, os.path.split(filepath)[-1].replace('.html', '.md'))
            convert_to_markdown(filepath, output_file)

def convert_to_markdown(source_file: str, output_file: str):
    soup = read_as_soup(source_file)
    with open(output_file, 'w+', encoding='utf8') as f:
        f.write(md(soup))

def read_as_soup(filepath: str) -> BeautifulSoup:
    with open(filepath, encoding='utf8') as f:
        return BeautifulSoup(f, 'html.parser')
    
def md(soup: BeautifulSoup, **options) -> str:
    return MarkdownConverter(**options).convert_soup(soup)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_folder', '-f', default=os.path.join('data', 'html'), help='The folder containing the HTML files to convert.')
    parser.add_argument('--output_folder', '-o', help='The folder to save the Markdown files to. Defaults to the {source_folder}/md/')
    args = parser.parse_args()

    if not args.output_folder:
        args.output_folder = os.path.join(args.source_folder, 'md')
    
    os.makedirs(args.output_folder, exist_ok=True)

    all_to_markdown(args.source_folder, args.output_folder)


if __name__ == '__main__':
    main()