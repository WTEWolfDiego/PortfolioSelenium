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
urlTest1="https://validaciones.rodrigovillanueva.com.mx/Radios_Ok.html"


input_nombre ="campo1"
nombre_val="Diego"
input_tel="campo2"
tel_val="123456789"
radiobutton_1="opcion1"
radiobutton_2="opcion2"
checkbutton_1="opcionA"
checkbutton_2="opcionB"
btn_limpiar="//button[@onclick='limpiarFormulario()']"
btn_enviar="//button[@type='submit']"

driver.get(urlTest1)
driver.implicitly_wait(5)
driver.maximize_window()

#===================completing fields,checking radiobuttons and checkboxes and cleaning the form==================================

driver.find_element(By.ID,input_nombre).send_keys(nombre_val)
driver.find_element(By.ID,input_tel).send_keys(tel_val)
driver.find_element(By.ID,radiobutton_1).click()
driver.find_element(By.ID,radiobutton_2).click()
driver.find_element(By.ID,checkbutton_1).click()
driver.find_element(By.ID,checkbutton_2).click()
driver.find_element(By.XPATH,btn_limpiar).click()
time.sleep(2)

#===================completing fields,checking radiobuttons and checkboxes and sending the form==================================

driver.find_element(By.ID,input_nombre).send_keys(nombre_val)
driver.find_element(By.ID,input_tel).send_keys(tel_val)
driver.find_element(By.ID,radiobutton_1).click()
driver.find_element(By.ID,radiobutton_2).click()
driver.find_element(By.ID,checkbutton_1).click()
driver.find_element(By.ID,checkbutton_2).click()
driver.find_element(By.XPATH,btn_enviar).click()
time.sleep(2)


driver.close()
