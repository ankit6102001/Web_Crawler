import time
import random
from urllib.parse import urlparse

def is_valid_url(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme in ['http', 'https']

def wait_randomly():
    time.sleep(random.uniform(1, 3))  
