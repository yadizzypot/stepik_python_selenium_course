from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    label = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    
    #button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(str(y))
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit_button.click()
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()