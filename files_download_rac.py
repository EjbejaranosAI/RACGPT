import json
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Path to your config.json file
config_file_path = './config.json'

# Read the config.json file
with open(config_file_path, 'r') as file:
    config = json.load(file)

# Accessing variables from the config file
name = config['name']
url = config['url']
data_location = config['data_location']

def get_rac_pdfs(url_link, data_location, max_pdfs=None):
    # Create directory if it does not exist
    if not os.path.exists(data_location):
        os.mkdir(data_location)

    response = requests.get(url_link)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all links on the page
    links = soup.find_all('a')

    # Filter out the links to PDFs
    pdf_links = [urljoin(url_link, link.get('href')) for link in links if link.get('href') and '.pdf' in link.get('href')]

    # Determine the number of PDFs to download
    num_pdfs_to_download = len(pdf_links) if max_pdfs is None else min(len(pdf_links), max_pdfs)

    for i in range(num_pdfs_to_download):
        pdf_url = pdf_links[i]
        response = requests.get(pdf_url)
        pdf_name = os.path.join(data_location, f'document_{i}.pdf')

        with open(pdf_name, 'wb') as file:
            file.write(response.content)
        print(f'Downloaded {pdf_name}')

# Use the variables in your project
print(name)
print(url)
print(data_location)

# Example usage: Download up to 3 PDFs
get_rac_pdfs(url, data_location, max_pdfs=3)

