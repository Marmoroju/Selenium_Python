from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from IPython.display import HTML


driver = webdriver.Chrome()
HTML(driver.page_source)
driver.get('http://localhost:8000/#/exemplo/8')
driver.maximize_window()

proximo = driver.find_element(By.XPATH, '//main//button[contains(text(), "Próxima")]')
ActionChains(driver).click(proximo)
ActionChains(driver).double_click(proximo).perform()

