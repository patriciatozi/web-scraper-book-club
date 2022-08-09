from web_scraper.utils import get_soup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
import string
import time

main_url = 'http://books.toscrape.com/'

soup = get_soup(main_url)

books_limit = soup.find_all("form",{"class": "form-horizontal"})[0].get_text()
max_value_books = int((books_limit.strip())[len(books_limit.strip())-3:len(books_limit.strip())-1])

print(type(max_value_books))
print(max_value_books)

page_limit = soup.find_all("li",{"class": "current"})[0].get_text()
max_value_page = int((page_limit.strip())[len(page_limit.strip())-2:len(page_limit.strip())])
print(max_value_page)

print(soup.find_all("li",{"class": "next"})[0])

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(main_url)

# driver.find_element(By.CSS_SELECTOR, 'div.pager.next').click()
# driver.find_element(By.CSS_SELECTOR, '.pager.next').click()
n =2
time.sleep(2)
driver.get(main_url + 'catalogue/page-'+ str(n) +'.html')
time.sleep(2)

driver.quit()