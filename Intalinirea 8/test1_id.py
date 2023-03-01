'''  Obiective Întâlnire 8

● Să verificăm dacă are toată lumea proiectul pe github
● Să aprofundăm și să sedimentam diferitele tipuri de selectori
○ Id
○ Link Text
○ Partial Link Text
○ Name
○ Tag
○ Class name
○ CSS
○ Xpath
'''

'''
Id

● În Terminal: pip install webdriver-manager si pip install selenium
● Deschidem Chrome
● Navigăm către url dorit (ex: https://formy-project.herokuapp.com/form)
● Click dreapta pe elementul ce dorim să îl inspectăm
● Selectați opțiunea ‘Inspect’
● Veți găsi partea de html a unui website
● Structura e următoarea:
○ tag sau webelement (ex: <input>)
○ atribut=”valoare” (ex: type=”text” id=”first-name”)
● Copiem ID al elementului dorit (ex: ‘first-name’)
'''
# pip install selenium
# pip install webdriver-manager

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
# maximizam fereastra
driver.maximize_window()

# navigam catre un url
driver.get('https://formy-project.herokuapp.com/form')

# selector by ID
try:
    first_name = driver.find_element(By.ID, 'first-name')
    first_name.send_keys('Matei')
except Exception as e:
    print('ID-ul introdus nu este corect')
print('Am ajuns aici')
#driver.find_element(By.ID, 'first-name').send_keys('TEST AUTOMATION')

sleep(10)
# inchidem ferestra de chrome
driver.quit()
