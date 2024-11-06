from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from IPython.display import HTML
import time

driver = webdriver.Chrome()
HTML(driver.page_source)

url = 'http://localhost:8000/#/exemplo/3'
driver.get(url)

selecao = Select(driver.find_element(By.NAME, 'regiao'))
for opt in selecao.options:
    print(opt.get_attribute('value'), opt.text)

# SELECIONAR ELEMENTO PELO VALUE, INDEX OU TEXTO    

selecao.select_by_value('0')
time.sleep(2)
selecao.select_by_value('1')
time.sleep(2)
selecao.select_by_index(2)
time.sleep(2)
selecao.select_by_visible_text('Mato Grosso do Sul')
time.sleep(2)

# RETORNAR OPÇÃO SELECIONADA
selecionado = selecao.first_selected_option.text
print(selecionado)


# SELEÇÃO MULTIPLA
# find_element -> Seleciona a DIV com id #multi-select e seleciona a primeira DIV dentro dela
# div mãe e div filha
multi = Select(driver.find_element(By.CSS_SELECTOR, '#multi-select select'))
for opt in multi.options:
    print(opt.get_attribute('value'), opt.text)

# SELECIONAR TODOS OS OBJETOS SELECIONADOS
multi.select_by_index(0)
multi.select_by_index(2)
for m in multi.all_selected_options:
    print(m.get_attribute('value'), m.text)    


# DESMARCAR OBJETOS SELECIONADOS
multi.deselect_by_index(0)
multi.deselect_all


#  SELECIONAR O SEGUNDO ELEMENTO DE CADA SELECT
all_selects = driver.find_elements(By.TAG_NAME, 'select')
for item in all_selects:
    select = Select(item)
    select.select_by_index(1)



