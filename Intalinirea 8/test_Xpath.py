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

# navigam catre un url
chrome.get("https://formy-project.herokuapp.com/form")
sleep(5)
''' incercari Matei
# selector by XPATH - folosind wildcard
chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Matei')
# selector by XPATH - navigare in jos trecand prin fiecare elemet
chrome.find_element(By.XPATH, '//div/div/input[@id="last-name"]').send_keys('Oltean')
# selector by XPATH - navigare in jos skip tags pana la elementul dorit
chrome.find_element(By.XPATH, '//div//input[@id="job-title"]').send_keys('tester')

'''
# selector by XPATH - atribut=valoare
# chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('M')
# # selector by XPATH - (folosind wildcard) * toate elementele care respecta regula
# chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Mat')
# # selector by XPATH - navigare in jos trecand prin fiecare elemet
# chrome.find_element(By.XPATH, '//div/div/input[@id="first-name"]').send_keys('Matei')
# # selector by XPATH - navigare in jos - skip tags - cautam oriunde in form un input care sa respecte regula
# chrome.find_element(By.XPATH, '//form//input[@id="first-name"]').send_keys('Matei CORVIN')
# # selector by XPATH - selectare element din lista - indexul incepe de la 1
# chrome.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('Matei CORVIN')

# selector by XPATH - OR = | primul gasit dintre variante
s = chrome.find_element(By.XPATH, '//input[@id="last-name1"] | //input[@id="last-name2"] | //input[@id="last-name3"]')
# stergem valorile din input
s.clear()
s.send_keys('Matei')
# # xpath search by partial text
# chrome.get('https://formy-project.herokuapp.com/form')
# full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Sub")]').text
# print(full_text)
# # xpath  search by text
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.XPATH, '//a[text()="Submit"]').click()


sleep(10)
chrome.quit()




