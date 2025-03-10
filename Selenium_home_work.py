from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.keys import Keys

def paragraph_listing():
    # Находим все параграфы на странице
    paragraphs = browser.find_elements(By.TAG_NAME, "p")

    for paragraph in paragraphs:
        print()   
        print(paragraph.text)
    #    input("Нажмите Enter для продолжения...")

query = input('Input search   ')

browser = webdriver.Chrome()
#browser.get("https://wikipedia.org")
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

search_box = browser.find_element(By.NAME, "search")
search_box.send_keys(query)
time.sleep(3)
search_box.send_keys(Keys.RETURN)

def variants():
    print('Варианты дейсвий :')
    print('1 : листать параграфы')
    print('2 : перейти на одну из связанных страниц' )
    print('3 : выйти из программы')

    var = int(input('1, 2 или 3 ?  '))

    if var == 1:
        paragraph_listing()
        variants()
    elif var == 2:

        # Поиск элементов с нужным классом
        hatnotes = []
        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable ts-main":
                hatnotes.append(element)


        # Проверяем, нашли ли мы нужные элементы
        if hatnotes:
            hatnote = random.choice(hatnotes)
            link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
            print(f"Переход по ссылке: {link}")
            
            browser.get(link)
        else:
            print("Не найдено элементов с классом 'hatnote navigation-not-searchable ts-main'")
        variants()
    else:
        browser.quit()

variants()
