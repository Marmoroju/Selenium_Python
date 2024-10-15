from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython.display import HTML

driver = webdriver.Chrome()
HTML(driver.page_source)

url = 'http://localhost:8000/#/exemplo/1'
driver.get(url)

# styled-input.optional-info são duas classes de CSS
multi_class = driver.find_elements(By.CLASS_NAME, 'styled-input.optional-info')
multi_class
for mc in multi_class:
    value = mc.get_property('value')
    print(value)
