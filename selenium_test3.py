import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
driver = webdriver.Chrome('/home/harsh/Desktop/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.facebook.com/');
time.sleep(1) 
search_box = driver.find_element_by_name('email')
search_box.send_keys('Email')
#search_box.submit()
#time.sleep(5)
search_box = driver.find_element_by_name('pass')
search_box.send_keys('password')
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
src=driver.page_source
soup=bs(src,"html.parser")
soup1=soup.find_all('a',class_="_6-6")
for i in soup1:
	if i["data-tab-key"] == "friends" :
		k=i["href"]
		break

print k
link=k
print "done"
driver.get(link);
src=driver.page_source
soup=bs(src,"html.parser")
soup1=soup.find_all('a',class_="_3c_")
for i in soup1:
	if i["name"] == "Birthdays" :
		k=i["href"]
		break

print k
link=k
print "done"
driver.get(link);
src=driver.page_source
soup=bs(src,"html.parser")
soup1=soup.find_all('div',class_="_3i9")[0]
soup2=soup1.find_all('a',class_="pvs _39g5")
#_50f8 _50f4
print "2"
for i in soup2:
	print "1"
	soup3=i.find_all('div',class_="_50f8 _50f4")[0]
	title="".join([str(j) for j in soup3.contents])
	print title
	if title == "Birthday is in 3 days" :
		k=i["href"]
		break
print k
link=k
print "done"
driver.get(link);
#use the #collection_wrapper_2356318349 to uniquely pinpoint birthdays
time.sleep(100) # Let the user actually see something!
driver.quit()
