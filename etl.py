from requests import get
from web_scraper.utils import get_soup, get_max_values
from web_scraper.constants import main_url
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

def web_scraping_booklist(driver):

    start_time = time.time()

    soup = get_soup(main_url)

    driver.maximize_window()

    driver.get(main_url)

    max_value_page = get_max_values(soup, "li", "current", 2, 0)

    dataframe = pd.DataFrame(columns=['id','title', 'description'])

    dataframe = dataframe.set_index('id')

    for n in range(0, max_value_page):

        max_value_books = get_max_values(soup, "form", "form-horizontal", 3, 1)

        dataframe = iterate_book_list(driver, max_value_books, n, dataframe)

        if n < max_value_page:
            driver.get(main_url + 'catalogue/page-'+ str(n+2) +'.html')
    
    dataframe.to_csv('results/books_list.csv', sep=';')

    driver.quit()
    
    print("--- %s seconds ---" % (time.time() - start_time))


def iterate_book_list(driver, max_value, n, dataframe):

    for i in range(0,max_value):

            driver.execute_script("window.open('');")
            
            driver.switch_to.window(driver.window_handles[1])

            driver.get(main_url + 'catalogue/page-'+ str(n+1) +'.html')

            driver.find_elements(By.CLASS_NAME, 'image_container')[i].click()

            dataframe = get_book_details(driver, dataframe, n)

            driver.close()
            
            driver.switch_to.window(driver.window_handles[0])

    return dataframe

def get_book_details(driver, dataframe, n):

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    dataframe = dataframe.append({'title': soup.find_all('h1')[0].get_text(),
                                   'description': soup.find_all('p')[3].get_text()},
                                   ignore_index=True)

    return dataframe