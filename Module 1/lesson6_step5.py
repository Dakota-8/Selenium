"""Задание: поиск элемента по тексту в ссылке

В этой задаче мы попробуем искать элементы по тексту ссылки, для этого воспользуемся методом find_element_by_link_text:

link = browser.find_element(By.LINK_TEXT, text)

В качестве аргумента в метод передается такой текст, ссылку с которым мы хотим найти. Это тот самый текст, который
содержится между открывающим и закрывающим тегом <a> вот тут </a>

Допустим, на странице https://www.degreesymbol.net/ мы хотим найти ссылку с текстом "Degree symbol in Math" и перейти
по ней. Если хотим найти элемент по полному соответствию текста, то нам подойдет такой код:

link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
link.click()

А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код:

link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
link.click()

Обычно поиск по подстроке чуть более удобный и гибкий, но с ним надо быть вдвойне аккуратными и проверять, что находится
нужный элемент.
Задание

На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

    Добавьте в самый верх своего кода import math
    Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
    Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:

    str(math.ceil(math.pow(math.pi, math.e)*10000))

    (можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже
    его использовать в вашем коде)

    Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации

    Заполните скриптом форму так же как вы делали в предыдущем шаге урока
    После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    find_text = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    find_text.click()

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
