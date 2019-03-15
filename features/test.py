import time
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Chili Willy/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://www.wikipedia.org/")

search_field = driver.find_elements_by_id('searchInput')
search_field[0].send_keys('Колорадо') # return list not an object https://stackoverflow.com/questions/46880302/cant-send-keys-to-selenium-python?rq=1

search_button = driver.find_element_by_xpath("//*[@id='search-form']/fieldset/button")
search_button.click()
time.sleep(5)
assert "Колорадо" in driver.title #title in chrome

driver.quit()

