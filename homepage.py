from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
import pytest



urltest="https://frontend.wildar.dev/Autos"


@pytest.fixture
def driver():
    chrome_driver_path=r"c:\drivers\chromedriver.exe"
    service=Service(chrome_driver_path)
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    #try:    
    yield driver
    #finally:
    #    print("closing driver")
        #driver.quit()


    #=====================Test 1: Searching a car using the filters ===========================
def test_searchCar(driver):

    #============Variables=====================================================================
    driver.get(urltest)
    strbusqueda_sinexito="No se encontraron resultados para la búsqueda especificada."
    input_marca="marca"
    input_modelo="modelo"
    input_anio="anio"
    input_precioMin="precioMin"
    input_precioMax="precioMax"
    str_marca="Alfa Romeo"
    str_modelo="Z3"
    str_anio="1995"
    str_precioMin="10000"
    str_precioMax="30000"
    select_opcion="estado"
    str_opcion1="Todos"
    btn_buscar="//button[@type='submit']"
    strmensajeResultado="//div[@class='alert alert-info' and @role='alert']"
    #=======================================================================================

    print("Test 1: Initialization --- Searching for a car using the filters")
    driver.find_element(By.ID,input_marca).send_keys(str_marca)
    driver.find_element(By.ID,input_modelo).send_keys(str_modelo)
    driver.find_element(By.ID,input_anio).send_keys(str_anio)
    driver.find_element(By.ID,input_precioMin).send_keys(str_precioMin)
    driver.find_element(By.ID,input_precioMax).send_keys(str_precioMax)
    
    select_combo=driver.find_element(By.ID,select_opcion)
    combo_estado = Select(select_combo)
    combo_estado.select_by_visible_text(str_opcion1)
    driver.find_element(By.XPATH,btn_buscar).click()
    mensaje=driver.find_element(By.XPATH,strmensajeResultado)
   
    assert  mensaje.text.strip() == strbusqueda_sinexito

    print("Test 1: Searching for a car using the filters ---> Completed succesfully!")
  
    time.sleep(5)

    #=====================Test 2: Accessing Car details page ===============================    
def test_CarDetails(driver):

    btn_detalles="//tr[1]/td/a[@class='btn btn-info btn-sm']"

    driver.get(urltest)
    print("Test 2: Initialization --- Accessing car details page")
    driver.find_element(By.XPATH,btn_detalles).click()
    time.sleep(5)
    print("Test 2: Accessing car details Page ---> Completed Succesfully!")

    #=====================Test 3: Creating a new car ========================================


def test_CreatingCar(driver):

    btn_registrar="//div/a[@href='/Autos/Crear']"
    input_marca="Marca"
    input_modelo="Modelo"
    input_chasis="NumeroChasis"
    input_anio="Anio"
    input_precio="Precio"
    input_color="Color"
    strmarca="Chevrolet"
    strmodelo="Cruiser"
    strchasis="111111111111111111"
    stranio="2015"
    strprecio="10000"
    strcolor="Verde"
    combo_selector="Estado"
    stropcion1="Usado"
    btn_crear="//input[@type='submit']"

    driver.get(urltest)
    print("Test 3: Initialization - Creating a new car")
    driver.find_element(By.XPATH,btn_registrar).click()
    driver.find_element(By.ID,input_marca).send_keys(strmarca)
    driver.find_element(By.ID,input_modelo).send_keys(strmodelo)
    driver.find_element(By.ID,input_chasis).send_keys(strchasis)
    driver.find_element(By.ID,input_anio).send_keys(stranio)
    driver.find_element(By.ID,input_precio).send_keys(strprecio)
    driver.find_element(By.ID,input_color).send_keys(strcolor)
    select_combo=driver.find_element(By.ID,combo_selector)
    combo_estado=Select(select_combo)
    combo_estado.select_by_visible_text(stropcion1)
    driver.find_element(By.XPATH,btn_crear).click()
    time.sleep(5)
    print("Test 3: Creating a new car ---> Completed Succesfully!")

#===========================Test 4: Editing car details ===============================================

def test_EditCar(driver):

    btn_editar="//tr[2]/td/a[@class='btn btn-warning btn-sm']"
    input_marca="Marca"
    input_modelo="Modelo"
    input_anio="Anio"
    input_precio="Precio"
    input_color="Color"
    strmarca="Alfa Romeo"
    strmodelo="Z3"
    stranio="1998"
    strprecio="50000"
    strcolor="Rojo"
    combo_selector="Estado"
    stropcion1="Usado"
    btn_guardar="//input[@type='submit']"


    driver.get(urltest)
    print("Test 4: Initialization - Editing car details")
    driver.find_element(By.XPATH,btn_editar).click()
    driver.find_element(By.ID,input_marca).clear()
    driver.find_element(By.ID,input_marca).send_keys(strmarca)
    driver.find_element(By.ID,input_modelo).clear()
    driver.find_element(By.ID,input_modelo).send_keys(strmodelo)
    driver.find_element(By.ID,input_anio).clear()
    driver.find_element(By.ID,input_anio).send_keys(stranio)
    driver.find_element(By.ID,input_precio).clear()
    driver.find_element(By.ID,input_precio).send_keys(strprecio)
    driver.find_element(By.ID,input_color).clear()
    driver.find_element(By.ID,input_color).send_keys(strcolor)
    select_combo=driver.find_element(By.ID,combo_selector)
    combo_estado=Select(select_combo)
    combo_estado.select_by_visible_text(stropcion1)    
    driver.find_element(By.XPATH,btn_guardar).click()
    time.sleep(5)
    print("Test 4: Editing car details ---> Completed Succesfully!")

    #=================Test 5: Deleting the new car====================================

def test_DeletingCar(driver):

    driver.get(urltest)
    btn_eliminar="//tr[2]/td/a[@class='btn btn-danger btn-sm']"
    btn_confirmar="//input[@type='submit']"

    print("Test 5: Initialization --- Deleting the new car")
    driver.find_element(By.XPATH,btn_eliminar).click()
    time.sleep(2)
    driver.find_element(By.XPATH,btn_confirmar).click()
    time.sleep(2)
    print("Test 5: Deleting the new car ---> Completed Succesfully!")



