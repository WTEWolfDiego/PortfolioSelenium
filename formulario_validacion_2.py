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
urlTest1="https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html"
combobox1="comboBox1"
combobox2="comboBox2"
combobox3="os"
combobox4="version"
valor1_val="Valor 1"
valor2_val="Valor 2"
valor3_val="Valor 3"
os1_val="Linux"
os2_val="Windows"
os3_val="Mac"
windows7_val="Windows 7"
windows10_val="Windows 10"
windows11_val="Windows 11"
btn_enviar="//button[@onclick='validateForm()']"


driver.get(urlTest1)
driver.implicitly_wait(5)
driver.maximize_window()

#=================Selecting the values for each combobox======================================

combovalor=driver.find_element(By.ID,combobox1)
valorSelect = Select(combovalor)
valorSelect.select_by_visible_text(valor1_val)
time.sleep(2)
valorSelect.select_by_visible_text(valor2_val)	
time.sleep(2)
valorSelect.select_by_visible_text(valor3_val)
time.sleep(2)
comboValor2 = driver.find_element(By.ID,combobox2)
valorSelect2 = Select(comboValor2)
valorSelect2.select_by_visible_text(valor1_val)
time.sleep(2)
valorSelect2.select_by_visible_text(valor2_val)
time.sleep(2)
valorSelect2.select_by_visible_text(valor3_val)
time.sleep(3)
combovalor3=driver.find_element(By.ID,combobox3)
valorSelect3 = Select(combovalor3)
valorSelect3.select_by_visible_text(os1_val)
time.sleep(2)
valorSelect3.select_by_visible_text(os2_val)
time.sleep(2)
valorSelect3.select_by_visible_text(os3_val)
time.sleep(2)
valorSelect3.select_by_visible_text(os2_val)
time.sleep(2)
comboValor4=driver.find_element(By.ID,combobox4)
valorSelect4=Select(comboValor4)
valorSelect4.select_by_visible_text(windows7_val)
time.sleep(2)
valorSelect4.select_by_visible_text(windows10_val)
time.sleep(2)
valorSelect4.select_by_visible_text(windows11_val)

time.sleep(3)
driver.find_element(By.XPATH,btn_enviar).click()
time.sleep(2)

driver.close()
