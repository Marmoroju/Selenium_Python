from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from IPython.display import HTML
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
HTML(driver.page_source)
driver.get('https://google.com')
driver.maximize_window()
driver.implicitly_wait(time_to_wait=10) 



# driver.get_cookie('ola')
cookies = driver.get_cookies()
# driver.delete_cookies('')
# driver.delete_all_cookies()
print(cookies)


