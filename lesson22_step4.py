from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

browser.execute_script("alert('Robots at work');")
time.sleep(10)
browser.quit()
