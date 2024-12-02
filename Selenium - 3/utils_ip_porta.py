from selenium.webdriver.common import utils

ip = utils.find_connectable_ip(host='google.com')
print(ip)

# Testar uma conexão em uma porta específica
porta_espec = utils.is_connectable(port=8000, host='localhost')
print(porta_espec)