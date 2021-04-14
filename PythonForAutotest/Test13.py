from selenium import webdriver
import time
import os
import math

#в этой задаче мы заполнили 3 поля и вставили текстовый файл в поле  (можно использовать этот код для создания файла через скрип-
# with open("test.txt", "w") as file:
#     content = file.write("automationbypython")  # create test.txt file
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input_name = browser.find_element_by_xpath("//body/div[1]/form[1]/div[1]/input[1]").send_keys("Иван")
    input2_surname = browser.find_element_by_xpath("//body/div[1]/form[1]/div[1]/input[2]").send_keys("Алехин")
    input3_email = browser.find_element_by_xpath("//body/div[1]/form[1]/div[1]/input[3]").send_keys("test@test.com")
    element = browser.find_element_by_xpath("//input[@id='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "Doc2_test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element_by_xpath("//button[contains(text(),'Submit')]")
    button.click()



    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
