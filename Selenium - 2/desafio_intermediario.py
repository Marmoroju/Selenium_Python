from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from IPython.display import HTML
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, csv
from dataclasses import dataclass, asdict, fields



driver = webdriver.Chrome()
HTML(driver.page_source)

driver.get('http://localhost:8000/#/desafio/2')
driver.implicitly_wait(time_to_wait=10)


#BUSCAR DADOS DE USUARIOS
driver.refresh()

@dataclass # torna a classe Usuario uma classe de dados, assim cria uma instância/objeto com os dados solicitados.
class Usuario:
    foto: str
    nome: str
    profissao: str
    email: str
    telefone: str
    perfil: str
    estado: str

inp = driver.find_element(By.CSS_SELECTOR, 'main input[type="text"]')
botao = driver.find_element(By.CSS_SELECTOR, 'main button')

with open('./desafio2.json') as file:
    usuarios = json.load(file)

# Armazena os dados obtidos em cada iteração da consulta
data = []    

for usuario in usuarios:
    # Preenche as informações para pesquisa e limpa o campo de pesquisa
    inp.clear()
    inp.send_keys(usuario)
    
    # Aguarda o botão ser clicável para fazer as buscas
    wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)
    wait.until(EC.element_to_be_clickable(mark=botao))
    botao.click()
    
    # Obtém todos os usuários encontrados na busca
    locator = (By.CSS_SELECTOR, 'div.users-list > div > img')
    wait.until(EC.visibility_of_all_elements_located(locator=locator))
    users = driver.find_elements(By.CSS_SELECTOR, 'div.users-list > div')

    # faz a iteração das informações recolhidas na URL através da lista "users" com os usuarios encontrados
    for user in users:
        foto = user.find_element(By.TAG_NAME, 'img')
        nome = user.find_element(By.TAG_NAME, 'h3')
        profissao = user.find_element(By.TAG_NAME, 'span')
        email = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(1)')
        telefone = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(2)')
        perfil = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(3)')
        estado = user.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(4)')
        
        # salva os dados obtidos na CLASSE Usuario -> objeto @dataclass Usuario
        dados_do_usuario = Usuario(
            foto = foto.get_attribute('src'),
            nome = nome.text,
            profissao = profissao.text,
            email = email.text[8:],
            telefone = telefone.text[10:],
            perfil = perfil.text[9:],
            estado = estado.text[8:]
        )
        # Armazena os dados obtidos
        data.append(dados_do_usuario)

driver.quit()

# SALVAR EM JSON -> from dataclasses import asdict
# ensure_ascii=False -> Não converte os caracteres especiais
# w -> abre arquivo em mode de escrita. Se não tiver o arquivo, ele será criado.
# asdict(d) -> obtém os dados como sendo um dicionario

with open('dados_capturados.json', 'w') as file:
    dado_formatado =  [asdict(d) for d in data]
    json.dump(dado_formatado, file, ensure_ascii=False)


#SALVAR EM CSV - import csv // from dataclases import fields
# fields -> fields(Usuario)[0].name

with open('dados_capturados.csv', 'w') as arquivocsv:
    cabecalho = [field.name for field in fields(Usuario)]
    file = csv.DictWriter(arquivocsv, fieldnames=cabecalho)

    file.writeheader()

    dado_formatado =  [asdict(d) for d in data]
    file.writerows(dado_formatado)

