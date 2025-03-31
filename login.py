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
urlTest1="https://validaciones.rodrigovillanueva.com.mx/Login_ok.html"
input_username="username"
input_password="password" 
str_usernameVal="Diegotest"
str_passwordVal="TEst@#1271"
btn_limpiar="//button[@onclick='resetForm()']"
btn_enviar="//button[@onclick='validateForm()']"


driver.get(urlTest1)
driver.maximize_window()


#=============================Completing the form and cleaning =================================

time.sleep(4)

username=driver.find_element(By.ID,input_username)
password=driver.find_element(By.ID,input_password)

username.send_keys(str_usernameVal)
password.send_keys(str_passwordVal)

time.sleep(2)

driver.find_element(By.XPATH,btn_limpiar).click()


#=======================================Completing the form and sending=================================

username.send_keys(str_usernameVal)
password.send_keys(str_passwordVal)

time.sleep(2)

driver.find_element(By.XPATH,btn_enviar).click()

time.sleep(2)
username.clear()
password.clear()


driver.close()
