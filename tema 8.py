'''
Tema 8 - SELECTORS
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 7 și ia notițe în caz că ți-a scăpat ceva.
'''

'''
Exerciții obligatorii - grad de dificultate: Usor spre Mediu
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
'''


from time import sleep  # importam ca sa stea deschisa pagina
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)  # initializarea serviciilor in chrome
# # maximizam fereastra
chrome.maximize_window()

'''
Selector by ● ID
'''
# Navigam catre un url
# chrome.get('https://formy-project.herokuapp.com/form')
# sleep(5)
# first_name = chrome.find_element(By.ID, 'first-name')
# first_name.send_keys('Daniela')
# chrome.find_element(By.ID, 'last-name').send_keys('Minzala')
# chrome.find_element(By.ID, 'job-title').send_keys('Automation tester')
# sleep(3)
# chrome.quit()

'''
Selector by ● Link text
'''
# navigam catre un url
# chrome.get('https://formy-project.herokuapp.com/')
# sleep(5)
# # exemplul 1
# # selector by link_text
# link_test = chrome.find_element(By.LINK_TEXT, 'Autocomplete')
# link_test.click()
# chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()

# exemplul 2
# link_test = chrome.find_element(By.LINK_TEXT, 'Buttons')
# link_test.click()
# chrome.find_element(By.LINK_TEXT, 'Buttons').click()

# exemplul 3
# link_test = chrome.find_element(By.LINK_TEXT, 'Dropdown')
# link_test.click()
# chrome.find_element(By.LINK_TEXT, 'Dropdown').click()
# sleep(10)
# chrome.quit()

'''
Selector by ● Parțial link text
'''
#navigam catre un url
# chrome.get('https://the-internet.herokuapp.com/')
# sleep(5)

# exemplul 1
# try:
# partial_link_test = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Context')
# partial_link_test.click()
# except Exception as e:
#     print(f'Nu am gasit elementul cautat')
# print('Am ajuns aici')

# exemplul 2
# partial_link_test = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Broken')
# partial_link_test.click()

# exemplul 3
# partial_link_test = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Controls')
# partial_link_test.click()
#
# sleep(3)
# chrome.quit()

'''
Selector by ● Name
'''
#navigam catre un url
# chrome.get('http://www.seleniumframework.com/Practiceform/')
# sleep(5)

# exemplul 1
# link_test = chrome.find_element(By.NAME, 'country')
# link_test.send_keys('Romania')  # este mai babeste
# chrome.find_element(By.NAME, 'country').send_keys('Romania')  # sau asa

# exemplul 2
# link_test = chrome.find_element(By.NAME, 'company')
# link_test.send_keys('Ager press')

# exemplul 3
# chrome.find_element(By.NAME, 'email').send_keys('dariana@gmail.com')
#
# sleep(5)
# chrome.quit()

'''
Selector by ● Tag*
'''
#navigam catre un url
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
#
# sleep(5)
# #selector by TAG cand e unul singur
# chrome.find_element(By.TAG_NAME, 'input').click()
#
# sleep(5)
# le punem intr-o lista
# input_list = chrome.find_elements(By.TAG_NAME, 'input')
# #print(input_list)
# input_list[0].send_keys('Lahovari')
# input_list[1].send_keys('Marghiloman nr.2')
# input_list[2].send_keys('Batistei nr.1')
# sleep(5)
# chrome.quit()

'''
Selector by ● Class name*
'''
#navigam catre un url
# chrome.get('https://formy-project.herokuapp.com/form')
# sleep(5)

# daca avem Clasa unica
# chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('Marcel')

#daca avem mai multe, le punem intr-o lista
# input_list = chrome.find_elements(By.CLASS_NAME, 'form-control')
#print(input_list)
# input_list[0].send_keys('Marcel')
# input_list[1].send_keys('Iures')
# input_list[2].send_keys('actor')
# sleep(5)
# chrome.quit()

'''
Selector by ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
'''
# # navigam catre un url
# chrome.get('https://formy-project.herokuapp.com/form')
#
#
# # selector by CSS SELECTOR - ID
# chrome.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys('Minzala')
#
# # selector by CSS Class - only first one if multiple matches
# chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('Daniela')
#
# # selector by CSS atribut-valoare partiala + parinte -> copil
# chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="last name"]').send_keys(' GH.')
#
# sleep(5)
# chrome.quit()

'''
Selector by Xpath
Identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.
'''


# # selector by XPATH

# ● 3 după atribut-valoare

# # navigam catre un url
# chrome.get("https://formy-project.herokuapp.com/form")
# sleep(5)
# chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('Daniela')
# chrome.find_element(By.XPATH, '//input[@id="last-name"]').send_keys('Minzala')
# chrome.find_element(By.XPATH, '//input[@id="job-title"]').send_keys('automation tester')
#--------------------

# ● 3 după text

#  Ex.1
# navigam catre un url
# chrome.get("https://formy-project.herokuapp.com/form")
# sleep(5)
# chrome.find_element(By.XPATH, '//a[text()="Submit"]').click()

# Ex.2
# chrome.get("https://the-internet.herokuapp.com/")
# sleep(5)
# chrome.find_element(By.XPATH, '//a[text()="Dropdown"]').click()

#  Ex.3
# chrome.get("https://the-internet.herokuapp.com/")
# chrome.find_element(By.XPATH, '//a[text()="Context Menu"]').click()
# sleep(5)
#--------------------

# ● 1 după parțial text

# full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Drop")]').text
# print(full_text) # asa extrage textul elementului
# full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Drop")]')
# full_text.click() # Si asa da click si deschide
#--------------------

# ● 1 cu SAU, folosind pipe |

# chrome.get("https://formy-project.herokuapp.com/form")
# sleep(5)
# text = chrome.find_element(By.XPATH, '//input[@id="last-name"] | //input[@id="last-name2"] | //input[@id="last-name3"]')
# text.send_keys('Minzala')
# text.screenshot('testauto2.png')
#--------------------

#● 1 cu *

# chrome.get("https://formy-project.herokuapp.com/form")
# sleep(5)
# chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Daniela')
#--------------------

# ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci cu (xpath)[1]

# chrome.get("https://formy-project.herokuapp.com/form")
# sleep(5)
# chrome.find_element(By.XPATH, '(//input[@class="form-control"])[1]').send_keys('Daniela')
#--------------------

# ● 1 în care să folosești parent::

# chrome.get("https://formy-project.herokuapp.com/form")
# sleep(5)
# text1 = chrome.find_element(By.XPATH, '//form//label[text()="First name"]/parent::strong')
# text1.screenshot('strong.png')
#--------------------

# ● 1 în care să folosești fratele anterior sau de după (la alegere)

# chrome.get('https://formy-project.herokuapp.com/form')
# sleep(5)
# text1 = chrome.find_element(By.XPATH, '//form//label[text()="First name"]/parent::*/following-sibling::input')
# //form//label[text()="First name"]/parent::* = reprezinta strong-ul
# /following-sibling::input # fratele cel mic al lui strong
#--------------------

# chrome.get('https://formy-project.herokuapp.com/form')
# sleep(5)
# text2 = chrome.find_element(By.XPATH, '//form//label[text()="First name"]/parent::*/following-sibling::input/preceding-sibling::strong')
# //form//label[text()="First name"]/parent::* = reprezinta strong-ul
# /following-sibling::input/preceding-sibling::strong  # fratele cel mare al lui strong
#--------------------

# ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu ce element vreau să interacționez.
#
chrome.get('https://formy-project.herokuapp.com/form')


def formy_input_by_placeholder(placeholder_text, input_value):  # parametru - placeholder_text, input_value
    my_input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')  # caut dupa placeholder_text
    my_input.clear()
    my_input.send_keys(input_value)


formy_input_by_placeholder('Enter first name', 'Dana')   # chem fct cu placeholder_text si input_value Aladin
formy_input_by_placeholder('Enter last name', 'Mi')
formy_input_by_placeholder('Enter your job title', 'QA automation')
sleep(5)


def label_formy(label, input_value):
    # chrome.get('https://formy-project.herokuapp.com/form')
    my_input = chrome.find_element(By.XPATH, f'//label[text()="{label}"]/parent::strong/parent::div//input')
    my_input.clear()
    my_input.send_keys(input_value)


label_formy('Job title', 'automation tester')
label_formy('First name', 'Daniela')
label_formy('Last name', 'Minzala')

sleep(10)
chrome.quit()