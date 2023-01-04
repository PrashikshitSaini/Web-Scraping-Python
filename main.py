# ADVANCED WEB SCRAPING
# SELENIUM WEBDRIVER - A more powerful web scraper
# Can also help interact with the websites like clicks and automate google forms or data from excel or any sheet
# Can interact with all the web Browser in an automated manner.
# And Yeah Read the doxumneataion  for different web browser

from selenium import webdriver
from selenium.webdriver.common.by import By

edge_driver_path = "D:\eDGE dRIVER\msedgedriver"
driver = webdriver.ChromiumEdge(executable_path=edge_driver_path)

driver.get("https://www.amazon.in/Unchartered-Legacy-Thieves-Collection-PlayStation/dp/B09N9MBVD1/ref=sr_1_8?crid=3PABCGNEPHDPD&keywords=ps5&qid=1672724775&sprefix=ps%2Caps%2C241&sr=8-8")
name = driver.find_element(By.CLASS_NAME, "a-price-whole" )  # Find Element by Name, class, id, CSS Selector
print(name.text)
# driver.quit()

# Xpath - Locating a specific HTML element using a Path Structure
# When Nothing works, XPATH will work
# Copy the XPATH of the element you want and paste in the get with comas
