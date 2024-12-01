from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from IPython.display import HTML
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
HTML(driver.page_source)
driver.get('http://localhost:8000/#/exemplo/9')
driver.maximize_window()

titulo = driver.find_element(By.CSS_SELECTOR, 'main div.title')
ActionChains(driver).double_click(titulo).click(titulo)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()

