from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from IPython.display import HTML
import urllib.request, os

driver = webdriver.Chrome()
HTML(driver.page_source)

driver.get('http://localhost:8000/#/exemplo/7')
driver.implicitly_wait(time_to_wait=10)

# Selecionar o elemento principal pela div
imagens = driver.find_elements(By.CSS_SELECTOR, '#galeria img')

# importação de modulos para ser possível 
# import urllib.request ->  faz requisição para o link e obtém os dados da imagem
# import os ->  possibilita trabalhar com o sistema operacional

for img in imagens:
    
    # captura o link da imagem
    img_src = img.get_property('src')

    # captura o id da imagem que será utilizada como nome
    img_id = img.get_property('id')
    #print(img_id, img_src)

    # verifica se existe o diretório antes de criar
    if not os.path.exists('./imagens'):
        os.mkdir('./imagens')

    # variável para salvar a imagem com o nome e extensão
    file = img_id + '.jpg'

    # informa o diretório onde será salvo junto ao nome do arquivo baixado
    filename = os.path.join('./imagens', file)

    # faz o download
    urllib.request.urlretrieve(img_src, filename)

