from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


try:
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    browser = webdriver.Chrome(options=options)
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)
    x2 = browser.find_element_by_id("num1").text
    y2 = browser.find_element_by_id("num2").text
    x1 = int(x2)
    y1 = int(y2)
    summa = x1 + y1
    print(summa)
    browser.find_element_by_tag_name("select").click()
    xp1 = '//option[@value="' + str(summa) +'"]'
    # xp1 = f'//option[@value="{summa}"]'
    print(xp1)
    browser.find_element_by_xpath(xp1).click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()




    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()



