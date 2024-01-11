from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService


def tableScrap(driver):
    driver.implicitly_wait(10)

    tables = driver.find_elements(By.TAG_NAME, "table")

    lista_dic = []

    for table in tables:
        if table:
            for fila in table.find_elements(By.TAG_NAME, "tr"):
                for columna in fila.find_elements(By.TAG_NAME, "td"):
                    enlaces = columna.find_elements(By.TAG_NAME, 'a')
                    if enlaces:
                        for enlace in enlaces:
                            datos_enlace = {}
                            datos_enlace['Titulo'] = enlace.text
                            datos_enlace['Enlace'] = enlace.get_property(
                                "href")
                            lista_dic.append(datos_enlace)

    # Cierra el navegador
    driver.quit()

    return lista_dic
