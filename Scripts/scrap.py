from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

from titleScrap import titleScrap
from tableScrap import tableScrap

url = "https://www.adideandalucia.es/index.php?view=normativa"

# Configura el controlador del navegador (asegúrate de tener el controlador de Chrome instalado)
chrome_path = "./chromedriver.exe"
service = ChromeService(chrome_path)
driver = webdriver.Chrome(service=service)

# Abre la página web
driver.get(url)

# Espera a que el contenido dinámico generado por JavaScript cargue completamente
# Puedes ajustar este tiempo según sea necesario
driver.implicitly_wait(10)

print(titleScrap(driver=driver))
print(tableScrap(driver=driver))
