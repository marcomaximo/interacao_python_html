from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Executa ChromeDriver
driver = webdriver.Chrome(executable_path=r"C:\Users\55169\Desktop\chromedriver.exe")


#Abrir site
driver.get("https://www.google.com")


#Maximiza a janela
driver.maximize_window()


#Clicar no campo de inserção de texto
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click()


#Digitar busca
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Datacoin")


#Delay de 3 segundos
time.sleep(3)


#Clicar no botão de pesquisa
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()