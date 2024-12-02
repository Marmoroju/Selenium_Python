from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from IPython.display import HTML



driver = webdriver.Chrome()
HTML(driver.page_source)
driver.get('http://localhost:8000/#/exemplo/11')
#driver.get('https://www.magazineluiza.com.br')
driver.maximize_window()
driver.implicitly_wait(time_to_wait=10) 

logs = driver.log_types
#print(logs)

browser = driver.get_log('browser')
print(browser)

js = driver.execute_script('console.log("Olá, Mundo!")')
print(js)
