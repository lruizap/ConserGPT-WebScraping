import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

url = "https://www.adideandalucia.es/index.php?view=normativa"
arc_json = '../JSON/ConserGPT_DATA.json'

finalJSON = {}

try:
    # Configura las opciones del navegador para deshabilitar la carga de imágenes
    chrome_options = Options()
    chrome_options.add_argument("--disable-images")
    chrome_options.add_argument("--disable-extensions")

    # Configura el controlador del navegador con las opciones
    chrome_path = "../chromedriver.exe"
    service = ChromeService(chrome_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Abre la página web
    driver.get(url)

    # Espera a que el contenido dinámico generado por JavaScript cargue completamente
    # Puedes ajustar este tiempo según sea necesario
    driver.implicitly_wait(10)

    # Encuentra la tabla por algún identificador, clase, etc.
    module_elements = driver.find_elements(
        By.XPATH, "//div[@class='module-inner']")

    # Recorre Todos los Modulos
    for oneModuleInner in module_elements:
        # Obtiene La letra
        letter = oneModuleInner.find_element(By.TAG_NAME, 'h3').text

        # Si la letra no existe en finalJSON, crea un nuevo diccionario
        if len(letter) == 1:
            if letter not in finalJSON:
                finalJSON[letter] = {"Info": []}

            # Obtiene el resto
            tableI = oneModuleInner.find_element(By.TAG_NAME, 'tbody')

            print("Trabajando con: ", letter)

            if oneModuleInner:
                for tr in tableI.find_elements(By.TAG_NAME, 'tr'):
                    for td in tr.find_elements(By.TAG_NAME, 'td'):
                        for a in td.find_elements(By.TAG_NAME, 'a'):
                            link = a.get_property('href')
                            title = a.text

                            info_data = {"Title": title,
                                         "SectionLink": link, "ListPDF": []}

                            try:
                                # Second page
                                driver2 = webdriver.Chrome(service=service)
                                driver2.get(link)
                                driver2.implicitly_wait(10)
                                moduleGlobal = driver2.find_element(
                                    By.XPATH, "//ul[@class='lista']")

                                for li in moduleGlobal.find_elements(By.TAG_NAME, 'li'):
                                    liText = li.text
                                    for a in li.find_elements(By.TAG_NAME, 'a'):
                                        pdfLink = a.get_property('href')

                                    pdfTotal = {
                                        "Text": liText,
                                        "LinkPDF": pdfLink,
                                    }

                                    info_data["ListPDF"].append(pdfTotal)

                                driver2.close()

                            except Exception as e:
                                print(f"Error en la segunda página: {e}")
                                break

                            finalJSON[letter]["Info"].append(info_data)

    # Cierra la página web
    driver.close()

    with open(arc_json, 'w') as archivo:
        json.dump({"modules": finalJSON}, archivo)

except Exception as e:
    with open(arc_json, 'w') as archivo:
        json.dump({"modules": finalJSON}, archivo)
    print(f"Error general: {e}")
