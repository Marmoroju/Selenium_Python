from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from IPython.display import HTML
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
HTML(driver.page_source)
driver.get('http://localhost:8000/#/exemplo/2')
driver.maximize_window()
driver.implicitly_wait(time_to_wait=10) 

email = driver.find_element(By.NAME, 'email')
senha = driver.find_element(By.NAME, 'senha')

(
    ActionChains(driver)
    .send_keys_to_element(email, 'contato@email.com')
    .send_keys_to_element(senha, '123456')
    #.click()
    .send_keys_to_element(email, Keys.ENTER)
    .pause(5)
    .perform()
)

#forma 2

actions = ActionChains(driver)

actions.click(email)
actions.key_down(Keys.CONTROL)
actions.send_keys('a')
actions.key_up(Keys.CONTROL)
actions.send_keys(Keys.DELETE)
actions.perform()

actions = ActionChains(driver)
actions.click(senha)
actions.key_down(Keys.CONTROL)
actions.send_keys('a')
actions.key_up(Keys.CONTROL)
actions.send_keys(Keys.DELETE)
actions.perform()


actions.send_keys_to_element(email, 'contato2@email.com')
actions.send_keys_to_element(senha, '654321')
actions.send_keys_to_element(email, Keys.ENTER)
actions.perform()