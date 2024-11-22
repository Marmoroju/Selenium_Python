from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from IPython.display import HTML
import pandas as pd
from io import StringIO


driver = webdriver.Chrome()
HTML(driver.page_source)

driver.get('http://localhost:8000/#/exemplo/8')
driver.implicitly_wait(time_to_wait=10)

# PANDAS pesquisa o texto de todas as tabelas da url
# Aqui ele está buscando somente a tabela com id = tabela-usuarios
strio = StringIO(initial_value=driver.page_source)
tab = pd.read_html(io=strio, attrs={'id': 'tabela-usuarios'})[0]
print(tab)