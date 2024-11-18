from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_links(page_content, base_url):
    soup = BeautifulSoup(page_content, 'html.parser')
    links = set()

    for anchor in soup.find_all('a', href=True):
        href = anchor['href']
        full_url = urljoin(base_url, href)
        links.add(full_url)
    
    return links

def extract_metadata(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    title = soup.title.string if soup.title else 'No title'
    description = ''
    
    meta_description = soup.find('meta', attrs={'name': 'description'})
    if meta_description:
        description = meta_description.get('content', 'No description')
    
    return title, description
