from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

# Находим все параграфы на странице
"""paragraphs = browser.find_elements(By.TAG_NAME, "p")
for paragraph in paragraphs:
    print()

    
    print(paragraph.text)
 #   input("Нажмите Enter для продолжения...")"""

# Поиск элементов с нужным классом
hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

# Проверяем, нашли ли мы нужные элементы
if hatnotes:
    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    print(f"Переход по ссылке: {link}")
    browser.get(link)
else:
    print("Не найдено элементов с классом 'hatnote navigation-not-searchable'")

browser.quit()
