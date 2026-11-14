from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    
    
    x_find = browser.find_element(By.ID, "input_value")
    x = x_find.text
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()