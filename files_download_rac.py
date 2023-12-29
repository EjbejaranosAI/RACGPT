import json
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_config(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        logger.error(f"Error reading config file: {e}")
        return None

def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def get_pdf_links(url_link, soup):
    pdf_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and '.pdf' in href:
            full_url = urljoin(url_link, href)
            pdf_links.append(full_url)
    return pdf_links

def download_pdf(pdf_url, save_path):
    if os.path.exists(save_path):
        logger.info(f"{save_path} already exists, skipping.")
        return
    try:
        response = requests.get(pdf_url, stream=True)
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.info(f"Downloaded {save_path}")
    except requests.RequestException as e:
        logger.error(f"Error downloading {pdf_url}: {e}")

def get_response(url_link):
    try:
        return requests.get(url_link)
    except requests.RequestException as e:
        logger.error(f"Error fetching {url_link}: {e}")
        return None

def get_rac_pdfs(target_url, storage_path, max_download_limit=None):
    create_directory(storage_path)
    response = get_response(target_url)
    if response:
        soup = BeautifulSoup(response.text, "html.parser")
        pdf_links = get_pdf_links(target_url, soup)
        num_pdfs_to_download = len(pdf_links) if max_download_limit is None else min(len(pdf_links), max_download_limit)

        for i, pdf_url in enumerate(pdf_links[:num_pdfs_to_download]):
            pdf_name = os.path.join(storage_path, f'document_{i}.pdf')
            download_pdf(pdf_url, pdf_name)
    else:
        logger.error("Failed to retrieve the webpage.")

def get_pdf_data():
    config = read_config('./config.json')
    if not config:
        logger.error("Failed to read configuration, exiting.")
        return

    # Accessing new variables from config
    project_name = config['project_name']
    download_settings = config['pdf_download_settings']
    targetUrl = download_settings['target_url']
    storagePath = download_settings['storage_path']
    maxDownloadLimit = download_settings.get('max_download_limit')  # This will be None if not set

    logger.info(f"Project Name: {project_name}")
    logger.info(f"Starting PDF download from: {targetUrl}")
    logger.info(f"Saving to: {storagePath}")
    logger.info(f"Maximum PDFs to download: {'All' if maxDownloadLimit is None else maxDownloadLimit}")

    # Download PDFs
    get_rac_pdfs(targetUrl, storagePath, maxDownloadLimit)

if __name__ == "__main__":
    get_pdf_data()
