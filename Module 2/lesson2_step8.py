"""Задание: загрузка файла

В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

    Открыть страницу http://suninjuly.github.io/file_input.html
    Заполнить текстовые поля: имя, фамилия, email
    Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    Нажать кнопку "Submit"

Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого
задания."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Marco')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Polo')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('Marco@Polo.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    time.sleep(5)
    browser.quit()
