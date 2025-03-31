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
urlTest1="https://validaciones.rodrigovillanueva.com.mx/Campos_Dos_OK.html"

input_solletras="onlyLetters"
soloLetras_val ="ABCDEFGHIJKLMNOPQRSTUVWYZ"
input_alfanumerico="alphanumeric"
alfanumerico_val="ABCDEFGHIJKLMNOPQRSTUVWYZ12345689"
input_email="emailFormat"
email_val="diego@yopmail.com"
input_url="urlFormat"
url_val="https://www.google.com"
calendar_date="dateFormat"
calendarDate_val="03/04/2025"
btn_limpiar="//button[@type='reset']"
btn_enviar="//button[@type='submit']"




driver.get(urlTest1)
driver.implicitly_wait(5)
driver.maximize_window()

#===================completing fields,checking radiobuttons and checkboxes and cleaning the form==================================
driver.find_element(By.ID,input_solletras).send_keys(soloLetras_val)
driver.find_element(By.ID,input_alfanumerico).send_keys(alfanumerico_val)
driver.find_element(By.ID,input_email).send_keys(email_val)
driver.find_element(By.ID,input_url).send_keys(url_val)
driver.find_element(By.ID,calendar_date).send_keys(calendarDate_val)
driver.find_element(By.XPATH,btn_limpiar).click()
time.sleep(2)
#===================completing fields,checking radiobuttons and checkboxes and sending the form==================================
driver.find_element(By.ID,input_solletras).send_keys(soloLetras_val)
driver.find_element(By.ID,input_alfanumerico).send_keys(alfanumerico_val)
driver.find_element(By.ID,input_email).send_keys(email_val)
driver.find_element(By.ID,input_url).send_keys(url_val)
driver.find_element(By.ID,calendar_date).send_keys(calendarDate_val)
driver.find_element(By.XPATH,btn_enviar).click()
time.sleep(2)

driver.close()
