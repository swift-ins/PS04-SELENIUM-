from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
import time

browser = webdriver.Chrome()

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
            
# Проверяем, тот ли сайт открылся
assert "Википедия" in browser.title
time.sleep(10)

# Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")

# Вводим текст в строку поиска
search_box.send_keys("Солнечная система")

# Нажимаем Enter
search_box.send_keys(Keys.RETURN)
time.sleep(10)

# Находим ссылку на страницу "Солнечная система" и кликаем
a = browser.find_element(By.LINK_TEXT, "Солнечная система")
a.click()

# Закрываем браузер через некоторое время
time.sleep(10)
browser.quit()
