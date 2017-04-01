import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome('/home/harsh/Desktop/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.facebook.com');
time.sleep(5) 
search_box = driver.find_element_by_name('email')
search_box.send_keys('@gmail.com')
#search_box.submit()
#time.sleep(5)
search_box = driver.find_element_by_name('pass')
search_box.send_keys('passwords_are_not_to_be_revealed')
search_box.submit()
src=requests.get("").text
time.sleep(5)
driver.get('http://www.facebook.com');
time.sleep(500) # Let the user actually see something!
driver.quit()
