"""
Задание: оформляем тесты в стиле unittest

Попробуйте оформить тесты из первого модуля в стиле unittest.

    Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
    Создайте новый файл
    Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
    Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
    Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
    Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
    Запустите получившиеся тесты из файла
    Просмотрите отчёт о запуске и найдите последнюю строчку
    Отправьте эту строчку в качестве ответа на это задание

Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы
использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае,
здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения.
"""


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def registration(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input3.send_keys("ip@ip.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    browser.quit()
    return welcome_text


class TestUni(unittest.TestCase):
    def test_uni1(self):
        answer = registration("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", answer)

    def test_uni2(self):
        answer = registration("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", answer)
