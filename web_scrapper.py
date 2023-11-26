import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to search for text on a page
def search_text_on_page(url, text_to_search):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            occurrences = soup.find_all(text=lambda text: text and text_to_search in text)
            if occurrences:
                print(f"Found {len(occurrences)} occurrences of '{text_to_search}' at: {url}")
    except Exception as e:
        print(f"Error accessing the page {url}: {e}")

# Function to get all links from a page
def get_page_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            return [urljoin(url, link['href']) for link in links]
    except Exception as e:
        print(f"Error getting links from the page {url}: {e}")
    return []

# Function to recursively crawl the website
def crawl_website(url, text_to_search, visited=set()):
    if url in visited:
        return
    visited.add(url)
    print(f"Exploring: {url}")
    search_text_on_page(url, text_to_search)
    links = get_page_links(url)
    for link in links:
        crawl_website(link, text_to_search, visited)

# Starting URL for crawling
start_url = 'https://' #WEB TO SEARCH
text_to_search = 'miau' #STRING TO SEARCH

crawl_website(start_url, text_to_search)
