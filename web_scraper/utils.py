from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_soup(url):

    """
    Function to get html parser with BeautifulSoup.
    """
    
    u = urlopen(url)

    try:
        html = u.read().decode('utf-8')
    finally:
        u.close()

    soup = BeautifulSoup(html, 'html.parser')

    return soup