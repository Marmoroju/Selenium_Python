from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython.display import HTML

driver = webdriver.Chrome()
HTML(driver.page_source)

url = 'http://localhost:8000/#/exemplo/1'
driver.get(url)

campos = driver.find_elements(By.TAG_NAME, 'input')
campos
for campo in campos:
    valor = campo.get_property('value')
    print(valor)

print('\n')
# CONCATENAR BUSCAS PARA FILTRAR MELHOR

rede_social = driver.find_element(By.ID, 'social').find_elements(By.TAG_NAME, 'span')
rede_social
for rs in rede_social:
    valor = rs.get_property('innerText')
    print(valor)