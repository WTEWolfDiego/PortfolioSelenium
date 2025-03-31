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
urlTest1="https://validaciones.rodrigovillanueva.com.mx/Tiempos_Ok.html"

input_nombre="field1"
input_apellidos="field2"
combo_opciones='comboBox'
check_TyC="checkbox"
str_nombreVal="Diego"
str_apellidosVal="Testing"
combo_opcionVal="Opción 1"
btn_limpiar="//button[@onclick='resetForm()']"
btn_enviar="//button[@onclick='validateForm()']"

driver.get(urlTest1)
driver.maximize_window()




#=============================Completing the form and cleaning =================================

time.sleep(10)

driver.find_element(By.ID,input_nombre).send_keys(str_nombreVal)
time.sleep(5)
driver.find_element(By.ID,input_apellidos).send_keys(str_apellidosVal)
time.sleep(5)
combo1 = driver.find_element(By.ID,combo_opciones)
valorCombo=Select(combo1)
valorCombo.select_by_visible_text(combo_opcionVal)
time.sleep(2)
driver.find_element(By.ID,check_TyC).click()
time.sleep(2)
driver.find_element(By.XPATH,btn_limpiar).click()
time.sleep(2)


#=======================================Completing the form and sending=================================

driver.find_element(By.ID,input_nombre).send_keys(str_nombreVal)
time.sleep(1)
driver.find_element(By.ID,input_apellidos).send_keys(str_apellidosVal)
time.sleep(1)
combo1 = driver.find_element(By.ID,combo_opciones)
valorCombo=Select(combo1)
valorCombo.select_by_visible_text(combo_opcionVal)
time.sleep(1)
driver.find_element(By.ID,check_TyC).click()
time.sleep(1)
driver.find_element(By.XPATH,btn_enviar).click()
time.sleep(1)

driver.close()
