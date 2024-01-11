import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

url = "https://www.adideandalucia.es/index.php?view=normativa"
arc_json = '../JSON/ConserGPT_DATA.json'

# Configura el controlador del navegador (asegúrate de tener el controlador de Chrome instalado)
chrome_path = "../chromedriver.exe"
service = ChromeService(chrome_path)

# First page
driver = webdriver.Chrome(service=service)

# Abre la página web
driver.get(url)

# Espera a que el contenido dinámico generado por JavaScript cargue completamente
# Puedes ajustar este tiempo según sea necesario
driver.implicitly_wait(10)

# Encuentra la tabla por algún identificador, clase, etc.

module = driver.find_elements(By.XPATH, "//div[@class='module-inner']")


def datosTitle():
    finalJSON = {}
    # Recorre Todos los Modulos
    for oneModuleInner in module:
        # Obtiene La letra
        letter = oneModuleInner.find_element(By.TAG_NAME, 'h3')
        finalJSON["Letter"] = letter.text
        # Obtiene el resto
        tableI = oneModuleInner.find_element(By.TAG_NAME, 'tbody')

        print("Trabajando con: ", letter.text)

        if oneModuleInner:
            # print(letter.text)
            for tr in tableI.find_elements(By.TAG_NAME, 'tr'):
                # print("Entrando al tr...")
                for td in tr.find_elements(By.TAG_NAME, 'td'):
                    # print("Entrando al td...")
                    for a in td.find_elements(By.TAG_NAME, 'a'):
                        finalJSON["Info"] = {}
                        finalJSON["Info"]["Title"] = a.text
                        finalJSON["Info"]["SectionLink"] = a.get_property(
                            'href')
        else:
            return finalJSON

        # Cierra la página web
        driver.close()

        # for h3 in h3s:
        # if len(h3.text) == 1:
        # datos_title.append(h3.text)


with open(arc_json, 'w') as archivo:
    archivo.write(datosTitle())

print(datosTitle())
# Second page
# Abrir y cerrar cuando se use
# driverInside = webdriver.Chrome(service=service)

# Cierra la página web
driver.close()
# driverInside.close()
