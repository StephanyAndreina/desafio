
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import win32com.client as win32
import datetime
import pyautogui 
import pandas as pd



driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://www.youtube.com")
time.sleep(2)
id	= driver.current_window_handle
time.sleep(2)

driver.switch_to.new_window('window')
time.sleep(2)
driver.get("https://br.pinterest.com/pin/1071153092614551882/")
time.sleep(2)
driver.switch_to.window(id)
time.sleep(2)

driver.switch_to.new_window('window')
time.sleep(2)
driver.get("https://dolarhoje.com/")
time.sleep(2)

id= driver.find_element("id","nacional")
valor= id.get_attribute("value")
time.sleep(5)

print(valor)

data = datetime.datetime.now()


print(data)


df={
	'dolar' : valor,
	'hora/dia' : data
}

df.to_excel('modolo.xlsx', index=False)
