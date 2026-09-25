from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


#modo dev mostrando pantalla
""" 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
"""

#Modo desatendido

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)
try:
    driver.get("https://www.saucedemo.com/")
    print("Ok - sitio web abierto")
    #type
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    print("add user name")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    print("envio password")
    
    #assert element present
    login =driver.find_element(By.ID,"login-button")
    assert login.is_displayed(),"El boton no esta visible"
    login.click()
    print("ok-botón login visible")
    
    #login-button
    titulo=driver.find_element(By.CLASS_NAME,"title").text
    assert titulo =="Products","el titulo Products no se encuentra"
    print("titulo products encontrado")
    
    imagen=driver.find_element(By.CSS_SELECTOR,'[data-test="inventory-item-sauce-labs-backpack-img"]')
    assert imagen.is_displayed(),"imagen no existe"
    print("imagen back-pack visible")

    producto=driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert producto=="Sauce Labs Backpack","no se encuentra el producto "
    print("ok - producto encontrado")

finally:
    driver.quit()



