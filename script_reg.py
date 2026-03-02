from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ищем обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first[required]")
    input1.send_keys("Один")

    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second[required]")
    input2.send_keys("Два")

    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third[required]")
    input3.send_keys("Три")

    # отправка формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!"

finally:
    time.sleep(10)
    browser.quit()
