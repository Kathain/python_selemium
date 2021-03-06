from selenium import webdriver
import time

#в данном тесте мы проверяем ожидаемый результат или нет, и сравниваем

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//body/div[1]/form[1]/div[1]/div[1]/input[1]")
    input1.send_keys("Ura")
    input2 = browser.find_element_by_xpath("//body/div[1]/form[1]/div[1]/div[2]/input[1]")
    input2.send_keys("Koz")
    input3 = browser.find_element_by_xpath("//body/div[1]/form[1]/div[1]/div[3]/input[1]")
    input3.send_keys("test@kkk.kom")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()