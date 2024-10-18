from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython.display import HTML

driver = webdriver.Chrome()
HTML(driver.page_source)

url = 'http://localhost:8000/#/exemplo/1'
driver.get(url)

# XPATH é mais utilizado para arquivos XML
# Busca no caminho absoluto do elemento através da / ou //
# // Filtra por TAG
# / Filtra o caminho absoluto da TAG 

# Caminho ABSOLUTO
driver.find_elements(By.XPATH, '/html/body/div/div/div')

# Busca por TAG
driver.find_elements(By.XPATH, '//input')

# Busca por POSIÇÃO
# Retorna o primeiro input e o quarto input encontrados
driver.find_elements(By.XPATH, '//input[1] | //input[4]' )

# Busca por ATRIBUTOS
# deve ser colocado um @ antes do elemento
driver.find_elements(By.XPATH, '//input[@id="user"]')

# Busca por ATRIBUTOS CONCATENADOS
# Busca todas as TAGS <a> filhas da DIV que possui o id=social
# Duas //a seleciona todas as filhas
# Neste caso o /a[1] retorna a primeira filha direta encontrada
driver.find_elements(By.XPATH, '//div[@id="social"]/a[1]')