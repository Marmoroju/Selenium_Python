from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from IPython.display import HTML
import json, datetime

driver = webdriver.Chrome()
HTML(driver.page_source)

url = 'http://localhost:8000/#/desafio/1'
driver.get(url)

with open('./desafio1.json') as file:
    data = json.load(file)

for item in data:
    email = driver.find_element(By.NAME, 'email')    
    senha = driver.find_element(By.NAME, 'senha')

    email.clear()
    senha.clear()

    email.send_keys(item['email'])
    senha.send_keys(item['senha'])

    # conversão de data
    dt = datetime.datetime.strptime(item['data-de-nascimento'], '%Y-%m-%d')

    dia = Select(driver.find_element(By.NAME, 'dia'))
    mes = Select(driver.find_element(By.NAME, 'mes'))
    ano = Select(driver.find_element(By.NAME, 'ano'))

    # seleção com visible_text pois o campo de selação não tem index
    # conversão com str() pois no html é tratado como str, não int.
    dia.select_by_visible_text(str(dt.day))
    mes.select_by_visible_text(str(dt.month))
    ano.select_by_visible_text(str(dt.year))

    # seleção do switch de newsletter
    newsletter = driver.find_element(By.ID, 'airplane-mode')
    switch_on = True if newsletter.get_attribute('aria-checked') == 'true' else False

    if switch_on != item['newsletter']:
        newsletter.click()

    email.submit()
