from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(str(y))
    
    iamrobot = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    iamrobot.click()
    
    robotrule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robotrule.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
        
    
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()