import time
from selenium import webdriver


driver = webdriver.Chrome('E:\drivers\chrome\chromedriver.exe')
driver.get('https://www.google.com/')
time.sleep(2)
buscar = driver.find_element_by_name("q")
buscar.send_keys("hlacomunicaciones")