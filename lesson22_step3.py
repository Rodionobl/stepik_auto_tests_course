from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

linkone = "https://suninjuly.github.io/selects1.html"
linktwo = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(linktwo)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = int(x_element.text)

    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = int(y_element.text)
    r = x + y

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(r))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
