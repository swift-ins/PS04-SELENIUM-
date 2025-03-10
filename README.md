README для скрипта с Selenium
Описание
Этот скрипт использует Selenium для автоматического поиска информации на русскоязычной Википедии. Пользователь вводит запрос, после чего программа открывает соответствующую страницу и предлагает несколько вариантов действий.

Установка зависимостей
Перед запуском убедитесь, что у вас установлены все необходимые библиотеки:

bash
Kopēt
Rediģēt
pip install selenium
Также необходимо установить WebDriver для Chrome.

Как использовать
Запустите скрипт:
bash
Kopēt
Rediģēt
python script.py
Введите поисковый запрос.
После загрузки страницы выберите одно из действий:
1: Просмотреть все параграфы на странице.
2: Перейти на случайную связанную страницу.
3: Выйти из программы.
Основные функции
paragraph_listing() – извлекает и отображает текст всех параграфов на текущей странице.
variants() – предлагает пользователю выбор действий.
Переход по случайной ссылке – выбирается случайный элемент с классом "hatnote navigation-not-searchable ts-main", и выполняется переход по его ссылке.
Примечания
Скрипт использует Chrome WebDriver, поэтому убедитесь, что он установлен и соответствует версии вашего браузера.
Для надежной работы рекомендуется использовать актуальную версию Selenium.
Лицензия
Этот проект распространяется под лицензией MIT.
