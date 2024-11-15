from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from IPython.display import HTML


driver = webdriver.Chrome()
HTML(driver.page_source)

driver.get('http://localhost:8000/#/exemplo/6')
driver.implicitly_wait(time_to_wait=10)

# Captura do ID e estanciando na variável estados
estados = driver.find_element(By.ID, 'estados')

# Obtendo o atributo CLASS da div com id='estados'
# atributo = flex flex-wrap justify-start lg:mx-auto gap-8 text-left
atributo = estados.get_attribute('class')
print(atributo)

id_nome = estados.get_attribute('id')
print(id_nome)

# Capturando a Propriedade <> de Atributo
# #Propriedade é DOM da página, que busca pelo nome da CLASS (className) 
# ao invés de buscar pelo atributo 'class' para não dar conflito
# do CSS com o JAVASCRIPT da página.
# get_attribute('class','id', ...) = CSS 
# get_property('className', 'id', ...) = JAVASCRIPT
estados.get_property('className')


# PROPRIEDADE CHILDREN do elemento id=estados no navegador
children = estados.get_property('children')

for child in children:
    # Faz uma iteração na variável children e retorna o valor de cada item
    #print(child.text)

    # Recebe o retorno da iteração anterior para cada children de outra children
    cchild = child.get_property('children') 

    # Faz a iteração com os dados recebidos
    # e imprime caso atenda as condições
    for cc in cchild:
        if cc.tag_name == 'label':
            print(cc.text)
        
        if cc.tag_name == 'div':
            print(f' \t - {cc.text}')

# DATASET -> Propriedade -> data-country, data-timezone, data-language, data-location
# O DATASET está relacionado a toda propriedade iniciada por data-

data = estados.get_property('dataset')
print(data)

# OUTERHTML -> através da biblioteca from IPython.display import HTML
outer = HTML(estados.get_property('outerHTML'))
print(outer)

# Obter tamanho de determinado componente, neste caso, o size da div estados
tam = estados.size
print(tam)

# Location -> retorna localização do componente na tela
loc = estados.location
print(loc)

# Size e location

sizeLoc = estados.rect
print(sizeLoc)

# Obter propriedades do CSS do elemento
# aba COMPUTED
cssElemento = estados.value_of_css_property('border-top-color')
print(cssElemento)

# tag_name -> Obtem estrutura de componentes
print(estados.tag_name)
for estado in estados.get_property('children'):
    print(f'- {estado.tag_name}' )



driver.quit()