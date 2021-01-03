from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://stockcharts.com/")
elem = driver.find_element_by_id("nav-chartSearch-input")
elem.send_keys("spy")
elem.send_keys(Keys.RETURN)

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close() 