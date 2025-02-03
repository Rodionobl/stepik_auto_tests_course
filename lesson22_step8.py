from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    input1.send_keys("Name")

    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    input2.send_keys("lastname")

    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    input3.send_keys("email@ttt.hu")

    input4 = browser.find_element(By.CSS_SELECTOR, "input[name='file']")
    input4.send_keys(os.path.abspath(__file__))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
