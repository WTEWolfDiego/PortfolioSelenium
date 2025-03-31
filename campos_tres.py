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
urlTest1="https://validaciones.rodrigovillanueva.com.mx/Campos_Tres_OK.html"

driver.get(urlTest1)
driver.maximize_window()
input_phone="phone"
input_noSpaces="noSpaces"
input_noSpecialChars="noSpecialChars"
input_password="password"
input_range="range"
input_whitelist="whitelist"
str_phoneVal="527576889"
str_noSpacesVal="estetextoessinespacios"
str_noSpecialCharsVal="test123456789"
str_passwordVal="Testing123$"
str_rangeVal="30"
str_whitelistVal="python"
btn_limpiar="//button[@type='reset']"
btn_enviar="//button[@type='submit']"

#=============================Completing the form and cleaning =================================

time.sleep(5)
driver.find_element(By.ID,input_phone).send_keys(str_phoneVal)
driver.find_element(By.ID,input_noSpaces).send_keys(str_noSpacesVal)
driver.find_element(By.ID,input_noSpecialChars).send_keys(str_noSpecialCharsVal)
driver.find_element(By.ID,input_password).send_keys(str_passwordVal)
driver.find_element(By.ID,input_range).send_keys(str_rangeVal)
driver.find_element(By.ID,input_whitelist).send_keys(str_whitelistVal)

driver.find_element(By.XPATH,btn_limpiar).click()
time.sleep(2)

driver.find_element(By.ID,input_phone).send_keys(str_phoneVal)
driver.find_element(By.ID,input_noSpaces).send_keys(str_noSpacesVal)
driver.find_element(By.ID,input_noSpecialChars).send_keys(str_noSpecialCharsVal)
driver.find_element(By.ID,input_password).send_keys(str_passwordVal)
driver.find_element(By.ID,input_range).send_keys(str_rangeVal)
driver.find_element(By.ID,input_whitelist).send_keys(str_whitelistVal)
time.sleep(2)
driver.find_element(By.XPATH,btn_enviar).click()


#=======================================Completing the form and sending=================================

time.sleep(2)

driver.close()
