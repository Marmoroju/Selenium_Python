from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from IPython.display import HTML
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


driver = webdriver.Chrome()
HTML(driver.page_source)
driver.get('http://localhost:8000/#/exemplo/7')
driver.maximize_window()
driver.implicitly_wait(time_to_wait=10) 

img = driver.find_element(By.ID, 'imagem_0')
scroll_origin = ScrollOrigin.from_element(img)

#ActionChains(driver).scroll_to_element(img).perform()

ActionChains(driver).scroll_from_origin(scroll_origin=scroll_origin, delta_x=0, delta_y=2000).perform()





