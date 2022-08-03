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

def get_max_values(soup, tag_type, class_name, start_point, end_point):

    html_limit = soup.find_all(tag_type,{"class": class_name})[0].get_text()

    max_value = int((html_limit.strip())[len(html_limit.strip())-start_point:len(html_limit.strip())-end_point])
    
    return max_value