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

proximo = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div[2]/div/div[3]/button[2]')
# ActionChains(driver).click(proximo).pause(5).double_click(proximo).perform()

ActionChains(driver).click_and_hold(proximo).pause(3).release().perform()