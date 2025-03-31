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

input_nombre ="nombre"
nombre_val="Diego"
btn_click_Action="//button[@onclick='clickAction()']"
btn_dblclick_Action="//button[@ondblclick='doubleClickAction()']"
btn_mouseOver_Action="//button[@onmouseover='hoverAction()']"
btn_rightclick_Action="//button[@oncontextmenu='rightClickAction(event)']"
btn_mouseDown_Action="//button[@onmousedown='mouseDownAction()']"
btn_mouseUp_Action="//button[@onmouseup='mouseUpAction()']"
btn_focusAction="//button[@onfocus='focusAction()']"
btn_blurAction="//button[@onblur='blurAction()']"

urlTest1="https://validaciones.rodrigovillanueva.com.mx/Botones_ok.html"



driver.get(urlTest1)
driver.implicitly_wait(5)
driver.maximize_window()

#===================clicking on each button==================================

driver.find_element(By.ID,input_nombre).send_keys(nombre_val)
driver.find_element(By.XPATH,btn_click_Action).click()
driver.find_element(By.XPATH,btn_dblclick_Action).click()
driver.find_element(By.XPATH,btn_mouseOver_Action).click()
driver.find_element(By.XPATH,btn_rightclick_Action).click()
driver.find_element(By.XPATH,btn_mouseDown_Action).click()
driver.find_element(By.XPATH,btn_mouseUp_Action).click()
driver.find_element(By.XPATH,btn_focusAction).click()
driver.find_element(By.XPATH,btn_blurAction).click()
time.sleep(2)


driver.close()
