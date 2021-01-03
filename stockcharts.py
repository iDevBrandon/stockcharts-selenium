from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
 
driver = webdriver.Chrome()
driver.get("https://stockcharts.com/")
elem = driver.find_element_by_id("nav-chartSearch-input")
elem.send_keys("spy")
elem.send_keys(Keys.RETURN)
time.sleep(3)
imgUrl = driver.find_element_by_css_selector(".chartimg").get_attribute("src")

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(imgUrl, "test.jpg")

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close() 