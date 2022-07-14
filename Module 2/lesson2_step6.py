"""Задание на execute_script

В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который
дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

    Открыть страницу http://SunInJuly.github.io/execute_script.html.
    Считать значение для переменной x.
    Посчитать математическую функцию от x.
    Проскроллить страницу вниз.
    Ввести ответ в текстовое поле.
    Выбрать checkbox "I'm the robot".
    Переключить radiobutton "Robots rule!".
    Нажать на кнопку "Submit".

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с
числом. Отправьте полученное число в качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script, чтобы сделать прокрутку в область видимости
элементов, перекрытых футером."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
        browser.find_element(By.CSS_SELECTOR, selector).click()


finally:
    time.sleep(5)
    browser.quit()
