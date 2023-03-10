from time import sleep  # importam ca sa stea deschisa pagina
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
# maximizam fereastra
chrome.maximize_window()

#navigam catre un url
chrome.get('https://formy-project.herokuapp.com/')

sleep(5)
#selector by link_text
link_test = chrome.find_element(By.LINK_TEXT, 'Autocomplete')
link_test.click()

chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()

sleep(10)
chrome.quit()
