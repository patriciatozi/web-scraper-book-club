from requests import get
from selenium import webdriver
from web_scraper.utils import get_soup, get_max_values
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

    max_value_page = get_max_values(soup, "li", "current", 2, 0)

    for n in range(0, max_value_page):

        max_value_books = get_max_values(soup, "form", "form-horizontal", 3, 1)

        for i in range(0,max_value_books):

            driver.execute_script("window.open('');")
            
            driver.switch_to.window(driver.window_handles[1])

            driver.get(main_url + 'catalogue/page-'+ str(n+1) +'.html')

            driver.find_elements(By.CLASS_NAME, 'image_container')[i].click()

            driver.close()
            
            driver.switch_to.window(driver.window_handles[0])

        if n < max_value_page:
            driver.get(main_url + 'catalogue/page-'+ str(n+2) +'.html')

    driver.quit()
    
    print("--- %s seconds ---" % (time.time() - start_time))