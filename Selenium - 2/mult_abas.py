from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from IPython.display import HTML

driver = webdriver.Chrome()
HTML(driver.page_source)

driver.get('http://localhost:8000/#/exemplo/1')

# Captura o ID das abas abertas
abas = driver.window_handles
print(abas)

# Dicionário
janelas = {
    'Exemplo 1' : 'E0CC47B2015588D5B246DC38CB02D339',
    'Exemplo 2' : ''
}

driver.switch_to.window(window_name=janelas['Exemplo 2'])


# Cria uma nova aba
driver.switch_to.new_window('tab')
driver.get('http.google.com')

# Cria uma nova janela
driver.switch_to.new_window('window')

# seleciona o item específico da lista de abas retornada
# aqui retorna o último item
driver.switch_to.window(window_name=driver.window_handles[-1])

# pega a url atual da página
driver.current_url


# Manipular alertas
driver.switch_to.new_window('tab')
driver.get('http://localhost:8000/#/exemplo5')
driver.find_element(By.CSS_SELECTOR, 'main button.btn-primari').click()

# muda o foco para o alerta
alert = driver.switch_to.alert

# dá o aceite do alert
alert.accept()
