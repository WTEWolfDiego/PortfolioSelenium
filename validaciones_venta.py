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
urlTest1="https://validaciones.rodrigovillanueva.com.mx/Venta_Pantalla_ok.html"
combo_Producto="product"
combo_opcionVal1="Pantalla" 
combo_opcionVal2="Xbox"
combo_opcionVal3="Laptop"
input_quantity="quantity"
input_price="price"
str_quantityVal="5"
str_priceVal="15.4"
btn_limpiar="//button[@onclick='resetForm()']"
btn_enviar="//button[@onclick='validateAndCalculate()']"


driver.get(urlTest1)
driver.maximize_window()


#=============================Completing the form and cleaning =================================

time.sleep(4)
comboProducto = driver.find_element(By.ID,combo_Producto)
valorproducto= Select(comboProducto)

valorproducto.select_by_visible_text(combo_opcionVal1)
time.sleep(2)
valorproducto.select_by_visible_text(combo_opcionVal2)
time.sleep(2)
valorproducto.select_by_visible_text(combo_opcionVal3)
time.sleep(2)

driver.find_element(By.ID,input_quantity).send_keys(str_quantityVal)
driver.find_element(By.ID,input_price).send_keys(str_priceVal)

time.sleep(2)

driver.find_element(By.XPATH,btn_limpiar).click()

#=======================================Completing the form and sending=================================

time.sleep(4)
comboProducto = driver.find_element(By.ID,combo_Producto)
valorproducto= Select(comboProducto)

valorproducto.select_by_visible_text(combo_opcionVal1)
time.sleep(2)
valorproducto.select_by_visible_text(combo_opcionVal2)
time.sleep(2)
valorproducto.select_by_visible_text(combo_opcionVal3)
time.sleep(2)

driver.find_element(By.ID,input_quantity).send_keys(str_quantityVal)
driver.find_element(By.ID,input_price).send_keys(str_priceVal)
driver.find_element(By.XPATH,btn_enviar).click()

time.sleep(2)


driver.close()
