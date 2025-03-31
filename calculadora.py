from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"c:\drivers\chromedriver.exe"
service= Service(chrome_driver_path)
driver=webdriver.Chrome(service=service)
urlTest1="https://validaciones.rodrigovillanueva.com.mx/Calculador_ok.html"


input_numero1 ="numero1"
numero1_val="4"
input_numero2="numero2"
numero2_val="3"
input_resultado="resultado"

btn_sumar="//button[@onclick='sumar()']"
btn_restar="//button[@onclick='restar()']"
btn_multiplicar="//button[@onclick='multiplicar()']"
btn_limpiar="//button[@onclick='limpiarFormulario()']"



driver.get(urlTest1)
driver.implicitly_wait(5)
driver.maximize_window()

#===================completing fields,checking radiobuttons and checkboxes and cleaning the form==================================


driver.find_element(By.ID,input_numero1).send_keys(numero1_val)
driver.find_element(By.ID,input_numero2).send_keys(numero2_val)
driver.find_element(By.XPATH,btn_sumar).click()
time.sleep(2)
driver.find_element(By.XPATH,btn_restar).click()
time.sleep(2)
driver.find_element(By.XPATH,btn_multiplicar).click()
time.sleep(2)
driver.find_element(By.XPATH,btn_limpiar).click()
time.sleep(2)


driver.close()
