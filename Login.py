from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')
stuff = driver.find_elements(By.CSS_SELECTOR, '.grayed b')[:-1]
names_of_items = [n.get_attribute('id') for n in driver.find_elements(By.CLASS_NAME, 'grayed')][:-1]

# Get the item prices in integer
item_prices = []
for m in stuff:
    item_prices.append(int(m.text.split()[-1].replace(',', '')))



timeout = time.time() + 5
five_min = time.time() + 30 # for 300 sec = 5min

while True:
    cookie.click()

    if time.time() > timeout:
        # A dict for item names and prices:
        upgrades = {}
        for i in range(len(item_prices)):
            upgrades[item_prices[i]] = names_of_items[i]

        # cookies I currently have
        present = driver.find_element(By.ID, 'money').text
        if "," in present:
            present = present.replace(",", "")
        present_cookie = int(present)

        # What can I get Currently:
        affordable = {}
        for cost,name in upgrades.items():
            if present_cookie > cost:
                affordable[cost] = name

        # The most expensive currently:
        max_price = max(affordable)
        print(max_price)
        id_of_item = affordable[max_price]

        driver.find_element(By.ID, id_of_item).click()


        # Waiting for another 5 seconds
        timeout = time.time() + 5

    # if time is over check for the cookie per seconds being clicked and stop the game
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, 'cps').text
        print(cookie_per_s)
        break






