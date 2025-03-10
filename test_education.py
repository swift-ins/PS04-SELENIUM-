from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Функция для извлечения параграфов статьи
def get_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")  # Находим все параграфы
    return [p.text for p in paragraphs if p.text.strip()]  # Возвращаем только непустые параграфы

# Функция для извлечения связанных статей
def get_related_links(browser):
    links = browser.find_elements(By.CSS_SELECTOR, "div.mw-parser-output p a")  # Находим все ссылки в тексте статьи
    return [link.text for link in links if link.text.strip()]  # Возвращаем только непустые названия статей

# Функция для вывода меню и обработки выбора пользователя
def show_menu(browser):
    while True:
        print("\n1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Выберите действие: ")

        if choice == "1":
            # Листать параграфы
            paragraphs = get_paragraphs(browser)
            for i, paragraph in enumerate(paragraphs, 1):
                print(f"\n--- Параграф {i} ---")
                print(paragraph)
                if i < len(paragraphs):
                    next_action = input("\nНажмите Enter для продолжения или введите 'выход', чтобы вернуться в меню: ")
                    if next_action.lower() == "выход":
                        break
        elif choice == "2":
            # Перейти на связанную страницу
            links = get_related_links(browser)
            if not links:
                print("Связанные статьи не найдены.")
                continue
            print("\nСвязанные статьи:")
            for i, link in enumerate(links, 1):
                print(f"{i}. {link}")
            link_choice = input("Выберите номер статьи (или введите 'выход', чтобы вернуться в меню): ")
            if link_choice.lower() == "выход":
                continue
            try:
                link_index = int(link_choice) - 1
                if 0 <= link_index < len(links):
                    # Кликаем на выбранную ссылку
                    selected_link = browser.find_element(By.LINK_TEXT, links[link_index])
                    selected_link.click()
                    print(f"Переход на статью: {links[link_index]}")
                    time.sleep(5)  # Ждём загрузки страницы
                else:
                    print("Неверный номер статьи.")
            except ValueError:
                print("Введите корректный номер.")
        elif choice == "3":
            # Выход из программы
            print("Завершение программы.")
            browser.quit()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Основной код
browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

# Проверяем, тот ли сайт открылся
assert "Википедия" in browser.title
time.sleep(5)

# Находим окно поиска и вводим запрос
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys("education")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Переходим на статью ""
article_link = browser.find_element(By.LINK_TEXT, "education")
article_link.click()
time.sleep(5)

# Запускаем меню
show_menu(browser)