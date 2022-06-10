from pickle import FALSE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    i1 = browser.find_element(By.CSS_SELECTOR, "input:required.first")
    i2 = browser.find_element(By.CSS_SELECTOR, "input:required.second")
    i3 = browser.find_element(By.CSS_SELECTOR, "input:required.third")
    i1.send_keys('fsd')
    i2.send_keys('fsd')
    i3.send_keys('fsd')
    
    time.sleep(3)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    browser.quit()