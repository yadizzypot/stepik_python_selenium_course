from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    labels = browser.find_elements(By.TAG_NAME, 'label') # Список лэйблов над текстовыми полями
    inputs = browser.find_elements(By.TAG_NAME, 'input') # Список текстовых полей

    for i, label in enumerate(labels):          # Если последний символ
        if label.text[-1] == '*':               # лейбла над текстовым полем равен "*",
            inputs[i].send_keys('Dimka is perfect!')   # то в поле ввода печатаем "Обязалово!"

    
    time.sleep(1)
    
    current_dir = os.path.abspath(os.path.dirname('__file__'))     # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')                           # добавляем к этому пути имя файла 
    
    print(current_dir + '   ' + file_path)
    
    forfile = browser.find_element(By.CSS_SELECTOR, '#file')
    forfile.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()