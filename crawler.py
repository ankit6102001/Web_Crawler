import requests
from parser import extract_links, extract_metadata
from storage import store_data_to_mongo
from utils import wait_randomly

visited_urls = set()

def crawl(url, max_depth=2, current_depth=0):
    if current_depth > max_depth:
        return
    
    if url in visited_urls:
        return
    
    visited_urls.add(url)
    
    print(f"Crawling: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving {url}: {e}")
        return
    
    title, description = extract_metadata(response.content)
    links = extract_links(response.content, url)
    
    data = {
        'url': url,
        'title': title,
        'description': description,
        'links': list(links), 
        'depth': current_depth
    }
    
    store_data_to_mongo(data)
    
    for link in links:
        wait_randomly()
        crawl(link, max_depth, current_depth + 1)
