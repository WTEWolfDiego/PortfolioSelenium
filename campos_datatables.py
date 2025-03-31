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
urlTest1="https://validaciones.rodrigovillanueva.com.mx/Datatables_OK.html"
btn_addRecord="//button[@data-target='#addRecordModal']"
input_nombre="nombre"
input_apellidos="apellidos"
input_telefono="telefono"
str_nombreVal="Diego"
str_apellidosVal="Testing"
str_telefonoVal="123456789"
btn_cancel="//button[@data-dismiss='modal']"
btn_limpiar="//button[@onclick='resetForm()']"
btn_enviar="//button[@onclick='addRecord()']"

driver.get(urlTest1)
driver.maximize_window()





#=============================Completing the form and cleaning =================================

time.sleep(5)

driver.find_element(By.XPATH,btn_addRecord).click()
time.sleep(3)
driver.find_element(By.ID,input_nombre).send_keys(str_nombreVal)
driver.find_element(By.ID,input_apellidos).send_keys(str_apellidosVal)
driver.find_element(By.ID,input_telefono).send_keys(str_telefonoVal)
time.sleep(3)
driver.find_element(By.XPATH,btn_cancel).click()
time.sleep(3)
#=========================Cleaning the fields==================================================

driver.find_element(By.XPATH,btn_addRecord).click()
time.sleep(3)
driver.find_element(By.ID,input_nombre).send_keys(str_nombreVal)
driver.find_element(By.ID,input_apellidos).send_keys(str_apellidosVal)
driver.find_element(By.ID,input_telefono).send_keys(str_telefonoVal)
time.sleep(3)
driver.find_element(By.XPATH,btn_limpiar).click()
time.sleep(3)
#===========================Adding a new record=================================================

driver.find_element(By.ID,input_nombre).send_keys(str_nombreVal)
driver.find_element(By.ID,input_apellidos).send_keys(str_apellidosVal)
driver.find_element(By.ID,input_telefono).send_keys(str_telefonoVal)
time.sleep(3)
driver.find_element(By.XPATH,btn_enviar).click()


time.sleep(2)


#=======================================Completing the form and sending=================================

driver.close()
