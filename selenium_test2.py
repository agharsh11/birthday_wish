import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
driver = webdriver.Chrome('/home/harsh/Desktop/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.facebook.com/');
time.sleep(1) 
search_box = driver.find_element_by_name('email')
search_box.send_keys('your_email')
#search_box.submit()
#time.sleep(5)
search_box = driver.find_element_by_name('pass')
search_box.send_keys('your_password')
search_box.submit()
#src=requests.get("").text
time.sleep(5)
src=driver.page_source
soup=bs(src,"html.parser")
soup1=soup.find_all('a',class_="_2s25")[0]
print soup1
link=soup1["href"]
#driver.find_elements_by_class_name("_2s25")[0].is_selected
#driver2 = webdriver.Chrome('/home/harsh/Desktop/chromedriver')  # Optional argument, if not specified will search path.
driver.get(link);
print "done"
time.sleep(100) # Let the user actually see something!
driver.quit()
