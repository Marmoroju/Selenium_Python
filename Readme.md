Iniciar a biblioteca Selenium
```bash
pip install selenium
```

Iniciar o servidor http através do python
```bash
python -m http.server -d dist/
```

Manter navegador aberto
```bash
from IPython.display import HTML

driver = webdriver.Chrome()
HTML(driver.page_source)
```