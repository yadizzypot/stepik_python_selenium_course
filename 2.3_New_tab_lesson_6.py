from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    
    
    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(str(y))
    
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()