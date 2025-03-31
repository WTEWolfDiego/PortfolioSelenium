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
urlTest1="https://validaciones.rodrigovillanueva.com.mx/Campos_Uno_OK.html"
input_obligatorio="obligatorio"
obligatorio_val="Esto es una automatizacion en Selenium con Python"
input_minlength="minLength"
minlength_val="Testing"
input_maxlength="maxLength"
maxLength_val="Testing"
input_onlyNumbers="onlyNumbers"
numbers_val="123456789"
btn_enviar="//button[@type='submit']"


driver.get(urlTest1)
driver.implicitly_wait(5)
driver.maximize_window()

#=================Completing the fields======================================

driver.find_element(By.ID,input_obligatorio).send_keys(obligatorio_val)
driver.find_element(By.ID,input_minlength).send_keys(minlength_val)
driver.find_element(By.ID,input_maxlength).send_keys(maxLength_val)
driver.find_element(By.ID,input_onlyNumbers).send_keys(numbers_val)
driver.find_element(By.XPATH,btn_enviar).click()
time.sleep(2)


driver.close()
