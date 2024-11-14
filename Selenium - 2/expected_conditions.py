from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from IPython.display import HTML
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
HTML(driver.page_source)

driver.get('http://localhost:8000/#/exemplo/5')

wait = WebDriverWait(driver=driver, timeout=30, poll_frequency=1)

# title_is/tile_contains -> Aguarda condição do título da página
driver.refresh()
teste = wait.until(EC.title_contains(title='Programador'))
print(teste)

# presence_of_element_located -> Aguarda até que aquele elemento esteja disponível na tela
driver.refresh()
teste2 = wait.until(EC.presence_of_element_located(locator=(By.ID, 'star1')))
print(teste2)

# presence_of_all_element_located
driver.refresh()
teste3 = wait.until(EC.presence_of_all_elements_located(locator=(By.NAME, 'stars')))
print(teste3)


# visibility_of_element_located -> Aguarda até que aquele elemento (imagem) esteja visível na tela 
driver.refresh()
teste4 = wait.until(EC.visibility_of_element_located(locator=(By.NAME, 'stars')))
print(teste4)

# element_to_be_clickable -> Aguarda até que o elemento se torne clicável
driver.refresh()
teste5 = wait.until(EC.element_to_be_clickable(mark=(By.ID, 'telegram')))
print(teste5)

# staleness_of -> Aguarda até que determinado elemento suma da página
driver.refresh()
estrela = driver.find_element(By.ID, 'star4')
teste6 = wait.until(EC.staleness_of(element=estrela))

# element_attribute_to_include -> Para elementos dinâminos de telas que mudam de atributos
# como se foi clicado ou não
driver.refresh()
wait.until(EC.element_attribute_to_include(
    locator=(By.ID, 'star5'),
    attribute_='name'
))


# alert_is_present -> Aguarda até que um alerta/pop-up esteja presente na tela
# não possui timer ou parâmetro para ser executado
driver.refresh()
wait.until(EC.alert_is_present())

