import logging
from requests import get
from selenium import webdriver
from web_scraper.utils import get_soup
from web_scraper.constants import main_url
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

soup = get_soup(main_url)

html_limit = soup.find_all("form",{"class": "form-horizontal"})[0].get_text()
max_value = int((html_limit.strip())[-3:-1])

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(main_url)

# print(driver.page_source)

for i in range(0,max_value):


    # Open a new window
    driver.execute_script("window.open('');")
    
    # Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[1])

    driver.get(main_url)

    driver.find_elements(By.CLASS_NAME, 'image_container')[i].click()
    time.sleep(1)

    # Closing new_url tab
    driver.close()
    
    # Switching to old tab
    driver.switch_to.window(driver.window_handles[0])

driver.quit()
