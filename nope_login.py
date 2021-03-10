from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time

# Instantiate the driver. choose options
fp = webdriver.FirefoxProfile()
mime_types = [
    'text/plain', 
    'application/vnd.ms-excel', 
    'text/csv', 
    'application/csv', 
    'text/comma-separated-values', 
    'application/download', 
    'application/octet-stream', 
    'binary/octet-stream', 
    'application/binary', 
    'application/x-unknown'
]
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", ",".join(mime_types))

driver = webdriver.Firefox(firefox_profile=fp)
# driver = webdriver.Chrome()
# def driver_selector():
#     driver_list = [Chrome, Firefox]

#define the payload. 
payload = {
    'username': 'myname@myemail.com',
    'password': 'mypassword'
}

#define request URL
PREMIUM_URL = 'https://nopechart.com/premium'
REQUEST_URL = 'https://nopechart.com/csv'

#create login script
def site_login(URL):
    driver.get(URL)
    driver.find_element_by_id('username').send_keys(payload.get('username'))
    driver.find_element_by_id('password').send_keys(payload.get('password'))
    driver.find_element_by_xpath('.//*[@class="c6069c11a cf6cae695 c495fb6b5 ca4c2ddb1 c65e1117c"]').click()

#execute login
site_login(REQUEST_URL)
try:
    element = WebDriverWait(driver, 10). until(
        EC.presence_of_element_located((By.XPATH, './/*[@class="nav-link"][@href="/csv"]'))
        )
finally:
    driver.get(REQUEST_URL)


time.sleep(5)
driver.get(REQUEST_URL)


#open the csv path
# driver.find_element_by_xpath('.//*[@class="nav-link"][@href="/csv"]').click()

# ticker_list = ['']
# To-Do create a ticker list to loop through

# Opens the ticker
driver.find_element_by_xpath('.//*[@class="form-control"][@name="ticker"]').click()
ticker = driver.find_element_by_xpath('.//*[@class="form-control"][@name="ticker"]')
for option in ticker.find_elements_by_tag_name('option'):
    if option.text == 'TSLA': # this could be automated to loop through a list
        option.click() # select() in earlier versions of webdriver
        break

# Option1 for date - create a URL & call

# DATED_URL = 'https://nopechart.com/csv?ticker=CLOV&date=2021-03-01'
# driver.get(DATED_URL)
# time.sleep(5)

# Option 2 for date - try to pick date
#Opens the date picker
# Opens the calendar
# driver.find_element_by_xpath('.//input[@class="form-control"][@name="date"]').click()

#get calendar elements
# time.sleep(5)
# date_selector = driver.find_element_by_xpath('.//*[@id="date"]')
# date_selector = driver.find_element_by_xpath('.//input[@class="form-control"][@id="date"]')
# ActionChains(driver).move_to_element(date_selector).click().send_keys('2021-03-04').perform()


# Opens the download CSV button
try:
    element = WebDriverWait(driver, 10). until(
        EC.presence_of_element_located((By.XPATH, './/*[@class="dt-button buttons-csv buttons-html5"]'))
        )
finally:
    driver.find_element_by_xpath('.//*[@class="dt-button buttons-csv buttons-html5"]').click()
    