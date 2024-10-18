from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython.display import HTML

driver = webdriver.Chrome()
HTML(driver.page_source)

# Dentro da PROPRIEDADE dos ELEMENTOS da página (F12)
# Clicar com o botão direito em cima da propriedade desejada, opção COPIAR
# Na opção de seleção escolher o tipo de seletor que deseja

url = 'http://localhost:8000/#/exemplo/1'
driver.get(url)

seletor = driver.find_elements(By.CSS_SELECTOR, '#social > a:nth-child(1) > span')

xpath = driver.find_elements(By.XPATH, '//*[@id="user"]')
xpath
for i in xpath:
    value = i.get_property('value')
    print(value)

driver.quit()


