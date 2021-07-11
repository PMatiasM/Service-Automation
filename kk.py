import pyautogui
from selenium import webdriver
import time, keyboard

lugar = input("Informe o local desejado: ")
data = input("Informe a data (AA-MM-DD): ")
options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
options.binary_location=r'C:/Program Files/Google/Chrome/Application'
driver = webdriver.Chrome(executable_path=r'C:/Users/User/Desktop/CD/chromedriver.exe')
driver.get("http://www.proeis.rj.gov.br/")
def marcar():

    a = driver.find_element_by_xpath(f"//input[@name='btnNovaInscricao']")
    a.click()
    time.sleep(0.3)
    b = driver.find_element_by_xpath(f"//span[@id='select2-chosen-1']")
    b.click()
    time.sleep(0.3)
    c = driver.find_element_by_xpath(f"//*[text()='{lugar}']")
    c.click()
    
    pyautogui.press('tab')
    pyautogui.press('enter')

    d = driver.find_element_by_xpath(f"//*[text()='{data}']")
    d.click()
    time.sleep(0.3)
    f = driver.find_element_by_xpath("//input[@name='btnConsultar']")
    f.click()


keyboard.add_hotkey('ctrl + shift + 9', marcar)
keyboard.wait('ctrl + 0')