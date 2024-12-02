from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from IPython.display import HTML
from dataclasses import dataclass, asdict, fields
import json, csv


driver = webdriver.Chrome()
HTML(driver.page_source)
driver.get('http://localhost:8000/#/desafio/4')
driver.maximize_window()
actions = ActionChains(driver)


@dataclass
class Produto:
    titulo: str
    e_frete_gratis: bool
    e_parcelamento_sem_juros: bool
    e_envio_internacional: bool
    esta_em_oferta: bool
    num_estrelas: int
    descricao: str
    foto: str
    preco: int

wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)
driver.implicitly_wait(time_to_wait=10)

# AUTOMAÇÃO DO CODIGO

def acessar_produtos(categoria: str):
    
    #garante que a função sempre seja executada nessa pagina
    driver.get('http://localhost:8000/#/desafio/4')
    
    (
        ActionChains(driver)
        .click(driver.find_element(By.XPATH, f'//h1[contains(text(), "{categoria}")]'))
        .perform()
    )

def capturar_dados_dos_produtos():
    dados = []
    
    while True:
        wait.until(EC.visibility_of_all_elements_located(
            locator = (By.CSS_SELECTOR, 'form#filtros + div div > img')
        ))
        produtos = driver.find_elements(By.CSS_SELECTOR, 'form#filtros + div div:has(>img)')

        for produto in produtos:
            dados_do_produto = Produto (
                titulo = produto.find_element(By.TAG_NAME, 'h5').text,
                e_frete_gratis = True if produto.find_elements(By.CSS_SELECTOR, 'div.bg-blue-100') else False,
                e_parcelamento_sem_juros = True if produto.find_elements(By.CSS_SELECTOR, 'div.bg-green-100') else False,
                e_envio_internacional= True if produto.find_elements(By.CSS_SELECTOR, 'div.bg-orange-100') else False,
                esta_em_oferta = True if produto.find_elements(By.CSS_SELECTOR, 'div.bg-purple-100') else False,
                num_estrelas = len(produto.find_elements(By.CSS_SELECTOR, 'svg.text-yellow-300')),
                descricao = produto.find_element(By.TAG_NAME, 'p').text,
                foto = produto.find_element(By.TAG_NAME, 'img').get_attribute('src'),
                preco = produto.find_element(By.CSS_SELECTOR, 'div:has(>span:nth-last-child(2)) > span:nth-child(2)').text,
            )  

            dados.append(dados_do_produto)   

        #proximo = driver.find_element(By.CSS_SELECTOR, 'form#filtros + div button:last-child')
        proximo = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div[2]/div/div/div/div[2]/button[2]')
        try:
            proximo.click()
        except:
            break
    
    return dados

def preencher_filtros (
        frete_gratis = bool,
        parcelamento_sem_juros = bool,
        envio_internacional = bool,
        em_oferta = bool,
        preco_minimo = int,
        preco_maximo = int,
        nota = int,     
    ):
    # Captura dos filtros
    frete = driver.find_element(By.ID, 'frete')
    parcelamento = driver.find_element(By.ID, 'parcelamento')
    internacional = driver.find_element(By.ID, 'envio-internacional')
    oferta = driver.find_element(By.ID, 'oferta')

    # Captura dos preços
    preco_de = driver.find_element(By.ID, 'price-from')
    preco_ate = driver.find_element(By.ID, 'price-to')

    # Captura de classificação (estrelas)
    nota5 = driver.find_element(By.ID, 'five-stars')
    nota4 = driver.find_element(By.ID, 'four-stars')
    nota3 = driver.find_element(By.ID, 'three-stars')
    nota2 = driver.find_element(By.ID, 'two-stars')
    nota1 = driver.find_element(By.ID, 'one-star')

    # Captura do botao buscar/limpar
    buscar = driver.find_element(By.CSS_SELECTOR, 'form#filtros button[type="submit"]')
    limpar = driver.find_element(By.CSS_SELECTOR, 'form#filtros button[type="reset"]')

    actions = ActionChains(driver)
    actions.click(limpar)

    if frete_gratis:
        actions.click(frete)
    if parcelamento_sem_juros:
        actions.click(parcelamento)
    if envio_internacional:
        actions.click(internacional)
    if em_oferta:
        actions.click(oferta)

    # Limpar campos de preço
   
    actions.key_down(Keys.CONTROL)
    actions.send_keys_to_element(preco_de, 'a')
    actions.key_up(Keys.CONTROL)
    actions.send_keys_to_element(preco_de, Keys.DELETE)
    
    actions.key_down(Keys.CONTROL)
    actions.send_keys_to_element(preco_ate, 'a')
    actions.key_up(Keys.CONTROL)
    actions.send_keys_to_element(preco_ate, Keys.DELETE)

     # Preenche preços
    actions.send_keys_to_element(preco_de, preco_minimo)
    actions.send_keys_to_element(preco_ate, preco_maximo)

    #preenche estrela
    match nota:
        case 5:
            actions.click(nota5)
        case 4:
            actions.click(nota4)
        case 3:
            actions.click(nota3)
        case 2:
            actions.click(nota2)
        case 1:
            actions.click(nota1)

    actions.click(buscar)
    actions.perform()


# EXECUÇÃO
acessar_produtos(categoria='Celulares')
preencher_filtros (
        frete_gratis = True,
        parcelamento_sem_juros = False,
        envio_internacional = False,
        em_oferta = True,
        preco_minimo = 500,
        preco_maximo = 2500,
        nota = 4,     
)
#capturar_dados_dos_produtos()
celulares = capturar_dados_dos_produtos()


# EXPORTAÇÃO DOS DADOS
todos_os_produtos = celulares
with open('desafio3.json', 'w') as file:
    data_formatada = [asdict(d) for d in todos_os_produtos] 
    json.dump(data_formatada, file, ensure_ascii=False)

with open('desafio3.csv', 'w') as csvfile:
    headers = [field.name for field in fields(Produto)]
    file = csv.DictWriter(csvfile, fieldnames=headers)

    file.writeheader()

    data_formatada = [asdict(d) for d in todos_os_produtos] 
    file.writerows(data_formatada)

