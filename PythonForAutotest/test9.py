from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    testa1 = browser.find_element_by_xpath('//input[@id="answer"]')
    testa1.send_keys(calc(x))
    testa2 = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    testa2.click()
    testa3 = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    testa3.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
