from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from IPython.display import HTML


driver = webdriver.Chrome()
HTML(driver.page_source)
driver.get('http://localhost:8000/#/exemplo/7')
driver.maximize_window()

img = driver.find_element(By.ID, 'imagem_0')


#xoffset > 0 movimenta para direnta \\ xoffset < 0 movimenta para esquerda
#yoffset > 0 movimenta para baixo \\ yoffset < 0 movimenta para cima
ActionChains(driver).move_to_element(img).perform()
ActionChains(driver).move_by_offset(xoffset=0, yoffset=80).perform()


