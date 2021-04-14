from selenium import webdriver
import time
import math

#в этой задаче мы искали у картинки чему равен ее атрибут и его потом везде подтягивали

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value").text
    print("Valuex is ", x_element)
    x = x_element
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    testa1 = browser.find_element_by_xpath('//input[@id="answer"]')
    testa1.send_keys(calc(x))
    testa2 = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    testa2.click()
    browser.execute_script("window.scrollBy(0, 150);")
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
