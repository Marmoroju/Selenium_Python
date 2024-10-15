from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython.display import HTML

driver = webdriver.Chrome()
HTML(driver.page_source)

driver.get('http://localhost:8000/#/exemplo/1')

nome = driver.find_element(By.ID, 'user').get_property('value')
profissao = driver.find_element(By.ID, 'role').get_property('value')
signo = driver.find_element(By.ID, 'zodiac').get_property('value')
genero = driver.find_element(By.ID, 'gender').get_property('value')

print('Dados do Usuário')
print(f'Nome: {nome}')
print(f'Profissão: {profissao}')
print(f'Signo: {signo}')
print(f'Gênero: {genero}')