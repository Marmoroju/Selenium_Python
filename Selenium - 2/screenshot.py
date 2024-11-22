from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from IPython.display import HTML
import base64 

driver = webdriver.Chrome()
HTML(driver.page_source)

driver.get('http://localhost:8000/#/exemplo/1')
driver.implicitly_wait(time_to_wait=10)


driver.save_screenshot(filename='./screenshots/0.png')

driver.get_screenshot_as_file(filename='./screenshots/1.png')

main = driver.find_element(By.TAG_NAME, 'main')
main.screenshot(filename='./screenshots/2.png')

#import base64 -> para fazer conversão de arquivos para PDF
with open('./arquivo.pdf', 'wb') as file:
    #print_page serve como a opção de imprimir página no navegador (não imprime o CSS)
    data = driver.print_page()

    #conversão de base
    data_converted = base64.b64decode(data)

    file.write(data_converted)