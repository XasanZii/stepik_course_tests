import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://suninjuly.github.io/math.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    print(x_element)
    x = x_element.text
    y = calc(x)
    print(y)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()
    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()





finally:
    time.sleep(10)
    browser.quit()
