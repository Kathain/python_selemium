from selenium import webdriver
import time
import math

# этот тест нажимает на кнопку и переходит на вторую вкладку и делает действие на второй вкладке
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    troll_button = browser.find_element_by_xpath("//button[contains(text(),'I want to go on a magical journey!')]").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
    # first_window = browser.window_handles[0]
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
