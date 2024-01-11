from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService


def titleScrap(driver):
    driver.implicitly_wait(10)
    # Encuentra la tabla por algún identificador, clase, etc.

    module = driver.find_elements(By.XPATH, "//div[@class='module-inner']")

    datos_title = []

    for titles in module:
        h3s = titles.find_elements(By.TAG_NAME, 'h3')
        if titles:
            for h3 in h3s:
                if len(h3.text) == 1:
                    datos_title.append(h3.text)

    # Cierra el navegador
    driver.quit()

    return datos_title
