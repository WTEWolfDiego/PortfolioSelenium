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
urlTest1="https://validaciones.rodrigovillanueva.com.mx/Form1.html"
input_nombre="nombre"
nombre_val="Diego"
input_apellidos="apellidos"
apellidos_val="Testing"
input_tel="tel"
tel_val="123456789"
input_email="email"
email_val="diego@yopmail.com"
input_direccion="direccion"
direccion_val="av. Rivadavia 5300"
btn_limpiar="//button[@type='reset']"
btn_enviar="//button[@type='submit']"


driver.get(urlTest1)
driver.implicitly_wait(5)
driver.maximize_window()

#===================completing the fields and cleaning all==================

driver.find_element(By.ID,input_nombre).send_keys(nombre_val)
driver.find_element(By.ID,input_apellidos).send_keys(apellidos_val)
driver.find_element(By.ID,input_tel).send_keys(tel_val)
driver.find_element(By.ID,input_email).send_keys(email_val)
driver.find_element(By.ID,input_direccion).send_keys(direccion_val)
time.sleep(2)
driver.find_element(By.XPATH,btn_limpiar).click()

#===================Completing the fields again to send information==========

driver.find_element(By.ID,input_nombre).send_keys(nombre_val)
driver.find_element(By.ID,input_apellidos).send_keys(apellidos_val)
driver.find_element(By.ID,input_tel).send_keys(tel_val)
driver.find_element(By.ID,input_email).send_keys(email_val)
driver.find_element(By.ID,input_direccion).send_keys(direccion_val)
time.sleep(2)
driver.find_element(By.XPATH,btn_enviar).click()
time.sleep(2)
#====================Finishing the test=======================================

driver.close()
