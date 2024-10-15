from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython.display import HTML

driver = webdriver.Chrome()
HTML(driver.page_source)

url = 'http://localhost:8000/#/exemplo/1'
driver.get(url)

#Busca com o texto exato na tag link (<a>) text
driver.find_elements(By.LINK_TEXT, 'Instagram')

#Busca elementos na tag link (<a>) que contenham 'gram' em seu texto
gram = driver.find_elements(By.PARTIAL_LINK_TEXT, 'gram')
gram
for g in gram:
    value = g.get_property('innerText')
    print(value)

driver.quit()