from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from IPython.display import HTML
from dataclasses import dataclass

driver = webdriver.Chrome()
driver.maximize_window()
HTML(driver.page_source)


# torna a classe Usuario uma classe de dados, assim cria uma instância/objeto com os dados solicitados.
@dataclass 
class Usuario:
    foto: str
    nome: str
    profissao: str
    email: str
    telefone: str
    perfil: str
    estado: str

driver.switch_to.window(driver.window_handles[0])

driver.get('http://localhost:8000/#/desafio/2')
driver.implicitly_wait(time_to_wait=10)

driver.switch_to.new_window('tab')
driver.get('http://localhost:8000/#/desafio/3')

janelas = {
    'busca' : driver.window_handles[0],
    'cadastro' : driver.window_handles[1]
}

while True:
    # Mantém o foco na tela de cadastro
    driver.switch_to.window(window_name=janelas['cadastro'])
    try:
        # Obtem o usuario 
        usuario_busca = driver.find_element(By.ID, 'usuario').text
    except:
        # Interrompe se não tiver mais usuario
        break
    
    # Ir para página de busca
    driver.switch_to.window(window_name=janelas['busca'])

    # Pesquisar e obter o dados do usuario
    data = []

    # Preenche as informacoes para a pesquisa
    inp = driver.find_element(By.CSS_SELECTOR, 'main input')
    inp.clear()
    inp.send_keys(usuario_busca)

    # Aguarda o botão ser clicável e faz a busca
    botao = driver.find_element(By.CSS_SELECTOR, 'main button')
    wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)
    wait.until(EC.element_to_be_clickable(mark=botao))
    botao.click()

    # obtém todos os usuários encontrados na busca
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

    # Ir para a aba de cadastro
    driver.switch_to.window(window_name=janelas['cadastro'])

    # Selecionar os elementos de entrada de dados
    nome_cadastro = driver.find_element(By.NAME, 'nome')
    profissao_cadastro = driver.find_element(By.NAME, 'profissao')
    email_cadastro = driver.find_element(By.NAME, 'email')
    telefone_cadastro = driver.find_element(By.NAME, 'telefone')
    perfil_cadastro = driver.find_element(By.NAME, 'usuario')
    estado_cadastro = Select(driver.find_element(By.NAME, 'estado'))

    # Preencher cada um dos campos com os usuarios na lista data[] encontrados na busca
    for dt in data:
        nome_cadastro.clear()
        profissao_cadastro.clear()
        email_cadastro.clear()
        telefone_cadastro.clear()
        perfil_cadastro.clear()
 
        nome_cadastro.send_keys(dt.nome)
        profissao_cadastro.send_keys(dt.profissao)
        email_cadastro.send_keys(dt.email)
        telefone_cadastro.send_keys(dt.telefone)
        perfil_cadastro.send_keys(dt.perfil)
        estado_cadastro.select_by_visible_text(dt.estado)

        # Envior o formulário
        nome_cadastro.submit()

