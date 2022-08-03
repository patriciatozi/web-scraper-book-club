from requests import get
from selenium import webdriver
from web_scraper.utils import get_soup
from web_scraper.constants import main_url
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def web_scraping_booklist():

    start_time = time.time()

    soup = get_soup(main_url)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(main_url)
    number_of_books = 0
    # print(driver.page_source)

    page_limit = soup.find_all("li",{"class": "current"})[0].get_text()
    max_value_page = int((page_limit.strip())[len(page_limit.strip())-2:len(page_limit.strip())])

    for n in range(0, max_value_page):

        books_limit = soup.find_all("form",{"class": "form-horizontal"})[0].get_text()
        max_value_books = int((books_limit.strip())[-3:-1])

        for i in range(0,max_value_books):

            # Open a new window
            driver.execute_script("window.open('');")
            
            # Switch to the new window and open new URL
            driver.switch_to.window(driver.window_handles[1])

            driver.get(main_url + 'catalogue/page-'+ str(n+1) +'.html')

            driver.find_elements(By.CLASS_NAME, 'image_container')[i].click()

            # Closing new_url tab
            driver.close()
            
            # Switching to old tab
            driver.switch_to.window(driver.window_handles[0])

        if n < max_value_page:
            driver.get(main_url + 'catalogue/page-'+ str(n+2) +'.html')

    driver.quit()
    print("--- %s seconds ---" % (time.time() - start_time))