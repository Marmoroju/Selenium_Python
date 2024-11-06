from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import  webdriver
from IPython.display import HTML


driver = webdriver.Chrome()
HTML(driver.page_source)

url = 'http://localhost:8000/#/exemplo/2'
driver.get(url)


# SELECIONA OS CAMPOS QUE SERÃO PREENCHIDOS
email = driver.find_element(By.NAME, 'email')
senha = driver.find_element(By.NAME, 'senha')
enviar = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]' )

# INSERE DADOS NOS CAMPOS SELECIONADOS
email.send_keys('marcos@email.com')
senha.send_keys('abc123')
enviar.click()
email.clear()
senha.clear()


email.send_keys('martha@email.com')
senha.send_keys('abc321')
enviar.click()



# ACESSA BOTÃO DE ENVIO PERTENCENTE AO ELEMENTO DO MESMO FORMULÁRIO
email.clear()
senha.clear()
email.send_keys('marcos2@email.com')
senha.send_keys('123456')
email.submit()


# SIMULAR TECLA
email.clear()
senha.clear()

email.send_keys('outroemail@email')
senha.send_keys('qweasd')

email.send_keys(Keys.ENTER)
