from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython.display import HTML

driver = webdriver.Chrome()
HTML(driver.page_source)

url = 'http://localhost:8000/#/exemplo/1'
driver.get(url)

'''
CSS_SELECTOR
# Seleção de ID
. Seleção de Classe
> Seleção de Filhos Diretos
~ Seleção de Irmãos
+ Seleção de Irmão Imediato
* Seleciona todos os valores
[property="value"] Seleção de Propriedades
    ^= Corresponde a um Prefixo
    $= Corresponde a um Sufixo
    *= Corresponde a uma Substring
    |= Corresponde a um texto seguido por Hífen
    ~= Corresponde a uma palavra
'''

# ID
# É possível restringir, por exemplo, somente as TAGS (div) que contenham o determinado ID
id = driver.find_element(By.CSS_SELECTOR, 'div#social')

# CLASS
# É possível restringir, por exemplo, somente as TAGS (input) que contenham a determinada ou determinadas CLASSES
classe = driver.find_elements(By.CSS_SELECTOR, 'input.styled-input.optional-info')

# PARENTESCO
# É possível restringir, por exemplo, a busca somente dentro de uma TAG `main` e ao dar espaço insere o que deseja buscar nela
parent = driver.find_elements(By.CSS_SELECTOR, 'div.main-container input.optional-info')

# Selecionar apenas determinadas tags em uma DIV com o ID #social
# Aqui irá trazer todos os nomes das redes sociais da página
link = driver.find_elements(By.CSS_SELECTOR, 'div#social > a')

#link
#for l in link:
#    value = l.get_property('innerText')
#    print(value)
#
#driver.quit()

# Retorna todo o parentesco da div e classe main-container
todoParentesco = driver.find_elements(By.CSS_SELECTOR, 'div.main-container *')

# Retorna todos os atributos da classe #social e seus parentescos

link = driver.find_elements(By.CSS_SELECTOR, 'div#social > *')
#for lk in link:
#    print(lk.tag_name, '=>', lk.get_property('className'))


## PROPRIEDADES E ATRIBUTOS ##

# Encontra todas as tags input que contenha a propriedade name=fullname
driver.find_elements(By.CSS_SELECTOR, 'input[name="fullname"]')

# Encontra todas as tags input que contenha apenas a propriedade definida e ainda refinar a busca
driver.find_elements(By.CSS_SELECTOR, 'input[disable]')

driver.find_elements(By.CSS_SELECTOR, 'input[disable] [data-optinonal="true]')

# Busca por SUFIXO
driver.find_elements(By.CSS_SELECTOR, 'input[value$="ino"]')
driver.find_elements(By.CSS_SELECTOR, '[class$="gram"]')

# Busca por PREFIXO
driver.find_elements(By.CSS_SELECTOR, '[name^="user"]')

# Busca por palavra que contenha HÍFEN
driver.find_elements(By.CSS_SELECTOR, '[class|="text"]')

# Busca por SUBSTRING que contenha um determinado caractere
driver.find_elements(By.CSS_SELECTOR, 'input[id*="e"]')