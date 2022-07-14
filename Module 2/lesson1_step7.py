"""Задание: поиск сокровища с помощью get_attribute

В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

    Открыть страницу http://suninjuly.github.io/get_attribute.html.
    Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    Посчитать математическую функцию от x (сама функция остаётся неизменной).
    Ввести ответ в текстовое поле.
    Отметить checkbox "I'm the robot".
    Выбрать radiobutton "Robots rule!".
    Нажать на кнопку "Submit".

Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.



Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с
числом. Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    treasure = browser.find_element(By.ID, 'treasure')
    x = treasure.get_attribute('valuex')
    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(calc(x))

    for selector in ['[id="robotCheckbox"]', '[id="robotsRule"]', '.btn']:
        browser.find_element(By.CSS_SELECTOR, selector).click()

finally:
    time.sleep(30)
    browser.quit()
