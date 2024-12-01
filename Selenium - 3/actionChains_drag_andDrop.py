from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from IPython.display import HTML


driver = webdriver.Chrome()
HTML(driver.page_source)
driver.get('http://localhost:8000/#/exemplo/9')
driver.maximize_window()

drag = driver.find_element(By.ID, 'drag-source')
drop = driver.find_element(By.ID, 'drag-target')

ActionChains(driver).drag_and_drop(source=drag, target=drop).perform()

# Menu de contexto (quando clica com o botão direito do mouse)
# basicamente o selenium já realiza essas ações

img = driver.find_element(By.XPATH, '//*[@id="main-image"]/a/img')
ActionChains(driver).context_click(img).perform()