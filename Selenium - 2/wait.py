from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from IPython.display import HTML
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
HTML(driver.page_source)

driver.get('http://localhost:8000/#/exemplo/4')

# IMPLICITLY_WAIT 
# Aguarda até 10 segundos carregar qualquer elemento da página
# Caso de uso: Quando testar em diferentes navegadres e tipos de latência
driver.implicitly_wait(time_to_wait=10) 
teste2 = driver.find_element(By.ID, 'vantagens')
print(teste2)

# WAIT / UNTIL
# Define o tempo de espera para cada elemento especifico da consulta
# Caso de uso: Testar componente específico da página antes de levantar exceção

#teste = wait.until(EC.presence_of_element_located(locator=(By.ID, 'vantagens')))
#print(teste)
#print(teste.get_attribute('innerText'))
'''
#TRATAMENTO DE ERRO
wait = WebDriverWait(driver=driver, timeout=2, poll_frequency=0.5)
try:
    wait.until(
        method=EC.presence_of_element_located(locator=(By.ID, 'vantagens')),
        message='Não encontrado o componente de ID="vantagens"'
    )
except Exception as e:
    print(e.msg)
'''



