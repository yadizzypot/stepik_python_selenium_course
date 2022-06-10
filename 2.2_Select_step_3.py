from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    y = num1 + num2
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y)) # ищем элемент с текстом "Python"

    
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
        
    
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()