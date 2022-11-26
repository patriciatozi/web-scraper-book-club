from etl import web_scraping_booklist
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

web_scraping_booklist(driver)