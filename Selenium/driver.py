from selenium import webdriver
from IPython.display import HTML

driver = webdriver.Chrome()
HTML(driver.page_source)

driver.get('https://google.com')

# driver.refresh()
# driver.maximize_window()
# driver.minimize_window()
# driver.fullscreen_window()

driver.get('https://youtube.com')
driver.back()
driver.forward()

driver.quit()


