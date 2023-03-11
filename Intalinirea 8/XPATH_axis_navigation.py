from time import sleep  # importam ca sa stea deschisa pagina
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
# initializarea serviciilor in 'chrome'
driver = webdriver.Chrome(service=s)
# maximizam fereastra
driver.maximize_window()
# navigam catre un url
driver.get('https://formy-project.herokuapp.com/form')

# exemplu cu parinte - aka parintele la label = strong
# text1 = driver.find_element(By.XPATH, '//form//label[text()="First name"]/parent::strong')
# text1.screenshot('strong.png')


# exemplu cu pipe - pipe reprezinta " | " care tine locul de sau
# text2 = chrome.find_element(By.XPATH, '//input[@id="last-name"] | //input[@id="last-name2"] | //input[@id="last-name3"]')
# # text2.send_keys('Test Auto2')
# # text2.screenshot('testauto2.png')


#exemplu cu or
# text3 = chrome.find_element(By.XPATH, '//input[@id="last-name"]' or '//input[@id="last-name2"]' or '//input[@id="last-name3"]')
# text3.send_keys('Test Auto3')
# text3.screenshot('testauto3.png')


#exemplu frate
# text1 = chrome.find_element(By.XPATH, '//form//label[text()="First name"]/parent::*/following-sibling::input')
# //form//label[text()="First name"]/parent::* = reprezinta strong-ul
# /following-sibling::input = fratele lui strong


# text1 = chrome.find_element(By.XPATH, '//form//label[text()="First name"]/parent::*/following-sibling::input/preceding-sibling::strong')
# aici m-am "intors" la "fratele" strong al lui input - e o "porcarie" la baza, dar pentru a demonstra proprietatile "fratilor"


# Cu ajutorul unei functii cand avem foarte multe elemente de acelasi tip
# si vrem sa parametrizam selectorul

# def formy_input_by_placeholder(placeholder_text, input_value):  # parametru - placeholder_text, input_value
#     my_input = driver.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]') #  caut dupa placeholder_text
#     my_input.clear()
#     my_input.send_keys(input_value)
#
#
# formy_input_by_placeholder('Enter first name', 'Aladin')  # apleze fct cu placeholder_text si input_value Aladin
# formy_input_by_placeholder('Enter last name', 'SALAM')
# formy_input_by_placeholder('Enter your job title', 'QA AUTOMATION')
# sleep(5)
# def label_formy(label, input_value):
#     driver.get('https://formy-project.herokuapp.com/form')
#     my_input = driver.find_element(By.XPATH, f'//label[text()="{label}"]/parent::strong/parent::div//input')
#     my_input.clear()
#     my_input.send_keys(input_value)
#
#
# label_formy('Job title', 'INGINER')
# label_formy('First name', 'Florin')
# label_formy('Last name', 'SALAM')

sleep(5)
driver.quit()