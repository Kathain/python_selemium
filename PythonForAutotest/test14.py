from selenium import webdriver
import time
import math

# этот тест нажимает ок в аллерте и потом считает по формуле и вводит ответ
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_xpath("//button[contains(text(),'I want to go on a magical journey!')]")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_id('input_value').text
    print("Valuex is ", x_element)
    assert x_element is not None, "Valuex YES"
    x = x_element
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    testa1 = browser.find_element_by_xpath('//input[@id="answer"]')
    testa1.send_keys(calc(x))

 #   okki = browser.find_element_by_xpath('//input[@id="answer"]')
  #  okki.send_keys(calc(x))
    button1 = browser.find_element_by_xpath("//button[contains(text(),'Submit')]")
    button1.click()




    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
